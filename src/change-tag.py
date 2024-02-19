import json

# Open the JSON file in read mode and load its content
with open("my-articles.json", "r") as fp:
    data = json.load(fp)

# Modify the "tag" field as needed
for article in data["articles"]:
    if article.get("tag") == "Actor":
        article["tag"] = "Actors"

# Open the same JSON file in write mode and write the modified content back
with open("your_file.json", "w") as fp:
    json.dump(data, fp, indent=4)

# Print the modified JSON data
print(json.dumps(data, indent=4))
