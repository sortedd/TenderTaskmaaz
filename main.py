import requests
import csv
from bs4 import BeautifulSoup

# URL to scrape
url = "https://etenders.gov.in/eprocure/app"

# Make a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find the table on the page
table = soup.find("table")

# Extract the rows from the table
rows = table.find_all("tr")

# Create a CSV file to store the data
with open("etenders.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write the header row to the CSV file
    writer.writerow(["Tender Title", "Tender Number", "Tender Date", "Due Date", "Organization Name"])

    # Loop through each row in the table
    for row in rows:
        # Extract the data from each cell
        cells = row.find_all("td")

        # If the row has 5 cells, then it's a valid row
        if len(cells) == 5:
            # Write the data to the CSV file
            writer.writerow([cell.text for cell in cells])
