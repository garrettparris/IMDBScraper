import requests
from bs4 import BeautifulSoup
import time

start = time.time()


print('start')
page = requests.get('https://www.imdb.com/user/ur64640683/ratings')
nextPage=True
while (nextPage is not None):
        
    soup = BeautifulSoup(page.text, 'html.parser')
    movieCard = soup.find(class_='lister list detail sub-list')
    movieTitle = movieCard.find_all('a')

    for text in movieTitle:
        print(text)
    try:
        nextPage = soup.find(class_='flat-button lister-page-next next-page', href=True)
        page = requests.get('https://www.imdb.com/' + nextPage['href'])
    except:
        print('end of ratings.')

end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))