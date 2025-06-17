from flask import Flask, render_template, request
from utils.visualization import generate_bokeh_chart
from utils.wiki_api import get_wiki_pageviews, translate_article, fetch_wikipedia_languages
from datetime import date
import pandas as pd

app = Flask(__name__)

# Przechowywanie danych globalnie (do filtrowania wykresu bez zmiany tabeli)
global_full_df = pd.DataFrame()

@app.route('/', methods=['GET', 'POST'])
def index():
    global global_full_df
    article_titles, legend_labels, table_data, table_data  = [], [], [], []
    error_msg = None
    script, div = "", ""
    today = date.today().isoformat()
    languages_list = fetch_wikipedia_languages()

    if request.method == 'POST':
        articles_raw = request.form.getlist('article')

        langs = request.form.getlist('language')
        start_date = request.form['start_date'].replace('-', '')
        end_date = request.form['end_date'].replace('-', '')

        articles = [a.strip().replace(' ', '_') for a in articles_raw if a.strip()]
        full_df = pd.DataFrame()
        if request.form.get('clear'):
            global_full_df = pd.DataFrame()  # Reset globalnego DataFrame
            return render_template(
                'index.html',
                table_data=[],
                article_titles=[],
                languages_list=languages_list,
                selected_languages=[],
                selected_start_date='',
                selected_end_date='',
                chart_html=False,
                script='',
                div='',
                legend_labels=[],
                error_msg=None,
                today=today
            )

        for article in articles:
            for lang in langs:
                translated_title = article  # Domyślnie: oryginalny tytuł

                # Jeśli język docelowy różni się od źródłowego (pl), spróbuj przetłumaczyć
                if lang != 'pl':
                    translated = translate_article(article, 'pl', lang)
                    if translated:
                        translated_title = translated.replace(' ', '_')
                    else:
                        continue  # Jeśli brak tłumaczenia, pomiń

                df = get_wiki_pageviews(translated_title, lang, start_date, end_date)
                if df.empty:
                    continue
                display_title = translated_title.replace('_', ' ') if lang != 'pl' else article.replace('_', ' ')
                df['article'] = display_title
                df['lang'] = lang
                df['label'] = display_title + ' (' + lang + ')'
                full_df = pd.concat([full_df, df], ignore_index=True)

        if full_df.empty:
            error_msg = "Nie znaleziono danych dla żadnego z haseł."
        else:
            global_full_df = full_df.copy()
            pivot_df = full_df.pivot_table(index='date', columns='label', values='views', fill_value=0).reset_index()
            pivot_df['date'] = pivot_df['date'].dt.strftime('%Y-%m-%d')
            legend_labels = pivot_df.columns.tolist()
            legend_labels.remove('date')
            table_data = pivot_df.to_dict(orient='records')
            script, div = generate_bokeh_chart(pivot_df)

    return render_template('index.html',
                           table_data=table_data,
                           article_titles=articles_raw if request.method == 'POST' else '',
                           languages_list=languages_list,
                           selected_languages = langs if request.method == 'POST' else '',
                           selected_start_date=request.form.get('start_date', ''),
                           selected_end_date = request.form.get('end_date', ''),
                           chart_html=True,
                           script=script,
                           div=div,
                           legend_labels=legend_labels,
                           error_msg=error_msg,
                           today=today)


if __name__ == '__main__':
    app.run(debug=True)
