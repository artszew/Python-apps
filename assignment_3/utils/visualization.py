from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Legend, DatetimeTickFormatter,DateRangeSlider
from bokeh.palettes import Category10, Category20, Category20b
import pandas as pd

def get_color_palette(n):
    if n <= 2:
        return ['#1f77b4', '#3db41f'][:n]
    elif n <= 10:
        return Category10[n]
    elif n <= 20:
        return Category20[n]
    else:
        return Category20b[20]

def generate_bokeh_chart(pivot_df):
    pivot_df = pivot_df.copy()
    pivot_df['date'] = pd.to_datetime(pivot_df['date'])
    articles = [col for col in pivot_df.columns if col != 'date']
    source = ColumnDataSource(pivot_df)

    # Tworzenie wykresu
    p = figure(
        x_axis_type='datetime',
        height=600,
        sizing_mode="stretch_width",
        tools="pan,box_zoom,reset,save"
    )
    p.title.text = "Popularność artykułów na Wikipedii"
    p.title.align = "center"
    p.title.text_font_size = "18pt"
    p.title.text_font_style = "bold"

    colors = get_color_palette(len(articles))
    renderers = p.varea_stack(
        stackers=articles,
        x='date',
        color=colors[:len(articles)],
        source=source
    )

    legend = Legend(items=[(article, [r]) for article, r in zip(articles, renderers)])
    p.add_layout(legend, 'right')
    p.legend.click_policy = "mute"

    p.yaxis.axis_label = "Liczba odsłon"
    p.yaxis.axis_label_text_font_style = "normal"
    p.yaxis.axis_label_text_font_size = "12pt"
    p.yaxis.major_label_text_font_size = "12pt"
    p.xaxis.major_label_text_font_size = "11pt"
    p.xaxis.formatter = DatetimeTickFormatter(
        days="%d.%m.%Y",
        months="%d.%m.%Y",
        years="%d.%m.%Y"
    )

    # Tworzenie suwaka
    min_date = pivot_df['date'].min()
    max_date = pivot_df['date'].max()

    range_slider = DateRangeSlider(
        title="Zakres dat",
        start=min_date,
        end=max_date,
        value=(min_date, max_date),
        step=1,
        format="%d.%m.%Y",
        width=400
    )
    # Połączenie suwaka z osią X
    range_slider.js_link("value", p.x_range, "start", attr_selector=0)
    range_slider.js_link("value", p.x_range, "end", attr_selector=1)

    # Layout
    layout_ = column(p, range_slider, sizing_mode="stretch_width")

    return components(layout_)
