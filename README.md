import requests
from bs4 import BeautifulSoup

url = "https://example-blog.com"
response = requests.get(url)  # Fetch the page
soup = BeautifulSoup(response.text, "html.parser")  # Parse HTML

titles = soup.find_all("h2")  # Find all <h2> tags (article titles)
for title in titles:
    print(title.text)
