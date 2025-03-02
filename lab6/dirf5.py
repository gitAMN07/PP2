def l_to_f(file_path, data_list):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            for item in data_list:
                file.write(str(item) + "\n")
        print(f"List written to {file_path}")
    except Exception as e:
        print(f"Error: {e}")

data = ["Mustang", "Mercedes", "Toyota", "Tesla", "Geely"]
file_path = input("File path: ")
l_to_f(file_path, data)