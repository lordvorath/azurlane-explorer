from bs4 import BeautifulSoup
import re, os

def parse_list_of_ships_by_stats(source_file, destination_folder):
    with open(source_file, encoding="utf-8") as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    spans = soup.find_all('span', class_='mw-headline')
    for span in spans:
        the_div = span.parent.next_sibling.next_sibling
        for article in the_div.find_all('article'):
            match = re.search(re.compile(r"Level_\d+"), article['id'])
            if not match:
                continue
            level = match.group(0)
            table = article.find('table')
            headers = []
            for th in table.find_all('th'):
                if th.text:
                    headers.append(th.text)
                else:
                    headers.append(th.find('img')['alt'])
            data = []
            for tr in table.find_all('tr'):
                row = []
                for td in tr.find_all('td'):
                    row.append(td.text)
                data.append(row)
            if not os.path.isdir(destination_folder):
                os.makedirs(destination_folder)
            filename = f"{destination_folder}/{span.text}_{level}.csv"
            content = ",".join(headers)
            for row in data:
                content += ",".join(row) + '\n'
            with open(filename, 'wt',encoding="utf-8") as f:
                f.write(content)



parse_list_of_ships_by_stats(".\html_files\List_of_Ships_by_Stats.html",".\csv_files")