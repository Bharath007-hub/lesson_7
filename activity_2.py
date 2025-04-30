class student:
    grade = 10
    name = 'Bharath'
    def introduction (self):
        print("Hi i am a student.")

    def details(self):
        print("my name is", self.name)
        print("I study in grade", self.grade)

ob = student()
ob.introduction()
ob.details()