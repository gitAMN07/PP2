import os
def d_file(fi_path):
    if os.path.exists(fi_path):
        print(f"\nzFile exists: {fi_path}")
        if os.access(fi_path, os.W_OK):
            try:
                os.remove(fi_path)
                print("File deleted.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Permission denied.")
    else:
        print("The file does not exist.")

fi_path = input("File path: ")
d_file(fi_path)