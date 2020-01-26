from bs4 import BeautifulSoup
with open("C:\\Users\\ASUS\\Desktop\\1234.html") as wb_data:
    Soup = BeautifulSoup(wb_data, 'html.parser')
    print(Soup)