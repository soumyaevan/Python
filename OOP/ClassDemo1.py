class User:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def full_name(self):
        return f"{self.fname} {self.lname}"

#Added Comment- This is implemetation of Class User in ClassDemo1.py
user1 = User("Soumya","Sen",25)
user2 = User("Pranoy","Das",27)
print(user1.full_name(), user1.age)
print(user2.full_name(), user2.age)