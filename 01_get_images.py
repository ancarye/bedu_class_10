from bs4 import BeautifulSoup
import requests


url = 'https://realpython.com/tutorials/community/'

response = requests.get(url)
response_content = response.content

soup = BeautifulSoup(response_content, features = 'html.parser')

#<img src=------>

images = soup.find_all('img',class_='card-img-top')
for img in images:
    url_img = img['src']

    print(img['src'])

