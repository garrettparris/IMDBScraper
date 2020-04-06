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

    castcrew = [None,[],[],[],[],[],[]]

    # returns[
    #     0[director]
    #     1[writer]
    #     2[producer]
    #     3[musician]
    #     4[cinematographer]
    #     5[editor]
    #     6[cast]
    # ]





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
                    castcrew[6].append([castName, rating])
                except:
                    print('failed to get cast member')
            castParsed = True
            continue
        try:
            
            
            position = header[i].text.split(' ')[0]
            if (position in dictionary):
                #creating dataset from name and header information
                names = credits[j].findAll(class_='name')
                for person in names:
                    name = str(person.text)
                    if position == 'Directed':
                        castcrew[0] = [name[2:len(name)-2],rating]
                    elif position == 'Writing':
                        castcrew[1].append([name[2:len(name) - 2], rating])
                    elif position == 'Produced':
                        castcrew[2].append([name[2:len(name) - 2], rating])
                    elif position == 'Music':
                        castcrew[3].append([name[2:len(name) - 2], rating])
                    elif position == 'Cinematography':
                        castcrew[4].append([name[2:len(name) - 2], rating])
                    elif position == 'Film':
                        castcrew[5].append([name[2:len(name) - 2], rating])
            if (position == 'Casting'):
                break
        except:
            print('none')
        j+=1

    return castcrew
