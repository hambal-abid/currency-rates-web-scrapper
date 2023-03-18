import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the product page to scrape
url = "https://www.forex.com.pk/"

# Send a GET request to the URL
response = requests.get(url)

if response.status_code == 200:

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    date_element = soup.find('td', {'class':'heading'}).find_next('p').find_next('span').find_next('br')
    date = date_element.text.strip()

    table = soup.find('table',{'cellspacing':4,'cellpadding':2})
    
    df = pd.DataFrame(columns=['Currency', 'Buying', 'Selling'])

    for row in table.find_all('tr'):
        columns = row.find_all('td')

        if(columns != []):
            try:
                curreny = columns[0].text.strip()
                if curreny == 'Currency':
                    pass
                buying = columns[1].text.strip()
                selling = columns[2].text.strip()

                df = pd.concat([df, pd.DataFrame.from_records([{'Currency':curreny,'Buying':buying,'Selling':selling}])])
            except:
                pass

    # # Print the product information
    print(date)
    print(df.to_string(index=False,header=False))
