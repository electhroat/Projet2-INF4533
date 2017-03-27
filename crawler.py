import requests #request information from a webpage
#video sur youtube sur comment écrire un webcrawler en python
from bs4 import BeautifulSoup #module that lets you sort through data(permet de rassembler des elements)

#core spider

def spectacles_gatineau(max_pages):
    page = 1; #nombre de pages a parcourir
    while page <= max_pages:
        #build a basic URL
        url = " http://www.gatineau.ca/portail/default.aspx?p=quoi_faire/spectacles_theatre"
        source_code = request.get(url)
        plain_text = source_code.text
        #création d'un objet BeautifulSoup
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll("a", {'class','main_section_title'}):
            href = link.get('href')
            title = link.string #string présente dans la balise
            #print(title)
            #print(href)
            get_single_item_data(href)

def get_single_item_data(href): #prendre de l'information sur les liens eux-mêmes, aka le prix des billets
    souce_code = request.get(href)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('p', {'style', 'float'}):
        print(item_name.string)



spectacles_gatineau(1)
#ing
