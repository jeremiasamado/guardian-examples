# web_scraper.py
import requests
from bs4 import BeautifulSoup
import csv

# Site de treino (seguro e permitido para scraping)
SITE_URL = "https://quotes.toscrape.com/"

def scrape_quotes():
    # Acede ao site
    response = requests.get(SITE_URL, timeout=15)
    response.raise_for_status() # Verifica se houve erro ao aceder
    
    # Analisa o HTML
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []

    # Procura as citações na página
    for quote_element in soup.select(".quote"):
        text = quote_element.select_one(".text").get_text(strip=True)
        author = quote_element.select_one(".author").get_text(strip=True)
        quotes.append({"citação": text, "autor": author})
    
    return quotes

def save_to_csv(quotes, filename="citações.csv"):
    # Guarda as citações num ficheiro CSV
    with open(filename, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["citação", "autor"])
        writer.writeheader()
        writer.writerows(quotes)
    print(f"Citações guardadas em {filename}")

def main():
    print(f"A extrair citações de {SITE_URL}...")
    quotes = scrape_quotes()
    save_to_csv(quotes)
    print(f"Concluído! Extraídas {len(quotes)} citações.")

if __name__ == "__main__":
    main()
