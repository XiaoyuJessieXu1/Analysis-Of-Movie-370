import json
import csv

# Load data from a JSON file
with open('articles.json', 'r') as file:
    data = json.load(file)

# Extract relevant data from JSON
articles = data.get("articles", [])
data_to_write = [
    (article.get("tag", ""), article.get("title", ""), article.get("description", ""))
    for article in articles
]

# Write data to a CSV file
with open("articles.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)  # No need to specify delimiter for CSV
    # Write header
    writer.writerow(["Topics", "Title", "Description"])
    # Write data
    writer.writerows(data_to_write)

print("CSV file 'articles.csv' has been created.")
