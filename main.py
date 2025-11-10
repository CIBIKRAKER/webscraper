import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/"   
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

while True:

    print("Welcome to the Webscraper\n" \
    "1. to Scrape the whole Site\n" \
    "2. to Scrape the Titles\n")

    x = input("\nEnter the number of your choice here: ")

    if(x == "1"):
        titles = soup.find_all("html")  

        with open("demofile.txt", "a", encoding="UTF-8") as f:
            for title in titles:
                f.write(f"--------\n{title.text}\n--------")

        with open("demofile.txt", "r", encoding="UTF-8") as f:
            print(f.read())

    elif(x == "2"):
        titles = soup.find_all("h1")  

        with open("demofile.txt", "w", encoding="UTF-8") as f:
            for title in titles:
                f.write(f"--------\n{title.text}\n--------")

        with open("demofile.txt", "r", encoding="UTF-8") as f:
            print(f.read())







