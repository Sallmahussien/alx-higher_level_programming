# Project: 0x08. Python - More Classes and Objects

## Resources

#### Read or watch:

* [Object Oriented Programming](https://python.swaroopch.com/oop.html)
* [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)
* [Class and Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)
* [classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)
* [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
* [str vs repr](https://shipit.dev/posts/python-str-vs-repr.html)
## Learning Objectives

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files.

### General

* Why Python programming is awesome 
* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is <code>self</code>
* What is a method
* What is the special <code>__init__</code> method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* What are the special <code>__str__</code> and <code>__repr__</code> methods and how to use them
* What is the difference between <code>__str__</code> and <code>__repr__</code>
* What is a class attribute
* What is the difference between a object attribute and a class attribute
* What is a class method
* What is a static method
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is and what does contain <code>__dict__</code> of a class and of an instance of a class
* How does Python find the attributes of an object or class
* How to use the <code>getattr</code> function


## Tasks

* **0. Simple rectangle**
  * [0-rectangle.py](./0-rectangle.py): Empty Python class that defines a rectangle.

* **1. Real definition of a rectangle**
  * [1-rectangle.py](./1-rectangle.py): Python class that defines a rectangle. Builds on
  [0-rectangle.py](./0-rectangle.py) with:
    * Private instance attribute `width`.
    * Property getter `def width(self):` to get `width`.
    * Property setter `def width(self, value):` to set `width`.
    * Private instance attribute `height`.
    * Property getter `def height(self):` to get `height`.
    * Property setter `def height(self, value):` to set `height`.
    * Instantiation with optional `width` and `height`: `def __init(self,
    width=0, height=0):`
  * If either of `width` or `height` is not an integer, a `TypeError` is
  raised with the message `width must be an integer` or `height must be an integer`.
  * If either of `width` or `height` is less than `0`, a `ValueError` is
  raised with the message `width must be >= 0` or `height must be >= 0`.

* **2. Area and Perimeter**
  * [2-rectangle.py](./2-rectangle.py): Python class that defines a rectangle. Builds on
  [1-rectangle.py](./1-rectangle.py) with:
    * Public instance method `def area(self):` that returns the area of
    the rectangle.
    * Public instance attribute `def perimeter(self):` that returns the
    permiter of the rectangle (if either of `width` or `height` equals `0`, the
    perimeter is `0`).

* **3. String representation**
  * [3-rectangle.py](./3-rectangle.py): Python class that defines a rectangle. Builds on
  [2-rectangle.py](./2-rectangle.py) with:
    * Special method `__str__` to print the rectangle with the `#` character
    (if either of `width` or `height` equals `0`, the method returns an empty
    string.).

* **4. Eval is magic**
  * [4-rectangle.py](./4-rectangle.py): Python class that defines a rectangle. Builds on
  [3-rectangle.py](./3-rectangle.py) with:
    * Special method `__repr__` to return a string representation of the
    rectangle.

* **5. Detect instance deletion**
  * [5-rectangle.py](./5-rectangle.py): Python class that defines a rectangle. Builds on
  [4-rectangle.py](./4-rectangle.py) with:
    * Special method `__del__` that prints the message `Bye rectangle...`
    when a `Rectangle` is deleted.

* **6. How many instances**
  * [6-rectangle.py](./6-rectangle.py): Python class that defines a rectangle. Builds on
  [5-rectangle.py](./5-rectangle.py) with:
    * Public class attribute `number_of_instances` that is initialized to `0`,
    incremented for each new instantiation, and decremened for each instance deletion.

* **7. Change representation**
  * [7-rectangle.py](./7-rectangle.py): Python class that defines a rectangle. Builds on
  [6-rectangle.py](./6-rectangle.py) with:
    * Public class attribute `class_symbol` that is initialized to `#` but can
    be any type - used as the symbol for string representation.

* **8. Compare rectangles**
  * [8-rectangle.py](./8-rectangle.py): Python class that defines a rectangle. Builds on
  [7-rectangle.py](./7-rectangle.py) with:
    * Static method `def bigger_or_equal(rect_1, rect_2):` that returns the
    rectangle with the greater area (returns `rect_1` if both areas are equal).
    * If either of `rect_1` or `rect_2` is not a `Rectangle` instance, a
    `TypeError` is raised with the message `rect_1 must be an instance of
    Rectangle` or `rect_2 must be an instance of Rectangle`.

* **9. A square is a rectangle**
  * [9-rectangle.py](./9-rectangle.py): Python class that defines a rectangle. Builds on
  [8-rectangle.py](./8-rectangle.py) with:
    * Class method `def square(cls, size=0):` that returns a new `Rectangle`
    instance with `width == height == size`.

* **10. N Queens**
  * [101-nqueens.py](./101-nqueens.py): Python program that solves the [N queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle).
  * Usage: `./101-nqueens.py N`
  * Determines all possible solutions for placing N non-attacking queens on an
  NxN chessboard.
  * Exactly two arguments must be provided. Otherwise, the program prints
  `Usage: nqueens N` and exits with the status `1`.
  * If the provided `N` is not an integer, the program prints `N must be a
  number` and exits with the status `1`.
  * If the provided `N` is less than `4`, the program prints `N must be at least
  4` and exits with the status `1`.
  * Solutions are printed one per line in the format `[[r, c], [r, c], [r, c],
  [r, c]]` where `r` and `c` represent the row and column, respectively, where a
  queen must be placed.