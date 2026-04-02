current_movies={}
current_movies["The Godfather"] = "9 a.m."
current_movies["The Dark Knight"] = "9:30 a.m."
current_movies["Shine"] = "10 a.m."
current_movies["The Matrix"] = "11 a.m."

print("We currently showing following moviews:\n")
for key in current_movies:
    print(key)
moview=input("What moview would you like to watch?\n")
showtime=current_movies.get(moview)
# showtime=current_movies[moview]
if showtime==None:
    print("Requested moview is not available")
else:
    print(moview+" is playing at "+showtime)