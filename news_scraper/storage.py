import csv
import os

CSV_FILE = "articles.csv"

def save_article(url, title, content, label):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode="a", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["url", "title", "content", "label"])
        writer.writerow([url, title, content, label])
