import requests
import frontmatter

# Fetch a random quote from the API
response = requests.get("https://api.quotable.io/random")
quote = response.json()["content"]

# Read the existing README.md file
with open("README.md", "r") as file:
    content = frontmatter.load(file)

# Update the README.md file with the random quote
content["quote"] = quote

# Write the updated content back to the README.md file
with open("README.md", "w") as file:
    frontmatter.dump(content, file)
