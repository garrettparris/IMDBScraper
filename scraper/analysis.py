def stats(crewcast):
    
    topDirector = getDirector(crewcast[0])
    topWriter = []
    topProducer = []
    topMusician = []
    topCinema = []
    topEditor = []
    topCast = []

    return [topDirector, topWriter, topProducer, topMusician, topMusician, topCinema, topEditor, topCast]


def find_with_list(myList, target):
         inds = []
         for i in range(len(myList)):
             if myList[i][0] == target:
                 inds += i,
         return inds

def getDirector(directors):
    passed = []
    topDirector = []
    i = 0
    avgRatingAmnt = 0
    for name in directors:
        if name[0] not in passed:
            passed.append(name[0])
            topDirector.append([name[0],[],0,0.0])
            inds = find_with_list(directors, name[0])
            print(name[0])
            print(str(inds))
            for j in inds:
                print(str(j))
                #rating add
                topDirector[i][1].append(directors[j][1])
                topDirector[i][2] += int(directors[j][1])
            laplaceRating = laplaceSmoothing(topDirector[i])
            topDirector[i][3] = laplaceRating
            avgRatingAmnt += topDirector[i][2]
        else:
            continue
        i += 1
    avgRatingAmnt = avgRatingAmnt/len(directors)
    print('avg rating: ' + str(avgRatingAmnt))
    return sorted(topDirector, key=lambda x : x[3])







# research results in picking between
#     Wilson lower bound https://www.evanmiller.org/how-not-to-sort-by-average-rating.html

#     vs
    
#     Laplace Smoothing https: // planspace.org / 2014 / 0 8 / 17 / how - to - sort - by - average - rating /
    
#     I am picking laplace smoothing for readability and performance reasons.
#     Wilson is much more complex is provides diminishing returns regarding my product's data

def laplaceSmoothing(director):
    
    result = (director[2]+1)/(len(director[1])+2)
    return result