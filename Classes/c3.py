import random

class MyList(list): # inherits from list
    

    def shuffle(self):
        random.shuffle(self)

    def get_random(self):
        return random.choice(self)

# object
a = MyList([12,72,39,121,2,3,4,8,9])
a.sort()
print(a)
a.shuffle
print(a)
print("random items from list=",a.get_random())