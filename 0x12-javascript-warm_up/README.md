# Project: 0x12. JavaScript - Warm up

## Resources

#### Read or watch:

* [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
* [Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
* [Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
* [Operators](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
* [Operator Precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)
* [Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
* [Functions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)
* [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
* [Intrinsic Objects](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
* [Module patterns](https://darrenderidder.github.io/talks/ModulePatterns/#/)
* [var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8)
* [JavaScript Tutorial](https://www.youtube.com/watch?v=vZBCTc9zHtI)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## Learning Objectives

### General

* Why JavaScript programming is amazing
* How to run a JavaScript script
* How to create variables and constants
* What are differences between <code>var</code>, <code>const</code> and <code>let</code>
* What are all the data types available in JavaScript
* How to use the <code>if</code>, <code>if ... else</code> statements
* How to use comments
* How to affect values to variables
* How to use <code>while</code> and <code>for</code> loops
* How to use <code>break</code> and <code>continue</code> statements
* What is a function and how do you use functions
* What does a function that does not use any <code>return</code> statement return
* Scope of variables
* What are the arithmetic operators and how to use them
* How to manipulate dictionary
* How to import a file

## Tasks

* **0. First constant, first print**
  * [0-javascript_is_amazing.js](./0-javascript_is_amazing.js): Prints "JavaScript is amazing":
    * You must create a constant variable called myVar with the value "JavaScript is amazing"
    * You are not allowed to use `var`

* **1. 3 languages**
  * [1-multi_languages.js](./1-multi_languages.js): Prints 3 lines:
    * The first line: "C is fun"
    * The second line: "Python is cool"
    * The third line: "JavaScript is amazing"
    * You are not allowed to use `var`

* **2. Arguments**
  * [2-arguments.js](./2-arguments.js): Prints a message depending of the number of arguments passed:
    * If no arguments are passed to the script, print "No argument"
    * If only one argument is passed to the script, print "Argument found"
    * Otherwise, print "Arguments found"
    * You are not allowed to use `var`


* **3. Value of my argument**
  * [3-value_argument.js](./3-value_argument.js): Prints the first argument passed to it:
    * If no arguments are passed to the script, print "No argument"
    * You are not allowed to use `var`
    * You are not allowed to use length

* **4. Create a sentence**
  [4-concat.js](./4-concat.js): Prints two arguments passed to it, in the following format: " is "
    * You are not allowed to use `var`

* **5. An Integer**
  * [5-to_integer.js](./5-to_integer.js): Prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:
      * If the argument can’t be converted to an integer, print "Not a number"
      * You are not allowed to use `var`
      * You are not allowed to use `try/catch`

* **6. Loop to languages**
  * [6-multi_languages_loop.js](./6-multi_languages_loop.js): Prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop
    * The first line: "C is fun"
    * The second line: "Python is cool"
    * The third line: “"avaScript is amazing"
    * You are not allowed to use `var`
    * You are not allowed to use any `if/else` statement
    * You can use only one `console.log`
    * You must use a loop (`while`, `for`, etc.)


* **7. I love C**
  * [7-multi_c.js](./7-multi_c.js): prints `x` times "C is fun"
    * Where `x` is the first argument of the script
    * If the first argument can’t be converted to an integer, print "Missing number of occurrences"
    * You are not allowed to use `var`
    * You can use only two `console.log`
    * You must use a loop (`while`, `for`, etc.)

* **8. Square**
  * [8-square.js](./8-square.js): prints a square
    * The first argument is the size of the square
    * If the first argument can’t be converted to an integer, print "Missing size"
    * You must use the character `X` to print the square
    * You are not allowed to use `var`
    * You must use a loop (`while`, `for`, etc.)

* **9. Add**
  * [9-add.js](./9-add.js): Prints the addition of 2 integers
    * The first argument is the first integer
    * The second argument is the second integer
    * You have to define a function with this prototype: function add(a, b)
    * You are not allowed to use `var`

* **10. Factorial**
  * [10-factorial.js](./10-factorial.js): Computes and prints a factorial
    * The first argument is integer (argument can be cast as integer) used for computing the factorial
    * Factorial of NaN is 1
    * You must do it recursively
    * You must use a function
    * You are not allowed to use `var`

* **11. Second biggest!**
  * [11-second_biggest.js](./11-second_biggest.js): Searches the second biggest integer in the list of arguments.
    * You can assume all arguments can be converted to integer
    * If no argument passed, print 0
    * If the number of arguments is 1, print 0
    * You are not allowed to use `var`

* **12. Object**
  * [12-object.js](./12-object.js): Update a given script to replace the value 12 with 89:
    * You are not allowed to use `var`

* **13. Add file**
  * [13-add.js](./13-add.js): Function that returns the addition of 2 integers.
    * The function must be visible from outside
    * The name of the function must be add
    * You are not allowed to use `var`

* **14. Const or not const**
  * [100-let_me_const.js](./100-let_me_const.js): Modifies the value of myVar to 333 in the given [main file](./100-main.js).

* **15. Call me Moby**
  * [101-call_me_moby.js](./101-call_me_moby.js): Executes `x` times a function.
    * The function must be visible from outside
    * Prototype: function (`x`, theFunction)
    * You are not allowed to use `var`

* **16. Add me maybe**
  * [102-add_me_maybe.js](./102-add_me_maybe.js): Increments and calls a function.
    * The function must be visible from outside
    * Prototype: function (number, theFunction)
    * You are not allowed to use `var`

* **17. Increment object**
  * [103-object_fct.js](./103-object_fct.js): Update a gievn script by adding a new function incr that increments the integer value.
    * You are not allowed to use `var`
