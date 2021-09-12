Genre_answer = ["Horror", "horror", "HORROR", "Sci-fi", "sci-fi", "SCI-FI", "sci fi", "Sci fi", "SCI FI", "Comedy", "comedy", "COMEDY", "Thriller", "thriller", "THRILLER", "Drama", "drama", "DRAMA", "Fantasy", "fantasy", "FANTASY", "Action", "action", "ACTION", "Crime", "crime", "CRIME"]
Genre_list = ["Horror", "Sci-fi", "Comedy", "Thriller", "Drama", "Fantasy", "Action", "Crime"]
print(Genre_list)
Genre_fun = input("Pick a genre")
if Genre_fun in Genre_answer:
    print("your data stored")
else:
    print("pick a genre in the list")
