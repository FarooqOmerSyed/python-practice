import httpx
from selectolax.parser import HTMLParser
from dataclasses import dataclass, asdict
import csv

@dataclass
class Product:
    title: str
    price: str

def get_html(page):
    url = f'https://www.amazon.in/s?k=mobiles&page={page}&crid=10VA4PCBG67T5&sprefix=mobile%2Caps%2C225'
    resp = httpx.get(url)
    return HTMLParser(resp.text)

def parse_products(html):
    products = html.css('div.s-main-slot div.s-result-item')

    results = []
    for item in products:
        title_elem = item.css_first('span.a-size-medium')
        price_elem = item.css_first('span.a-price-whole')
        if title_elem and price_elem:
            new_item = Product(
                title=title_elem.text(),
                price=price_elem.text()
            )
            results.append(asdict(new_item))
    return results

def to_csv(res):
    with open('amznmob.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'price'])
        writer.writeheader()
        writer.writerows(res)

def main():
    for x in range(1, 4):
        html = get_html(x)
        res = parse_products(html)
        to_csv(res)

if __name__ == '__main__':
    main()
