import time
import pandas as pd

from .output import printGreen
from os.path import join, dirname

parentPath = dirname(__file__)
MovieCsvPath = join(parentPath,'dataset/movies.csv')

def importData(verbose):
    start = time.time()
    # import movie dataset
    movieDF = pd.read_csv(MovieCsvPath)
    if(verbose):
        printGreen('Imported Data \t\t {.1f}s'.format(time.time()-start))
    # Return the imported datasets
    return movieDF

def splitData(movieDF,verbose):
    start = time.time()
    # get the movie title
    titles = movieDF[['Title']].values.flatten.tolist()
    # get the movie category
    categories = movieDF[['categories']].values.flatten.tolist()
    # Get the movie plot summaries
    plots = movieDF[['Plot']].values.flatten.tolist()
    if(verbose):
        printGreen('Split data\t\t {.1f}s'.format(time.time()-start))
    # Pack and return the split data
    return {'titles':titles,'categories':categories,'plots':plots}

