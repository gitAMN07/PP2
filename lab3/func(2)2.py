def high_rated():
    movies = []
    
    n = int(input("Number of movies: "))
    
    for _ in range(n):
        name = input("Movie name: ")
        try:
            imdb_score = float(input("IMDB score: "))
            movies.append({"name": name, "imdb": imdb_score})
        except ValueError:
            print("Invalid IMDB")
            return

    high_rated = [movie for movie in movies if movie["imdb"] > 5.5]

    if high_rated:
        print("\nMovies with IMDB score above 5.5:")
        for movie in high_rated:
            print(f"{movie['name']} - {movie['imdb']}")
    else:
        print("No movies have an IMDB score above 5.5.")

high_rated()
