#Animals
from abc import ABC, abstractmethod
class Animal(ABC):

    def __init__(self, name, age, breed, owner):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner

    def sleep(self):
        print(f"{self.name} is sleeping soundly...")

class Dog(Animal):

    def __init__(self, name, age, breed, owner):
        super().__init__(name, age, breed, owner)
                         
    def speak(self):
        print(f"{self.name} says Woof Woof!")

class Cat(Animal):

    def __init__(self, name, age, breed, owner):
        super().__init__(name, age, breed, owner)
                         
    def speak(self):
        print(f"{self.name} says Meow Meow!")

class Rabbit(Animal):
    def __init__(self, name, age, breed, owner=None):
        super().__init__(name, age, breed, owner=None)
                         
    def speak(self):
        print(f"{self.name} says Squeak Squeak!")

class Parrot(Animal):
    def __init__(self, name, age, breed, owner):
        super().__init__(name, age, breed, owner)

    def speak(self):
        print(f"{self.name} squawks: 'Surprise, motherf***er!'")

    def fly(self):
        print(f"{self.name} is flying all over the place!")

class owner:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

class staff:
    def __init__(self, name, position, phone, email):
        self.name = name
        self.position = position
        self.phone = phone
        self.email = email

    def display_info(self):
        print(f"Employee: {self.name}, Position: {self.position}, Phone: {self.phone}, Email: {self.email}")

    def work_with_animal(self, animal):
        print(f"{self.name} is working with {animal.name}, the {animal.breed}.")

o1 = owner("Dexter Morgan", "Palm Terrace 1155 103rd St, Miami Beach, FL", "305-555-1234", "dexter.morgan@miamimetro.gov")
o2 = owner("Debra Morgan", "1011 Coral Drive, Miami, FL", "305-555-5678", "debra.morgan@mmiamimetro.gov")
o3 = owner("Angel Batista", "447 Ocean View Blvd, Miami, FL", "305-555-8765", "angel.batista@miamimetro.gov")
o4 = owner("Vincent Masuka", "221B Baker St, Miami, FL", "305-555-4321", "vincent.masuka@miamimetro.gov")
o5 = owner("James Doakes", "225 Ocean Breeze Ave, Miami, FL", "305-555-6789", "james.doakes@miamimetro.gov")


d1 = Dog("Shadow", 5, "Belgian Malinois", o1)
d2 = Dog("Rex", 3, "German Shepherd", o2)

c1 = Cat("Luna", 2, "Siamese", o3)
c2 = Cat("Pixel", 4, "Bengal", o4)
c3 = Cat("Cleo", 6, "Persian", o5)

r1 = Rabbit("Whisper", 1, "Netherland Dwarf")
r2 = Rabbit("Nibbles", 2, "Mini Lop")
r3 = Rabbit("Pepe", 3, "Lionhead")
r4 = Rabbit("Turbo", 4, "Dutch")
r5 = Rabbit("Velvet", 5, "Holland Lop")

p1 = Parrot("Echo", 5, "African Grey", o5)
p2 = Parrot("Sunny", 2, "Macaw", o3)

s1 = staff("Hannah McKay", "Veterinarian", "305-555-3001", "hannah.mckay@miamivetclinic.com")
s2 = staff("Miguel Prado", "Assistant Veterinarian", "305-555-3002", "miguel.prado@miamivetclinic.com")
s3 = staff("Lila Tournay", "Animal Caretaker", "305-555-3003", "lila.tournay@miamivetclinic.com")
s4 = staff("Travis Marshall", "Groomer", "305-555-3004", "travis.marshall@miamivetclinic.com")
s5 = staff("Jordan Chase", "Trainer", "305-555-3005", "jordan.chase@miamivetclinic.com")
s6 = staff("Rudy Cooper", "Receptionist", "305-555-3006", "rudy.cooper@miamivetclinic.com")
s7 = staff("Dexters Therapist", "Manager", "305-555-3007", "dr.therapist@miamivetclinic.com")

s4.display_info()
s1.work_with_animal(c3)