from urllib.parse import quote
import requests
import pandas as pd
from datetime import datetime

def get_wiki_pageviews(article, lang, start_date, end_date):
    article_encoded = quote(article, safe='')
    url = (f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"
           f"{lang}.wikipedia/all-access/user/{article_encoded}/daily/{start_date}/{end_date}")

    headers = {"User-Agent": "MyWikiApp/1.0 (252546@edu.p.lodz.pl)"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Błąd zapytania ({response.status_code}): {response.text}")
        return pd.DataFrame()

    data = response.json().get('items', [])
    if not data:
        print("Brak danych.")
        return pd.DataFrame()

    df = pd.DataFrame([
        {
            'date': datetime.strptime(item['timestamp'][:8], "%Y%m%d"),
            'views': item['views']
        } for item in data
    ])
    return df
def translate_article(article_title, source_lang, target_lang):
    url = f"https://{source_lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "prop": "langlinks",
        "titles": article_title,
        "lllang": target_lang,
        "format": "json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    pages = data.get("query", {}).get("pages", {})
    for page in pages.values():
        langlinks = page.get("langlinks", [])
        if langlinks:
            return langlinks[0].get("*")
    return None

def fetch_wikipedia_languages():
    url = "https://meta.wikimedia.org/w/api.php"
    params = {
        "action": "sitematrix",
        "format": "json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    languages = []

    for key, val in data["sitematrix"].items():
        if key == "count":
            continue
        if isinstance(val, dict) and "site" in val:
            lang_code = val.get("code", "")
            lang_name = val.get("localname", "")
            if any(site["code"] == "wiki" for site in val["site"]):
                languages.append((lang_code, lang_name))

    return sorted(languages)