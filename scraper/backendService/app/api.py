from flask import Flask
from flask import request
from flask_celery import make_celery
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0'
)
celery = make_celery(app)


@app.route("/task/<userurl>")
def task(userurl):
    
    print(userurl)
    job = getRatings.delay(userurl)
    print('hello')
    return 'task recieved ' 

@celery.task()
def getRatings(userurl):


    print('start')
    page = requests.get('https://www.imdb.com/user/' + userurl + '/ratings')
    soup = BeautifulSoup(page.text, 'html.parser')

    nextPage = True
    i = 0
    userinfo = []
    j = 0
    while (nextPage is not None):
        movieList = soup.find(class_='lister list detail sub-list')
        movieTitle = movieList.find_all(class_='lister-item mode-detail')
        for card in movieTitle:
            print(j)
            movieinfo = []
            #find the unique imdb movie id
            movieurl = card.find(class_='lister-item-image ribbonize').get('data-tconst')
            #retrieve the imdb movie title
            header = card.find(class_='lister-item-header')
            #retrieve the star rating of movie
            rating = card.find(class_='ipl-rating-star ipl-rating-star--other-user small').find(class_='ipl-rating-star__rating').text
            #retrieve date rated
            date = card.findAll('p')[1].text[9:]
            
            # movieinfo = [
            #     0 title
            #     1 movieurl
            #     2 rating
            #     3 date
            # ]


            movieinfo.append(header.find('a').text)
            movieinfo.append(movieurl)
            movieinfo.append(str(rating))
            movieinfo.append(date)
            userinfo.append(movieinfo)
            j = j + 1
        i = i + 1
        try:
            nextPage = soup.find(class_='flat-button lister-page-next next-page', href=True)
            page = requests.get('https://www.imdb.com/' + nextPage['href'])
            soup = BeautifulSoup(page.text, 'html.parser')
        except:
            print('end of ratings.')

    
    return i



if __name__ == "__main__":
    app.run()