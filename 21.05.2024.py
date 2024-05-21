
class Animal:

    def my_voice(self, count):
        print("Hello")


class Cat(Animal):
    def my_voice(self, count):
        for i in range(1, count +1):
            print("мяу")


class Dog(Animal):
    def my_voice(self, count):
        for i in range(1, count +1):
            print("гав")


class NoneAnimal(Animal):
    ...


dog_obj = Dog()
dog_obj.my_voice(count=4)


dog_obj = Cat()
dog_obj.my_voice(count=4)

