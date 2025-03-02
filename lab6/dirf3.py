import os
def path_details(path):
    if os.path.exists(path):
        print(f"\nThe path exists: {path}")
        directory = os.path.dirname(path)
        filename = os.path.basename(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print("\nThe path does not exist.")

path = input("Enter the path to check: ")
path_details(path)