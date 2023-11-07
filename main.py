import requests

response = requests.get('https://api.quotable.io/random')
quote = response.json()['content']

with open('README.md', 'a') as f:
    f.write(f'\n> {quote}\n')
