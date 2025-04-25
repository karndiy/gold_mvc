import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

def xnowtime():
    dt = datetime.now()
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def save_to_json(data, filepath):
    with open(filepath, "w") as outfile:
        json.dump(data, outfile)


def scrape_gold_data(url='https://www.goldtraders.or.th/UpdatePriceList.aspx'):
    res = requests.get(url)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, 'html.parser')

    table = soup.find("table", {"id": "DetailPlace_MainGridView"})
    if table is None:
        return []

    data = []
    for idx, row in enumerate(table.findAll("tr")[1:]):
        columns = row.findAll("td")
        if len(columns) == 9:
            data.append({
                'asdate': columns[0].text.strip(),
                'nqy': columns[1].text.strip(),
                'blbuy': columns[2].text.strip(),
                'blsell': columns[3].text.strip(),
                'ombuy': columns[4].text.strip(),
                'omsell': columns[5].text.strip(),
                'goldspot': columns[6].text.strip(),
                'bahtusd': columns[7].text.strip(),
                'diff': columns[8].text.strip()
            })
    data.reverse()
    print(data)
    return data

def send_api():
     url = 'https://karndiy.pythonanywhere.com/cjson/goldjson-v2'
     res = requests.get(url)

def cjson_pythonanywhere():
    vdata = []
    url = 'https://karndiy.pythonanywhere.com/cjson/goldjson-v2'
    data = scrape_gold_data()
    vdata = data

    # Data to be sent in the POST request
    #data = {'key': 'value', 'another_key': 'another_value', 'v2': 'data2','time':gettime()}

    # Send a POST request to the Flask server
    response = requests.post(url, json=vdata )

    # Check the response from the server
    if response.status_code == 201:
        print('JSON file created successfully!')
    else:
        print('Error creating JSON file')
        print(response.json())  # Print the error message from the server, if any        
