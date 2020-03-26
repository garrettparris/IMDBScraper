import requests
from bs4 import BeautifulSoup
import time

def parseDate(date):
    return date[9:]


def getRatings(userurl):


    print('start')
    page = requests.get('https://www.imdb.com/user/ur80333814/ratings')
    soup = BeautifulSoup(page.text, 'html.parser')

    nextPage = True
    i = 0
    userinfo = []
    while (nextPage is not None):
            
        movieList = soup.find(class_='lister list detail sub-list')
        movieTitle = movieList.find_all(class_='lister-item mode-detail')
        for card in movieTitle:
            movieinfo = []
            #find the unique imdb movie id
            movieurl = card.find(class_='lister-item-image ribbonize').get('data-tconst')
            #retrieve the imdb movie title
            header = card.find(class_='lister-item-header')
            #retrieve the star rating of movie
            rating = card.find(class_='ipl-rating-star ipl-rating-star--other-user small').find(class_='ipl-rating-star__rating').text
            #retrieve date rated
            date = parseDate(card.findAll('p')[1].text)
            
            movieinfo.append(header.find('a').text)
            movieinfo.append(movieurl)
            movieinfo.append(str(rating))
            movieinfo.append(date)
            userinfo.append(movieinfo)
        
        i = i + 1
        try:
            nextPage = soup.find(class_='flat-button lister-page-next next-page', href=True)
            page = requests.get('https://www.imdb.com/' + nextPage['href'])
            soup = BeautifulSoup(page.text, 'html.parser')
        except:
            print('end of ratings.')

    
    return userinfo


