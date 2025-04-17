import requests
from bs4 import BeautifulSoup

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
