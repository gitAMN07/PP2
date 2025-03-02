def copy_file(source, destination):
    try:
        with open(source, "r", encoding="utf-8") as src_file:
            content = src_file.read()
        with open(destination, "w", encoding="utf-8") as dest_file:
            dest_file.write(content)
        print(f"File copied {source} to {destination}")
    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print(f"Error: {e}")

source_file = input("File path: ")
destination_file = input("Destination file path: ")
copy_file(source_file, destination_file)