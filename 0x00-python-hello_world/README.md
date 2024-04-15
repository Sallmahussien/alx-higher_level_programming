# Project: 0x00. Python - Hello, World

## Resources

#### Read or watch:

* [The Python tutorial](https://docs.python.org/3/tutorial/index.html) (only the first three chapters below)
* [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
* [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
* [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html) (Read up until “3.1.2. Strings” included)
* [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
* [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [Pycodestyle -- Style Guide for Python Code](https://pypi.org/project/pycodestyle/)
## Learning Objectives

### General

* Why Python programming is awesome
* Who created Python
* Who is Guido van Rossum
* Where does the name ‘Python’ come from
* What is the Zen of Python
* How to use the Python interpreter
* How to print text and variables using <code>print</code>
* How to use strings
* What are indexing and slicing in Python
* What is the official Python coding style and how to check your code with <code>pycodestyle</code>

## Tests

* [tests](./tests): Folder of test files.

## Function Prototypes

Prototypes for functions written in this project:

| File                       | Prototype                             |
| -------------------------- | ------------------------------------- |
| `10-check_cycle.c`         | `int check_cycle(listint_t *list);`   |
| `102-magic_calculation.py` | `def magic_calculation(a, b):`        |


## Tasks


* **0. Run Python File**
  * [0-run](./0-run): Bash script that runs a Python script file saved
  in the environment variable `$PYFILE`.

* **1. Run inline**
  * [1-run_inline](./1-run_inline): Bash script that runs Python code saved in the
  environment variable `$PYCODE`.

* **2. Hello, print**
  * [2-print.py](./2-print.py): Python script that prints exactly `"Programming is
  like building a multilingual puzzle`, followed by a new line using the function `print`.

* **3. Print integer**
  * [3-print_number.py](./3-print_number.py): Python script that prints the integer stored
  in the variable `number`, followed by `Battery street`, followed by a new line.
  * Completion of [this source code](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py).

* **4. Print float**
  * [4-print_float.py](./4-print_float.py): Python script that prints the float stored
  in the variable `number` with a precision of two digits.
  * Completion of [this source code](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py).

* **5. Print string**
  * [5-print_string.py](./5-print_string.py): Python script that prints a string stored
  in the variable `str` three times, then a new line, then the first nine characters
  contained in `str`, followed by another new line.
  * Completion of [this source code](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py).

* **6. Play with strings**
  * [6-concat.py](./6-concat.py): Python script that prints `Welcome to Holberton
  School!` using the variables `str1 = "Holberton"` and `str2 = "School"`.
  * Completion of [this source code](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py).

* **7. Copy - Cut - Paste**
  * [7-edges.py](./7-edges.py): Python script that sets three string variables based
  on the string contained in the variable `word` as follows:
  * `word_first_3`: Contains the first three letters of the variable `word`.
  * `word_last_2`: Contains the last two letters of the variable `word`.
  * `middle_word`: Contains the value of the variable `word` without the first and last letters.
  * Completion of [this source code](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py).

* **8. Create a new sentence**
  * [8-concat_edges.py](./8-concat_edges.py): Python script that prints `object-oriented
  programming with Python`, followed by a new line without creating new variables or
  string literals.
  * Completion of [this source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py).

* **9. Easter Egg**
  * [9-easter_egg.py](./9-easter_egg.py): Python script that prints "The Zen of Python" by
  Tim Peters, followed by a new line.

* **10. Linked list cycle**
  * [10-check_cycle.c](./10-check_cycle.c): C function that checks if a linked list
  contains a cycle.
  * Returns `0` if there is no cycle and `1` if there is.
  * Helper files:
    * [10-linked_lists.c](./10-linked_lists.c): C functions handling linked lists for testing
    * [lists.h](./lists.h): Header file containing definitions and prototypes for
    all types and functions used in [10-linked_lists.c](./10-linked_lists.c) and
    [10-check_cycle.c](./10-check_cycle.c).

* **11. Hello, write**
  * [100-write.py](./100-write.py): Python script that prints exactly `and that piece of
  art is useful - Dora Korpar, 2015-10-19`, followed by a new line to `stderr` using
  the function `write` from the `sys` module.
  * Exits with a status code of `1`.

* **12. Compile**
  * [101-compile](./101-compile): Python script that compiles a Python script file stored
  in the environment variable `$PYFILE` and saves it to an output file
  `$PYFILEc` (ex. `export PYFILE=my_main.py` => output filename: `my_main.pyc`).

* **13. ByteCode -> Python #1**
  * [102-magic_calculation.py](./103-magic_calculation.py): Python function matching exactly
  the following bytecode:
  ```bash
   3           0 LOAD_CONST               1 (98)
               3 LOAD_FAST                0 (a)
               6 LOAD_FAST                1 (b)
               9 BINARY_POWER
              10 BINARY_ADD
              11 RETURN_VALUE
  ```