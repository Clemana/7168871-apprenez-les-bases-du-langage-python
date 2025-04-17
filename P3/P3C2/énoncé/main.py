from bs4 import BeautifulSoup
with open("index.html", 'r') as file:
     soup = BeautifulSoup(file, 'html.parser')



