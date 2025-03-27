from bs4 import BeautifulSoup

import requests

# Ma'lumotlarni yig'ish
url = "https://realpython.github.io/fake-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
job_cards = soup.find_all("div", class_="card-content")

for card in job_cards:  # 'card' shu sikl ichida aniqlanadi
    title = card.find("h2", class_="title").text.strip()
    company = card.find("h3", class_="company").text.strip()
    location = card.find("p", class_="location").text.strip()

    # 'description' va 'application_link' bo‘sh bo‘lsa, muqobil matn qaytariladi
    description_tag = card.find("div", class_="description")
    description = description_tag.text.strip() if description_tag else "No description available"

    application_tag = card.find("a", class_="apply")
    application_link = application_tag['href'].strip() if application_tag else "No link available"

    print(title, company, location, description, application_link)  # Natijani ko‘rish uchun
