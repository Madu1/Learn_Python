import pickle


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Name: {self.name} and Age: {self.age} years old.")


p1 = Person("Nike", 23)
p1.print_info()
pickle_object = pickle.dumps(p1)
print(f"My pickled object is: \n {pickle_object}")
unpickle_object = pickle.loads(pickle_object)
print(f"My unpickled object is: \n Name: {unpickle_object.name} & Age: {unpickle_object.age}")