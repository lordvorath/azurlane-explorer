from bs4 import BeautifulSoup

def parse_list_of_ships_by_stats(file):
    with open(file) as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    tables = soup.find_all('table')
    print(tables)

