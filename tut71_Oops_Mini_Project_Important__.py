# Mini project Library Class .. 

# Display book
# Lend book
# Add book 
# Return book

class Library:
    def __init__(self, listbook , libraryname):
        self.listbook = listbook
        self.libraryname = libraryname

    @property
    def displaybook(self):
        return f"The List of Books are ---- {self.listbook}"

    # @property 
    # def libraryname (self):
    #     return f"The name of the Library is --------- {self.libraryname}"


Shashwat = Library(["Marathi Vykaran", "Hindi Vykaran", "English Grammar", "Maths.. "], "Shashwat's Library")

print(Shashwat.displaybook)