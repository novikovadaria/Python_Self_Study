from bs4 import BeautifulSoup
import requests
url = 'https://stackoverflow.com/questions'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
questions = soup.select('.question-summary')

