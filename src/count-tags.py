import csv
import json

with open('articles.json', 'r') as file:
    data = json.load(file)
count = 0
tag = "Unrelated"
# Iterate through the articles and count those with the specified tag
for article in data["articles"]:
    if article.get("tag") == tag:
        count += 1

# Print the count of articles with the "Financial Performance" tag
print("Number of articles with tag" + " "+ tag + "=", count)
#22
#18
#15
#18
#10
#19
#13
#10