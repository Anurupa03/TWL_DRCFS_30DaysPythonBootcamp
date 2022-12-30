# goto daraz site for a specific product
# fetch its current price
# write price to a file every 10 seconds

# request daraz product page using requests module
# parse the html string using bs4
# find the element that contains the price
# convert price to integer
# write the price in a file

import requests
import bs4
import time 

def request_site(url:str)-> str:
    return requests.get(url, timeout=100).text

def parse_html_site(unparserd_html: str)-> bs4.BeautifulSoup:
    return bs4.BeautifulSoup(unparserd_html,"html.parser")

def fetch_price_form_soup(parsed_html:bs4.BeautifulSoup)-> str:
    price_element = parsed_html.find('span', class_="price-wrapper")
    nepali_price = price_element.span.string
    return nepali_price


def write_price_to_file(price:str,filename:str,time:str)-> None:
    with open(filename,'a',encoding='utf-8') as file:
        file.write(",".join((price,time)))
        file.write('\n')

def main():
    
    site = "https://www.sastodeal.com/baltra-sensible-plus-electric-2-burner-infrared-cooker-bic-126-supply-baltra-09.html"
    filePath = "data.txt"
    time_now = time.asctime(time.localtime(time.time()))
    html_str = request_site(site)
    soup = parse_html_site(html_str)
    price = fetch_price_form_soup(soup)
    write_price_to_file(price,filePath,time_now)

if __name__ == '__main__':
    main()