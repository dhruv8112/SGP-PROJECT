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

    # Specify the path to the table using the select method
    table_path = "html > body > main > div:nth-of-type(2) > div:nth-of-type(3)"

    # Find the table based on the specified path
    table = soup.select(table_path)

    if table:
        # Extract data from the "Piotroski score" column and write it to a CSV file
        with open('piotroski_score_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Extract column header for "Piotroski score"
            piotroski_score_header = table[0].select_one('th[data-tooltip="Piotroski score"]').text.strip()
            csv_writer.writerow([piotroski_score_header])

            # Extract data from the "Piotroski score" column
            piotroski_scores = [data.text.strip() for data in table[0].select('td[data-tooltip="Piotroski score"]')]
            csv_writer.writerows(zip(piotroski_scores))

        print("CSV file 'piotroski_score_data.csv' has been created with the extracted Piotroski scores.")

    else:
        print("Table not found at the specified path:", table_path)

else:
    print("Failed to retrieve the page. Status code:", response.status_code)
