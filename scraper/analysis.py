
# crewcast = [
#     0[director]
#     1[writer]
#     2[producer]
#     3[musician]
#     4[cinematographer]
#     5[editor]
#     6[cast]
# ]
def stats(crewcast):


    topDirector = getDirector(crewcast[0])
    topWriter = getWriter(crewcast[1])
    topProducer = getWriter(crewcast[2])
    topMusician = getWriter(crewcast[3])
    topCinema = getWriter(crewcast[4])
    topEditor = getWriter(crewcast[5])
    topCast = getWriter(crewcast[6])

    return [topDirector, topWriter, topProducer, topMusician, topCinema,topEditor, topCast]


def find_with_list_directors(myList, target):
         inds = []
         for i in range(len(myList)):
             if myList[i][0] == target:
                 inds += i,
         return inds

def find_with_list(myList, target):
         inds = []
         for i in range(len(myList)):
             for j in range(len(myList[i])):
                if myList[i][j][0] == target:
                    inds.append([i,j])
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
            inds = find_with_list_directors(directors, name[0])
            for j in inds:
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
    return sorted(topDirector, key=lambda x : x[3])[::-1][:5]


def getWriter(writers):
    passed = []
    topWriter = []
    i = 0
    for movie in writers:
        if movie is None:
            continue
        for writer in movie:
            name = writer[0]
            if name not in passed:
                topWriter.append([name,[],0,0.0])
                passed.append(name)
                inds = find_with_list(writers, name) #returns [i,j] index
                for j in inds:
                    rating = int(writers[j[0]][j[1]][1])
                    topWriter[i][1].append(rating)
                    topWriter[i][2] += int(rating)
                laplaceRating = laplaceSmoothing(topWriter[i])
                topWriter[i][3] = laplaceRating
            else:
                continue
            i += 1
    return sorted(topWriter, key=lambda x : x[3])[::-1][:5]


# research results in picking between
#     Wilson lower bound https://www.evanmiller.org/how-not-to-sort-by-average-rating.html

#     vs
    
#     Laplace Smoothing https: // planspace.org / 2014 / 0 8 / 17 / how - to - sort - by - average - rating /
    
#     I am picking laplace smoothing for readability and performance reasons.
#     Wilson is much more complex is provides diminishing returns regarding my product's data

def laplaceSmoothing(director):
    
    result = (director[2]+1)/(len(director[1])+2)
    return result