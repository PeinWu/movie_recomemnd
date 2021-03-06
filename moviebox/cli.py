import sys
import click

from .recommender import recommender
from .output import displayHelpMessage, displayVersion

movieboxVersion = '0.0.0'

@click.command(add_help_option=False)
@click.option('-m', '--movie', default=2874, help='Input movie ID')
@click.option(
    '-r',
    '--recommendations',
    default=3,
    help='Number of movie recommendations')
@click.option(
    '-p', '--plot', is_flag=True, default=False, help='Display movie plot')
@click.option(
    '-i',
    '--interactive',
    is_flag=True,
    default=False,
    help='Display progress info')
@click.option(
    '-v',
    '--version',
    is_flag=True,
    default=False,
    help='Display installed version')
@click.option(
    '-h', '--help', is_flag=True, default=False, help='Display help message')
@click.option(
    '-s', '--search', is_flag=True, default=False, help='Search movie by ID')


def main(movie, recommendations, plot, interactive, help, version,search):
    if (help):
        displayHelpMessage()
        sys.exit()

    else:
        if (version):
            displayVersion()
        else:
            recommender(
                movieID = movie,
                recommendationsNumber = recommendations,
                showPlots = plot,
                interactive=interactive
            )

if __name__=='__main__':
    mian()








