class User:

    @classmethod
    def CreateUser(cls, parameter_list):
        fname,lname,age = parameter_list.split(",")
        return cls(fname,lname,int(age))

    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def full_name(self):
        return f"{self.fname} {self.lname}"

# user1 = User("Soumya","Sen",25)
# user2 = User("Pranoy","Das",27)
# print(user1.full_name(), user1.age)
# print(user2.full_name(), user2.age)
U1 = User.CreateUser("Soumya,Sen,25")
U2 = User.CreateUser("Pranoy,Das,27")
print(U1.full_name(), U1.age)
print(U2.full_name(), U2.age)