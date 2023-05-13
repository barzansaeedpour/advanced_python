# Object-Oriented Programming Principles in Python

This repository provides examples of implementing key object-oriented programming principles using Python. Each principle is explained and demonstrated with code examples.

## Principles Covered

1. [Encapsulation](#encapsulation)
2. [Inheritance](#inheritance)
3. [Polymorphism](#polymorphism)
4. [Abstraction](#abstraction)
5. [Composition](#composition)

## Encapsulation

Encapsulation refers to the bundling of data and methods (behavior) within an object. It ensures that the internal state of an object is protected and can be accessed or modified only through defined interfaces (methods). Encapsulation promotes data hiding, abstraction, and modular design.

Example:
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self._mileage = 0

    def drive(self, distance):
        self._mileage += distance

    def get_mileage(self):
        return self._mileage

car = Car("Toyota", "Camry")
car.drive(100)
print(car.get_mileage())  # Output: 100
```

## Inheritance

Inheritance enables the creation of new classes (derived classes) based on existing classes (base or parent classes). The derived classes inherit the attributes and behaviors of the base class, allowing code reuse and the establishment of hierarchical relationships. Inheritance supports the "is-a" relationship and promotes code extensibility and flexibility.

Example:
``` python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(5, 3)
print(rectangle.area())  # Output: 15
```

## Polymorphism

Polymorphism allows objects of different types to be treated as instances of a common superclass. It enables methods to be overridden in derived classes, allowing the same method name to exhibit different behaviors based on the specific object type at runtime. Polymorphism promotes code flexibility, modularity, and facilitates the implementation of complex systems.

Example:
``` python
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

def make_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()

make_sound(dog)  # Output: Woof!
make_sound(cat)  # Output: Meow!
```

## Abstraction

Abstraction focuses on representing essential features of objects while hiding unnecessary details. It allows developers to create abstract classes or interfaces that define a common structure and behavior without specifying the specific implementation. Abstraction helps in managing complexity, separating concerns, and providing a high-level view of the system.

Example:
``` python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car started!"

car = Car()
print(car.start())  # Output: Car started!

```

## Composition

Composition refers to constructing complex objects or systems by combining simpler objects or components. It involves creating relationships between objects where one object contains or is composed of other objects. Composition promotes code reusability, flexibility, and enables the creation of modular and loosely coupled systems.

Example:
``` python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def get_engine_horsepower(self):
        return self.engine.horsepower

engine = Engine(200)
car = Car("Toyota", "Camry", engine)
print(car.get_engine_horsepower())  # Output: 200
```

## Contributing

Feel free to contribute by adding more examples, improving existing code, or suggesting enhancements.

## License

This project is licensed under the [MIT License](LICENSE).
