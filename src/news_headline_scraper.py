import re
import urllib.request
from urllib.error import URLError, HTTPError

def fetch_html(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except URLError as e:
        print(f"Error fetching URL: {e}")
        return None

def extract_headlines(html):
    pattern = r'<h[1-3][^>]*>(.*?)</h[1-3]>'
    raw_headlines = re.findall(pattern, html, re.IGNORECASE | re.DOTALL)

    clean_headlines = []
    for headline in raw_headlines:
        text = re.sub(r'<[^>]+>', '', headline)
        text = re.sub(r'&[^;]+;', '', text)
        text = text.strip()
        if text and text not in clean_headlines:
            clean_headlines.append(text)

    return clean_headlines

def display_headlines(headlines):
    if not headlines:
        print("No headlines found.")
        return
    print("\n--- Extracted Headlines ---")
    for idx, headline in enumerate(headlines, 1):
        print(f"{idx}. {headline}")

def main():
    url = input("Enter the news website URL: ").strip()
    if not url.startswith("http"):
        print("Invalid URL. Must start with http:// or https://")
        return

    html = fetch_html(url)
    if html:
        headlines = extract_headlines(html)
        display_headlines(headlines)

if __name__ == "__main__":
    main()
