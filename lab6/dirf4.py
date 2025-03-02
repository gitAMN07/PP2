def count(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            line_count = sum(1 for _ in file)
        print(f"Number of lines: {line_count}")
    except FileNotFoundError:
        print("File not found.]")
    except Exception as e:
        print(f"An error: {e}")

file_path = input("File path: ")
count(file_path)