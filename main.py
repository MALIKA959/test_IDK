from bs4 import BeautifulSoup as  BS
import requests


def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def get_data(html):
    soup = BS(html, 'html.parser')
    container = soup.find('div', class_= 'container body-container')
    main = container.find('div', class_ = 'main-content')
    wrapper = main.find('div', class_ = 'listings-wrapper')
    post = wrapper.find_all('div',class_ = 'listing')
    for i in post:
        left_side = i.find('div', class_ = 'left-side')
        title = left_side.find('p', class_ = 'title')
        address = left_side.find('div', class_ = 'address')
        link = left_side.find('a').get('href')
        full_link = f'https://www.house.kg{link}'
        right_side = i.find('div', class_ = 'right-side')
        dollar = right_side.find('div', class_ = 'price')
        som = right_side.find('div', class_ = 'price-addition')
        # print(dollar.text.strip())
        # print(f'{som.text.strip()} - {dollar.text.strip()}')
        span = i.find('span', class_='dealer-name')
        desc = i.find('div', class_ = 'description')
        # print(f'Название: {desc.text.strip()}')
        info = i.find('div', class_ = 'additional-info').find('div', class_ = 'left-side')
        view = info.find('span', {"data-placement":"top"}).text.strip()
        
        
        # print(info.text.strip())
        
        # if span == None:
        #     print('Нет агенства недвижимости')
        # else:
        #     print(span.text.strip())
        # print(full_link)
        # print(title.text.strip())
        # print(address.text.strip())

def main():
    URL = 'https://www.house.kg/kupit-uchastok?region=1&town=2&sort_by=upped_at+desc'
    html = get_html(URL)
    get_data(html)
    
    
if __name__ == '__main__':
    main() 