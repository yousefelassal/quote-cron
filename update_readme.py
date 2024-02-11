import requests

# Fetch a random quote from api.quotable.io
response = requests.get("http://api.quotable.io/random")
quote_data = response.json()
quote = quote_data["content"]

# Update README.md with the new quote
with open("README.md", "a") as readme_file:
    readme_file.write("\n\n> " + quote)
