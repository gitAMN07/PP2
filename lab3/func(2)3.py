def movies_category():
    num_movies = int(input("Number of movies: "))
    movies = []

    for _ in range(num_movies):
        name = input("Name: ")
        imdb = float(input("IMDB score: "))
        category = input("Movie category: ").strip()
        movies.append({"name": name, "imdb": imdb, "category": category})

    search_category = input("\nEnter a category: ").strip().capitalize()
    
    filtered_movies = [movie for movie in movies if movie["category"].capitalize() == search_category]

    if filtered_movies:
        print(f"\nMovies in the '{search_category}' category:")
        for movie in filtered_movies:
            print(f"{movie['name']} - IMDB: {movie['imdb']}")
    else:
        print(f"No movies found in the '{search_category}' category.")

movies_category()

