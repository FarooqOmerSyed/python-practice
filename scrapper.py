import httpx
from selectolax.parser import HTMLParser
from dataclasses import dataclass, asdict
import csv

@dataclass
class Product:
    manufacturer: str
    title: str
    price: str

def get_html(page):
    url = f"https://www.thomann.co.uk/all-products-from-the-category-electric-guitars.html?ls=25&pg={page}"
    resp = httpx.get(url)
    return HTMLParser(resp.text)

def parse_products(html):
    products = html.css("div.product")

    results = []
    for item in products:
        new_item = Product(
            manufacturer=item.css_first('span.title__manufacturer').text(),
            title=item.css_first('span.title__name').text(),
            price=item.css_first('span.product__price-primary').text().strip()
        )
        results.append(asdict(new_item))
    return results

def to_csv(res):
    with open('ecomscrap.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['manufacturer', 'title', 'price'])
        writer.writeheader()  # Add this line to write headers
        writer.writerows(res)

def main():
    for x in range(1, 5):
        html = get_html(x)
        print(html.css_first('title').text())
        res = parse_products(html)
        to_csv(res)

if __name__ == '__main__':
    main()
