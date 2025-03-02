import os
def pathh(path):
    print(f"\nAccess for: {path}")
    if os.path.exists(path):
        print("Path exists")
        print("Readable" if os.access(path, os.R_OK) else "not readable")
        print("Writable" if os.access(path, os.W_OK) else "not writable")
        print("Executable" if os.access(path, os.X_OK) else "not executable")
    else:
        print("Path does not exist")

path = input("Path: ")
pathh(path)