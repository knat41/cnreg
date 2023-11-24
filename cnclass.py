class Person:
    """A simple person class"""
    name = ''
    nationalID = 0

    def __init__(self, name):
        self.name = name
        
    def get_id(self):
        return self.nationalID
    
class Teacher(Person):
    schoolID = 0
    Exam Hour
