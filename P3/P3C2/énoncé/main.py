from bs4 import BeautifulSoup
with open("index.html", 'r') as file:
     soup = BeautifulSoup(file, 'html.parser')

title = soup.title.string
print("Titre de la page :", title)


