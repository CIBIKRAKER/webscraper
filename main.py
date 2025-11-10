import requests
from bs4 import BeautifulSoup

url =  input("Enter the URL you want to scrape: ")

try:

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    while True:

        print("Welcome to the Webscraper\n" \
        "1. to Scrape the whole Site\n" \
        "2. to Scrape an HTML-Tag\n" \
        "3. To exit")

        x = input("\nEnter the number of your choice here: ")

        if(x == "1"):
            page_text = soup.get_text(separator="\n", strip=True)

            with open("demofile.txt", "w", encoding="utf-8") as f:
                f.write(page_text)

            print(page_text[:500])

        elif(x == "2"):

            tag = input("Type the HTML-Tag: ")

            titles = soup.find_all(tag)  

            with open("demofile.txt", "w", encoding="UTF-8") as f:
                for title in titles:
                    f.write(f"--------\n{title.text}\n--------")

            with open("demofile.txt", "r", encoding="UTF-8") as f:
                print(f.read())
        elif(x== "3"):
            break
except requests.exceptions.RequestException as e:
    print("Error: ", e)
    