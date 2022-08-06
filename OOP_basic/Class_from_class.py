




class MyList(list):

    def even_length(self):
        return len(self) % 2 == 0

x = MyList()
print(isinstance(x, list))
print(x)
x.extend([1, 2, 3, 4, 5])
print(x)
print(x.even_length())
x.append(6)
print(x.even_length())

class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0

class MyList(list, EvenLengthMixin):
    def pop(self):
        x = super(MyList, self).pop()
        print("last value is", x)
        return x

print(MyList.mro())
x = MyList([1, 2, 3])
print(x.even_length())
x.append(4)
print(x.even_length())

ml = MyList([1, 2, 4, 17])
z = ml.pop()
print(z)
print(ml)

class MyDict(dict, EvenLengthMixin):
    pass

x = MyDict()
x["key"] = "value"
x["another key"] = "another value"
print(x.even_length())

#__________ПРИМЕР КОТОПЁС__________
class Cat():
   def say(self,times):
      print('Meow '*times)
class Dog():
   def say(self,times):
      print('Bow-Wow '*times)
class CatDog(Cat,Dog):
   pass

class DogCat(Dog,Cat):
   pass

muteDog=CatDog()
muteDog.say(3)       #Meow Meow Meow

muteCat=DogCat()
muteCat.say(2)       #Bow-Wow Bow-Wow


















