import imdb
ia = imdb.IMDb()
movie_name = input("Enter Any Movie Name :\t")
search = ia.search_movie(movie_name)
id = search[0].getID()
print("Movie ID:\t",id)
movie = ia.get_movie(id)
print(f"Name : {movie['title']}: {movie['year']}")
print(f"IMDB Ratings: {movie.get('rating')}",end=" ")
print("\U00002B50"*int(round(movie.get('rating'))/2))
print(f"Votes: {movie.get('votes')}")
for i in movie['director']:
    print("Director: ", i)
print("Casts",end=":")
for i in movie['cast']:
    print(f"{i}",end=",")
print(f"\n{movie.get('countries')[0]}")