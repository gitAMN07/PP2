import os

def list(path):
    if not os.path.exists(path):
        print("Invalid path!")
        return
    
    entriies = os.listdir(path)
    directories = [entry for entry in entriies if os.path.isdir(os.path.join(path, entry))]
    files = [entry for entry in entriies if os.path.isfile(os.path.join(path, entry))]
    print("\nOnly Directories:")
    print("\n".join(directories) if directories else "No directories found.")
    print("\nOnly Files:")
    print("\n".join(files) if files else "No files found.")
    print("\nAll Directories and Files:")
    print("\n".join(entriies) if entriies else "Directory is empty.")

path = input("Enter dir: ")
list(path)