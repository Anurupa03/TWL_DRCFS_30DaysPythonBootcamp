# Go to weather website
# Get the current temp and weather for your local city 
# print the current temp and weather

# Hit the website with request module
# pasrse the html returned by requests module using bs4 module 
# Fetch the current temp and weather usinh html 
# print iy 

import requests
import bs4

def send_request(website_url:str) -> str:
    return requests.get(website_url).text

def parse_html_string(html_str:str) -> bs4.BeautifulSoup:
    return bs4.BeautifulSoup(html_str,'html.parser')

def fetch_current_nepali_date(parsed_html:bs4.BeautifulSoup)-> str:
    top_element = parsed_html.find(id="top")
    date_element = top_element.find('div',class_="date")
    current_date = date_element.span.string.removeprefix('\n')
    return current_date



def main():
    website = "https://www.hamropatro.com/"
    html_str = send_request(website)
    parse_html = parse_html_string(html_str)
    current_temp = fetch_current_nepali_date(parse_html)

    print(f'The current date is {current_temp} for today ')


if __name__ == '__main__':
    main()