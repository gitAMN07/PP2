def average_imdb():
    num_movies = int(input("Number of movies: "))
    movies = []

    for _ in range(num_movies):
        name = input("Enter movie name: ")
        imdb = float(input("Enter IMDB score: "))
        category = input("Enter movie category: ").strip()
        movies.append({"name": name, "imdb": imdb, "category": category})

    if not movies:
        print("No movies entered. Cannot compute average IMDB score.")
        return
    
    average_score = sum(movie["imdb"] for movie in movies) / len(movies)
    
    print(f"\nThe average IMDB score of the entered movies is: {average_score:.2f}")

average_imdb()