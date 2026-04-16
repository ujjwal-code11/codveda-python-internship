import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape (example: BBC News)
url = "https://www.bbc.com/news"

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find headlines (BBC specific class)
    headlines = soup.find_all("h3")

    # Save to CSV
    with open("headlines.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Headlines"])

        for h in headlines:
            text = h.get_text().strip()
            if text:
                print(text)
                writer.writerow([text])

    print("\n✅ Headlines saved to headlines.csv")

except Exception as e:
    print("Error:", e)