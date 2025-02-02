def average_imdb():
    num_movies = int(input("Enter the number of movies: "))
    movies = []

    for _ in range(num_movies):
        name = input("Enter movie name: ")
        imdb = float(input("Enter IMDB score: "))
        category = input("Enter movie category: ").strip().capitalize()
        movies.append({"name": name, "imdb": imdb, "category": category})

    search = input("\nEnter a category to compute the average IMDB score: ").strip().capitalize()
    
    filtered_movies = [movie for movie in movies if movie["category"] == search]

    if not filtered_movies:
        print(f"No movies found in the '{search}' category. Cannot compute average IMDB score.")
        return

    average_score = sum(movie["imdb"] for movie in filtered_movies) / len(filtered_movies)
    
    print(f"\nThe average IMDB score for '{search}' movies is: {average_score:.2f}")

average_imdb()
