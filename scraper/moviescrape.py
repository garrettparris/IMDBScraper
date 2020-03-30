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

def castCrew(movieurl,rating):

    print('start crew scrape')
    page = requests.get('https://www.imdb.com/title/' + movieurl + '/fullcredits')
    soup = BeautifulSoup(page.text, 'html.parser')

    maincontent = soup.find(class_='article listo')

    castcrew = []

    dictionary = ['Directed','Writing','Produced','Music','Cinematography','Film']
    #this finds behind the scenes cast
    credits = maincontent.findAll(class_='simpleTable simpleCreditsTable')
    header = maincontent.findAll(class_='dataHeaderWithBorder')
    j = 0
    castParsed = False
    for i in range(len(header)):
        if 'Cast' in str(header[i].text) and castParsed is False:
            #if its the header for class list, skip iteration
            castList = maincontent.find(class_="cast_list")
            castCards = castList.findAll('tr')
            for k in range(3):
                try:
                    castName = castCards[k + 1].find('a').find('img').get('alt')
                    castcrew.append(['Cast', castName, rating])
                except:
                    print('failed to get cast member')
            castParsed=True
        try:
            
            
            position = header[i].text.split(' ')[0]
            if (position in dictionary):
                #creating dataset from name and header information
                names = credits[j].findAll(class_='name')
                for person in names:
                    name = str(person.text)
                    castcrew.append([titleChange(position),name[2:len(name)-2],rating])
            if (position == 'Music'):
                break
        except:
            print('none')
        j+=1

    
    return castcrew
