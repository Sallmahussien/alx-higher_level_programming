# Project: 0x01. Python - if/else, loops, functions

## Resources

#### Read or watch:

* [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (Read until “4.6. Defining Functions” included)
* [IndentationError](https://www.youtube.com/watch?v=1QXOd2ZQs-Q)
* [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
* [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [Learn to Program 2 : Looping](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [Pycodestyle -- Style Guide for Python Code](https://pypi.org/project/pycodestyle/)
## Learning Objectives

### General

* Why Python programming is awesome
* Why indentation is so important in Python
* How to use the <code>if</code>, <code>if ... else</code> statements
* How to use comments
* How to affect values to variables
* How to use the <code>while</code> and <code>for</code> loops
* How is Python’s <code>for</code> different from <code>C</code>‘s?
* How to use the <code>break</code> and <code>continues</code> statements
* How to use <code>else</code> clauses on loops
* What does the <code>pass</code> statement do, and when to use it
* How to use <code>range</code>
* What is a function and how do you use functions
* What does return a function that does not use any <code>return</code> statement
* Scope of variables
* What’s a traceback
* What are the arithmetic operators and how to use them

## Tests
* [tests](./tests): Folder of test files.

## Function Prototypes

Prototypes for functions written in this project:

| File                       | Prototype                                               |
| -------------------------- | ------------------------------------------------------- |
| `7-islower.py`             | `def islower(c):`                                       |
| `8-uppercase.py`           | `def uppercase(str):`                                   |
| `9-print_last_digit.py`    | `def print_last_digit(number):`                         |
| `10-add.py`                | `def add(a, b):`                                        |
| `11-pow.py`                | `def pow(a, b):`                                        |
| `12-fizzbuzz.py`           | `def fizzbuzz():`                                       |
| `13-insert_number.c`       | `listint_t *insert_node(listint_t **head, int number);` |
| `101-remove_char_at.py`    | `def remove_char_at(str, n):`                           |
| `102-magic_calculation.py` | `def magic_calculation(a, b, c):`                       |

## Tasks

* **0. Positive anything is better than negative nothing**
  * [0-positive_or_negative.py](./0-positive_or_negative.py): Python program that assigns
  a random signed number to the variable `number` each time it is executed and
  prints whether `number` is positive or negative.
  * Prints the number followed by:
    * If the number is greater than 0: `is positive`
    * If the number is 0: `is zero`
    * If the number is less than 0: `is negative`
    * Followed by a new line.
  * Completion of [this source code](https://github.com/alx-tools/0x01.py/blob/master/0-positive_or_negative_py).

* **1. The last digit**
  * [1-last_digit.py](./1-last_digit.py): Python program that assigns a random signed number
  to the variable `number` each time it is executed and prints its last digit.
  * Prints the string `Last digit of [number] is [last_digit]` followed by:
    * If the number is greater than 5: `and is greater than 5`
    * If the number is 0: `and is 0`
    * If the number is less than 6 and not 0: `and is less than 6 and not 0`
    * Followed by a new line.
  * Completion of [this source code](https://github.com/alx-tools/0x01.py/blob/master/1-last_digit_py).

* **2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game**
  * [2-print_alphabet.py](./2-print_alphabet.py): Python program that prints the alphabet
  in lowercase, not followed by a new line.
  * Using only one `print` and one loop.
  * Without storing characters in variables or importing modules.

* **3. When I was having that alphabet soup, I never thought that it would pay off**
  * [3-print_alphabt.py](./3-print_alphabt.py): Python program that prints the
  alphabet in lowercase, followed by a new line.
  * Using only one `print` and one loop.
  * Without storing characters in variables or importing modules.
  * Prints every letter except for `q` and `e`.

* **4. Hexadecimal printing**
  * [4-print_hexa.py](./4-print_hexa.py): Python program that prints all numbers from
  `0` to `98` in decimal and hexadecimal.
  * Using only one `print` and one loop.
  * Without storing numbers or strings in variables or importing modules.
  * Printing format: `[decimal] = [hexadecimal]`

* **5. 00...99**
  * [5-print_comb2.py](./5-print_comb2.py): Python program that prints numbers from `0`
  to `99` two digits each.
  * Numbers are separated by `, `, except for the last number, which is followed by a new line.
  * Using no more than two `print` functions and one loop.
  * Without storing numbers or strings in variables or importing modules.

* **6. Inventing is a combination of brains and materials. The more brains you use, the less material you need**
  * [6-print_comb3.py](./6-print_comb3.py): Python program that prints all possible
  different combinations of two digits in ascending order.
  * Numbers are separated by `, `, except for the last number, which is followed by a new line.
  * The two digits must be different - `01` and `10` are considered identical.
  * Using no more than three `print` functions and two loops.
  * Without storing numbers or strings in variables or importing modules.

* **7. islower**
  * [7-islower.py](./7-islower.py): Python function that checks for lowercase characters.
  * Returns `True` if `c` is lowercase, `False` otherwise.
  * Without importing modules or using `str.upper()` or `str.isupper()`.

* **8. To uppercase**
  * [8-uppercase.py](./8-uppercase.py): Python function that prints a string in
  uppercase followed by a new line.
  * Using no more than two `print` functions and one loop.
  * Without importing modules or using `str.upper()` or `str.isupper()`.

* **9. There are only 3 colors, 10 digits, and 7 notes; its what we do with them that's important**
  * [9-print_last_digit.py](./9-print_last_digit.py): Python function that prints the last
  digit of a number.
  * Returns the value of the last digit.
  * Without importing modules.

* **10. a + b**
  * [10-add.py](./10-add.py): Python function that returns the addition of two integers.
  * Without importing modules.

* **11. a ^ b**
  * [11-pow.py](./11-pow.py): Python function that returns `a` to the power of `b`.
  * Without importing modules.

* **12. Fizz Buzz**
  * [12-fizzbuzz.py](./12-fizzbuzz.py): Python function that prints the numbers from
  `1` to `100` followed by a space.
  * For multiples of three, `Fizz` is printed instead of the number.
  * For multiples of five, `Buzz` is printed instead of the number.
  * For multiples of three and five, `FizzBuzz` is printed instead of the number.
  * Without importing modules.

* **13. Insert in sorted linked list**
  * [13-insert_number.c](./13-insert_number.c): C function that inserts a number
  into a sorted linked list.
  * If the function fails, returns `NULL`.
  * Otherwise, returns the address of the new node.
  * Helper files:
    * [linked_lists.c](./linked_lists.c): C functions handling linked lists for testing
    [13-insert_number.c](./13-insert_number.c).
    * [lists.h](./lists.h): Header file containing definitions and prototypes for
    all types and functions used in [linked_lists.c](./linked_lists.c) and
    [13-insert_number.c](./13-insert_number.c).

* **14. Smile in the mirror**
  * [100-print_tebahpla.py](./100-print_tebahpla.py): Python program that prints the alphabet
  in reverse order, alternating lowercase and uppercase, not followed by a new line.
  * Using only one `print` and one loop.
  * Without storing characters in variables or importing modules.

* **15. Remove at position**
  * [101-remove_char_at.py](./101-remove_char_at_py): Python function that
  creates a copy of a string without the character at position `n`.
  * Without importing modules.

* **16. ByteCode -> Python #2**
  * [102-magic_calculation.py](./102-magic_calculation.py): Python function matching exactly a
  bytecode provided by Holberton School.