import requests
from bs4 import BeautifulSoup

URL = 'http://lagniappebrasserie.com/menu/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

try:
    page = requests.get(URL, headers=headers)
    page.raise_for_status()
    soup = BeautifulSoup(page.content, 'html.parser')

    items = soup.find_all('strong')
    menu=[]
    for item in items:
        menu.append(item.string)

    #Print Out Data
    for drink_category in menu:
        print(drink_category)

except requests.exceptions.HTTPError as http_err:
    # Handle HTTP errors (e.g., 404, 503, etc.)
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    # Handle connection errors (e.g., DNS failure, refused connection, etc.)
    print(f"Connection error occurred: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    # Handle request timeout
    print(f"Timeout error occurred: {timeout_err}")
except requests.exceptions.RequestException as req_err:
    # Handle any other request-related errors
    print(f"An error occurred during the request: {req_err}")
except Exception as e:
    # Handle other exceptions (non-request related)
    print(f"An error occurred: {e}")