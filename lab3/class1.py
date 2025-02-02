class String:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())

string_object = String()
string_object.getString()
string_object.printString()