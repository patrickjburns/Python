#Simran Singh and Patrick Burns

import csv
from string import lower

def create_actors_DB(actor_file):
    '''Create a dictionary keyed on actors from a text file'''
    f = open(actor_file)
    movieInfo = {}
    for line in f:
        line = line.rstrip().lstrip()
        actorAndMovies = line.split(',')
        actor = actorAndMovies[0]
        movies = [x.lstrip().rstrip() for x in actorAndMovies[1:]]
        movieInfo[actor] = set(movies)
    f.close()
    return movieInfo

def create_ratings_DB(ratings_file):
    '''make a dictionary from the rotten tomatoes csv file'''
    scores_dict = {}
    with open(ratings_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            scores_dict[row[0]] = [row[1], row[2]]
    return scores_dict

def insert_actor_info(actor, movies, movie_Db):
    '''checks if movie is in movies_Db; if not, adds; if there, updates dict.'''
    if actor not in movie_Db:
        movie_Db[actor]=movies
    else:
        for movie in movies:
            if movie not in movie_Db[actor]:
                movie_Db[actor].add(movie)

def insert_rating(movie, ratings, ratings_Db):
    '''checks if movie is in ratings_Db; if not, adds; if there, updates dict.'''
    ratings = list(ratings)
    if movie not in ratings_Db:
        ratings_Db[movie]=ratings
    else:
        if ratings not in ratings_Db(movie):
            ratings_Db[movie].replace(ratings)
   
def removekey(d, key):
    '''removes a certain key from a given dictionary'''
    r = d.copy()
    del r[key]
    return r

import operator
    
def get_operator_fn(op):
    '''change a string into a mathematical operator'''
    return {
        '=' : operator.eq,
        '>' : operator.gt,
        '<' : operator.lt,
        '/' : operator.div,
        '%' : operator.mod,
        '^' : operator.xor,
        }[op]

def delete_movie(movie, movie_Db, ratings_Db):
    '''delete the movie from the movie DB and ratings DB'''
    for key in ratings_Db:
        if key == movie:
            ratings_Db = removekey(ratings_Db, key)
            
    for key in movie_Db:
        if movie in movie_Db[key]:
            x =list(movie_Db[key])
            x.remove(movie)
            movie_Db[key]=x
    return movie_Db, ratings_Db

def select_where_actor_is(actorName,movie_Db):
    '''return all movies for a certain actor'''
    l = movie_Db[actorName]
    return l

def select_where_movie_is(movieName,movie_Db):
    '''return all actors for a certain movie'''
    l =[]
    for key in movie_Db:
        if movieName in movie_Db[key]:
            l.append(key)
    return l

def select_where_rating_is(targeted_rating,comparison,is_critic,ratings_Db):
    '''all movies which satisfy certain criteria based on critics rating or audience rating'''
    l =[]
    b = get_operator_fn(comparison)
    
    for key in ratings_Db:
        a = ratings_Db[key]
        if is_critic == True:
            if b(int(a[0]),targeted_rating)== True:
                l.append(key)
        else:
            if b((int(a[1])),targeted_rating)==True:
                l.append(key)
    return l

def get_co_actors(actorName,moviedb):
    '''get the names of the actors who have costarred in a film with the given actor'''
    l = moviedb[actorName]
    coactors =[]
    for movies in l:
        for actors in moviedb:
            theirmovies = moviedb[actors]
            if movies in theirmovies and actors != actorName:
                coactors.append(actors)
    return coactors

def get_common_movie(actor1, actor2, moviedb):
    '''get the names of the movies common between the two given actors'''
    l1 = moviedb[actor1]
    l2 = moviedb[actor2]
    common = []
    for movies in l1:
        if movies in l2:
            common.append(movies)
    return common
    
def critics_darling(movie_Db,ratings_Db):
    '''actor with the highest critic rating'''
    finalrating={}
    for actors in movie_Db:
        totalrating=0
        movies = movie_Db[actors]
       
        for x in movies:
            if x in ratings_Db:
                    abc = list(ratings_Db[x])
                    rating = int(abc[0])
                    totalrating += rating
        averagerating = totalrating/len(movies)
        finalrating[actors] = averagerating
    sorted_x = sorted(finalrating.items(), key=operator.itemgetter(0))
    return sorted_x[0:5]

def audience_darling(movie_Db,ratings_Db):
    '''actor with the highest audience rating'''
    finalrating={}
    for actors in movie_Db:
        totalrating=0
        movies = movie_Db[actors]
        for x in movies:
            if x in ratings_Db:
                abc = list(ratings_Db[x])
                rating = int(abc[1])
                totalrating += rating
        averagerating = totalrating/len(movies)
        finalrating[actors] = averagerating
    sorted_x = sorted(finalrating.items(), key=operator.itemgetter(0))
    return sorted_x[0:5]

def good_movies(ratings_Db):
    '''returns a set of movies that are rated higher than 85 by critic and audience'''
    critic =(select_where_rating_is(85,">",True,ratings_Db))
    audience =(select_where_rating_is(85,">",False,ratings_Db))
    set=(critic, audience)
    return set

def main():
    
    actor_DB = create_actors_DB('movies.txt')
    ratings_DB = create_ratings_DB('moviescores.csv')

    print """Welcome to the movie database, the best source for info on actors and movies! \n
        Enter 1 to add the info for an actor to the database.
        Enter 2 to update a movie's rating in the database.
        Enter 3 to delete information about a movie from the database.
        Enter 4 to see all the movies for a certain actor.
        Enter 5 to see all the actors in a certain movie.
        Enter 6 to see a list of movies based on its ratings.
        Enter 7 to see all the actors an actor has worked with.
        Enter 8 to enter two actors and see the movies both were in.
        Enter 9 to see the movies that have the highest critic ratings.
        Enter 10 to see the movies that have the highest audience ratings.
        Enter 11 to see the movies both critics and audience have rated highly. \n """

    answer = raw_input("what would you like to do? ")      
    
    if answer == "1":
        actor = raw_input("Write an actor's name to find the actor's movies? ")
        movies = raw_input("Write the movies the actor was in ") 
        insert_actor_info(actor, movies, actor_DB)
    if answer == "2":
        movie = raw_input("What movie do you want to update? ")
        ratings = raw_input("What ratings did the movie get (critics rating, audience rating)? ")
        insert_rating(movie, ratings, ratings_DB)
    if answer == "3":
        movie = raw_input("What movie do you want to delete? ")
        delete_movie(movie, actor_DB, ratings_DB)
    if answer == "4":
        actorName = raw_input("Enter an actor name to see all his/her movies ")
        print select_where_actor_is(actorName, actor_DB)
    if answer == "5":
        movieName = raw_input("Enter a movie to see all the actors in it. ")
        print select_where_movie_is(movieName, actor_DB)    
    if answer == "6":
        targeted_rating = raw_input("Enter the rating for a movie ")
        comparison = raw_input("Would you like to see movies that are =, >, or < that rating? ")
        is_critic = raw_input("Would you to see movies with critics? (Y/N) ")
        if is_critic == "Y":
            is_critic = True
        else: is_critic = False
        print select_where_rating_is(int(targeted_rating),comparison,is_critic,ratings_DB)
    if answer == "7":
        actorName = raw_input("Enter the name of an actor to see the actors he/she has worked with ")
        print get_co_actors(actorName,actor_DB)
    if answer == "8":
        actor1 = raw_input("Enter the name of the first actor ")
        actor2 = raw_input("Enter the name of the second actor ")
        print get_common_movie(actor1, actor2, actor_DB)
    if answer == "9":
        print critics_darling(actor_DB,ratings_DB)
    if answer == "10":
        print audience_darling(actor_DB,ratings_DB)
    if answer == "11":
        print good_movies(ratings_DB)

if __name__ == '__main__':
    main()
