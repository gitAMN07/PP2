def is_high_rated():
    name = input("Movie name: ")
    try:
        imdb_score = float(input("IMDB score: "))
        if imdb_score > 5.5:
            print(f"True")
        else:
            print(f"False")
    except ValueError:
        print("Invalid IMDB")

is_high_rated()