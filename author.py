class Author:
    def __init__(self, name, biography=""):
        self.__name = name
        self.__biography = biography

    # Getters and Setters for encapsulation
    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    def __str__(self):
        return f"{self.__name} - {self.__biography}"