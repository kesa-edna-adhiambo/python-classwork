class Animal:
    def make_sound(self):
        pass
    
    def move(self):
        pass
    
    def feed(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("Birds produce chirp sound")

    def move(self):
        print("The bird is flying")
    
    def feed(self):
        print("Birds feed on seeds")

class Fish(Animal):
    def make_sound(self):
        print("Fish clicks")
    
    def move(self):
        print("Fish moves by swimming")

    def feed(self):
        print("Fish feed on insects")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

    def move(self):
        print("Dogs move by running or walking")

    def feed(self):
        print("Dogs feed on meat")
    
class Human(Animal):
    def make_sound(self):
        print("Human speaks")
    
    def move(self):
        print("Human move by walking or running")
    
    def feed(self):
        print("Human feeds on vegetables and beef")

