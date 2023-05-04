import sys
import spacy

nlp = spacy.load('en_core_web_md')

movies_file = open(sys.path[0] + '/movies.txt')
movies = movies_file.read().strip().split('\n')
movies_file.close()

watched_movie = input("Please enter the description of a movie you enjoyed recently: \n")

def similiar_movie(description):
    similiar_movie = ''
    similiar_score = 0

    for movie in movies:
        similarity = nlp(movie).similarity(nlp(description))

        if similarity > similiar_score:
            similiar_score = similarity
            similiar_movie = movie

    return similiar_movie

print(similiar_movie(watched_movie))