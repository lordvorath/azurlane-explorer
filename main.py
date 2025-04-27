import urls, os, requests
from parser import *

html_files = "./html_files/"

def main():
    print("Hello from azurlane-explorer!")
    main_menu()
    


def get_html_page(base_url, path):
    existing_files = [f for f in os.listdir(html_files) if os.path.isfile(html_files + f)]
    if (f"{path}.html") in existing_files:
        overwrite = input(f"WARNING: {path}.html already exists. Overwrite? Y/N\n-> ")
        if overwrite.lower() == "n":
            return
    res = requests.get(base_url + path)
    with open(f"./html_files/{path}.html", "wt") as f:
        f.write(res.text)

def main_menu():
    user_choice = input("Select mode: Get data (G) - Explore data (X) - Exit (any)\n-> ")
    match user_choice.lower():
        case "g":
            get_data()
        case "x":
            explore_data()
        case _:
            print("exiting...")
            return

def list_data_sources():
    print("Available data sources:")
    for i in range(len(urls.list_of_urls)):
        print(f"{i}: {urls.list_of_urls[i]}")
    choice, url = get_data_source(urls.list_of_urls)
    return choice, url

def list_data_files():
    print("Available data files:")
    existing_files = [f for f in os.listdir(html_files) if os.path.isfile(html_files + f)]
    for i in range(len(existing_files)):
        print(f"{i}: {existing_files[i]}")
    choice, file = get_data_source(existing_files)
    return choice, html_files + file
    
def get_data_source(list_of_options):
    choice = input(f"Select data source: 0..{len(list_of_options) - 1} / 666 (all)\n-> ")
    choice = int(choice)
    if choice >= 0 and choice < len(list_of_options):
        return choice, list_of_options[choice]
    if choice == 666:
        return 0, "ALL"
    print("ERROR: Choice out of bounds")
    raise Exception("Invalid choice")

def download_data_file(url):
    print(f"Getting {url}")
    try:
        get_html_page(urls.azurlane_wiki, url)
    except Exception as e:
        print(f"encountered an error: {e}")

def get_data():
    _, url = list_data_sources()
    if url == "ALL":
        for u in urls.list_of_urls:
            download_data_file(u)
    else:
        download_data_file(url)

def explore_data():
    _, file = list_data_files()
    print(f"Exploring {file}")
    parse_list_of_ships_by_stats(file)
    

if __name__ == "__main__":
    main()
