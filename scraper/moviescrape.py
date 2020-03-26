import requests
from bs4 import BeautifulSoup
import time

def titleChange(role):
    switcher = {
        'Directed': 'Director',
        'Writing': 'Writer',
        'Produced': 'Producer',
        'Music': 'Musician',
        'Cinematography': 'Cinematographer',
        'Film': 'Film Editor',
    }
    return switcher.get(role)

def crew(movieurl,rating):

    print('start moviescrape')
    page = requests.get('https://www.imdb.com/title/' + movieurl + '/fullcredits')
    soup = BeautifulSoup(page.text, 'html.parser')

    maincontent = soup.find(class_='article listo')

    crew = []

    dictionary = ['Directed','Writing','Produced','Music','Cinematography','Film']
    #this finds behind the scenes cast
    credits = maincontent.findAll(class_='simpleTable simpleCreditsTable')
    header = maincontent.findAll(class_='dataHeaderWithBorder')
    j = 0
    for i in range(len(header)):
        if 'Cast' in str(header[i].text):
            #if its the header for class list, skip iteration
            continue
        try:
            
            
            position = header[i].text.split(' ')[0]
            if (position in dictionary):
                #creating dataset from name and header information
                names = credits[j].findAll(class_='name')
                for person in names:
                    name = str(person.text)
                    crew.append([titleChange(position),name[2:len(name)-2],rating])
            if (position == 'Music'):
                break
        except:
            print('none')
        j+=1

    
    return crew
