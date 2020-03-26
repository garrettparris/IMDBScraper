import moviescrape
import ratingscrape
import time

def main():
    start = time.time()
    ratinglist = ratingscrape.getRatings('ur80333814')
    print('--- ratings retrieved ---')
    print('--- gathering cast & crew info ---')
    for item in ratinglist:
        crew = moviescrape.crew(item[1],item[2])
    end = time.time()
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))
    return

if __name__ == '__main__':
    main()