import moviescrape
import ratingscrape
import time
import analysis
def main():
    start = time.time()
    ratinglist = ratingscrape.getRatings('ur68950140')
    print('--- ratings retrieved ---')
    print('--- gathering cast & crew info ---')
    # results = [
    #     0[director]
    #     1[writer]
    #     2[producer]
    #     3[musician]
    #     4[cinematographer]
    #     5[editor]
    #     6[cast]
    # ]

    results = [[], [], [], [], [], [], []]
    index = 0
    dates = []
    for item in ratinglist:
        dates.append(item[3])
        index += 1
        print(index)
        castcrew = moviescrape.castCrew(item[1], item[2])
        if castcrew[0] is not None: results[0].append(castcrew[0])
        if castcrew[1] is not None: results[1].append(castcrew[1])
        if castcrew[2] is not None: results[2].append(castcrew[2])
        if castcrew[3] is not None: results[3].append(castcrew[3])
        if castcrew[4] is not None: results[4].append(castcrew[4])
        if castcrew[5] is not None: results[5].append(castcrew[5])
        if castcrew[6] is not None: results[6].append(castcrew[6])
    # print(results)
    end = time.time()
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    d = 0
    topcastcrew = analysis.stats(results)

    print('top directors: ' + str(topcastcrew[0]))
    print(' ')
    print('top writers: ' + str(topcastcrew[1]))
    print(' ')
    print('top producers: ' + str(topcastcrew[2]))
    print(' ')
    print('top musicians: ' + str(topcastcrew[3]))
    print(' ')
    print('top cinematographers: ' + str(topcastcrew[4]))
    print(' ')
    print('top editors: ' + str(topcastcrew[5]))
    print(' ')
    print('top cast: ' + str(topcastcrew[6]))
    print(' ')
    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))
    
    return

if __name__ == '__main__':
    main()