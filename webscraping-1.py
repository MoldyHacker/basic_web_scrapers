import requests
from bs4 import BeautifulSoup

URL = 'http://lagniappebrasserie.com/liquor-cordials/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

try:
    page = requests.get(URL, headers=headers)
    page.raise_for_status()

    soup = BeautifulSoup(page.content, 'html.parser')
    groups = soup.find_all('span', class_='collapseomatic')

    #List types
    list_types = []
    for categories in groups:
        line = ""
        for text in categories.strings:
            line += text
        list_types.append(line)
    #List all drinks
    list_drinks = []
    drinks = soup.find_all('ul')
    for drink_type in drinks:
        #The menu has a class the drinks do not
        if not drink_type.has_attr("class"):
            #List for each category
            list_categories = []
            list_categories.append(list_types.pop())
            #List for each drink to be in the category list
            choices = []
            each_drink = drink_type.find_all('li')
            for a_drink in each_drink:
                line = ""
                for text in a_drink.strings:
                    line += text
                decimal_position = len(line) - 2
                line = line[0:decimal_position] + "." + line[decimal_position:]
                choices.append(line)
            list_categories.append(choices)
            list_drinks.append(list_categories)

    #Print Out Data
    for drink_category in list_drinks:
        print("** {} **".format(drink_category[0]))
        for each_drink in drink_category[1]:
            print(each_drink)
        print()

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