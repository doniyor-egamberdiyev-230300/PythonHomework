import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Set up WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Navigate to the Demoblaze website
driver.get("https://www.demoblaze.com")

# Click on the "Laptops" section
laptops_section = driver.find_element(By.LINK_TEXT, "Laptops")
laptops_section.click()
time.sleep(3)  # Wait for the page to load

# List to store laptop data
laptop_data = []

while True:
    # Get all laptop elements on the page
    laptops = driver.find_elements(By.CLASS_NAME, "card")

    for laptop in laptops:
        try:
            name = laptop.find_element(By.CLASS_NAME, "card-title").text
            price = laptop.find_element(By.CLASS_NAME, "card-text").text.split("\n")[0]  # Extract price
            description = laptop.find_element(By.CLASS_NAME, "card-text").text.split("\n")[1]  # Extract description

            laptop_data.append({
                "name": name,
                "price": price,
                "description": description
            })
        except Exception as e:
            print(f"Error extracting data: {e}")

    # Try clicking the "Next" button to go to the next page
    try:
        next_button = driver.find_element(By.LINK_TEXT, "Next")
        next_button.click()
        time.sleep(3)  # Wait for the next page to load
    except:
        print("No more pages available.")
        break  # Exit loop when there are no more pages

# Save data to a JSON file
with open("laptops.json", "w", encoding="utf-8") as file:
    json.dump(laptop_data, file, indent=4, ensure_ascii=False)

print("Scraping complete. Data saved to laptops.json.")

# Close the browser
driver.quit()
