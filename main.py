import bs4
import requests

url = 'https://www.bukalapak.com/products?from=omnisearch&from_keyword_history=false&search%5Bkeywords%5D=terlaris&search_source=omnisearch_category&source=navbar'

contents = requests.get(url)
# print(contents.text)

response = bs4.BeautifulSoup(contents.text, "html.parser")
# print(response)
data = response.find_all('div', 'bl-flex-container flex-wrap is-gutter-16')
print(data[0].text)