from .data import importData, splitData
from .tfidf import trainEngine, getSimilarities
from .output import printYellow, printGreen, prettyPrint, validateInput

green = 'green'
yellow = 'yellow'

def recommender(movieID,recommendationsNumber, showPlots, interactive):
    validateInput(movieID,recommendationsNumber)
    data = importData(interactive)
    dataset = splitData(data,interactive)
    # train the recommendations engine
    results = trainEngine(dataset['[plots'],interactive)
    # generate recommendations
    recomendedMovies = getSimilarities(movieID,recommendationsNumber,results,interactive)

    # input movie
    # Input movie
    printGreen('❯ Given Movie')
    prettyPrint(
        movieID=movieID,
        title=dataset['titles'][movieID],
        category=dataset['categories'][movieID],
        plot=dataset['plots'][movieID],
        color=green,
        showPlots=showPlots)
    # Display the recommended movies
    printYellow('★ Top ' + str(recommendationsNumber) + ' Recommendations')
    for i in recomendedMovies:
        prettyPrint(
            movieID=i,
            title=dataset['titles'][i],
            category=dataset['categories'][i],
            plot=dataset['plots'][i],
            color=yellow,
            showPlots=showPlots)
    return 0
