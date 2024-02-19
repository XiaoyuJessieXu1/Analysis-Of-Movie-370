import json


with open('filtered_articles.json', 'r') as file:
    data = json.load(file)

unique_titles = []
filtered_articles = []

for article in data["articles"]:
    title = article["title"]
    if title not in unique_titles:
        unique_titles.append(title)
        filtered_articles.append(article)

# Update the JSON data with filtered articles
data["articles"] = filtered_articles

# Save the filtered data as JSON or perform further actions
with open("articles.json", "w") as outfile:
    json.dump(data, outfile, indent=4)

print("Filtered articles saved")
