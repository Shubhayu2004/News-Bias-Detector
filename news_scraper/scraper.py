import json
import time
from newspaper import Article
from storage import save_article

def load_sources():
    with open("sources.json") as f:
        return json.load(f)

def extract_articles(url_list, label, max_articles=300):
    for site in url_list:
        print(f"[{label.upper()}] Scraping from: {site}")
        try:
            from newspaper import build
            paper = build(site, memoize_articles=False)
            count = 0
            for article in paper.articles:
                if count >= max_articles:
                    break
                try:
                    article.download()
                    article.parse()
                    if article.text and len(article.text) > 200:
                        save_article(article.url, article.title, article.text, label)
                        count += 1
                    time.sleep(2)  #so what we did here is becuase manny sites will say that timeout has reached so we put 2 seconds time 
                except Exception as e:
                    print("maybe timeout reached", e)
        except Exception as e:
            print("site down", e)

if __name__ == "__main__":
    sources = load_sources()
    for label, urls in sources.items():
        extract_articles(urls, label, max_articles=300)
