import pickle


class Pet:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def print_info(self):
        print(f"Name: {self.name}, Age:{self.age} & Weight: {self.weight}")


'''pt = Pet("Bunny",1, 20)
pt.print_info()'''

'''with open('pet.pickle', 'wb')as f:
    pickle.dump(pt, f)
'''

with open('pet.pickle', 'rb')as f:
    pt = pickle.load(f)

pt.print_info()