import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.screener.in/company/compare/00000005/?limit=50&page=1'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the "Piotroski score" column header
    piotroski_score_header_element = soup.select_one('th[data-tooltip="Piotroski score"]')

    if piotroski_score_header_element:
        # If the element is found, extract its text
        piotroski_score_header = piotroski_score_header_element.text.strip()

        # Find all the "Piotroski score" data in the table
        piotroski_scores = [data.text.strip() for data in soup.select('td[data-tooltip="Piotroski score"]')]

        # Combine header and data into a list of lists
        table_data = [piotroski_score_header] + piotroski_scores

        # Write the data to a CSV file
        with open('piotroski_score_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(zip(table_data))

        print("CSV file 'piotroski_score_data.csv' has been created with the extracted Piotroski scores.")
    else:
        print("No 'Piotroski score' column header found in the table.")

else:
    print("Failed to retrieve the page. Status code:", response.status_code)
