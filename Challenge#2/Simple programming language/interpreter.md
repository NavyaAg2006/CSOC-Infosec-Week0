# Simple Language Interpreter

## 🧠 Overview

This project implements a **simple programming language** in Python. It recognizes simple commands such as variable assignment and arithmetic expressions, and supports evaluating expressions using stored variables.

## ✨ Features

* `let x = 5`: Assigns value `5` to variable `x`
* `print x`: Prints the value of `x`
* `print "hello"`: Prints the expression `hello`
* `let c = a + b`: Supports expressions with other variables
* Type `return` to finish input
* Basic error handling for:

  * Missing `=` in assignments
  * Unknown commands
  * Invalid expressions

## 💡 How It Works

1. **Input** is taken line-by-line from the user.
2. Each line is parsed and interpreted:

   * `let`: Extracts variable name and expression, evaluates it, and stores the result.
   * `print`: Evaluates and prints expressions using current variable values.
3. User types `return` to end input and run all lines.

## 🔧 How to Use

```plaintext
Enter your code line-by-line. Type 'return' to finish.
>> let a = 5
>> let b = 10
>> let c = a + b
>> print c
>> print b-a
>> print "hey!"
>> return
15
5
hey!
```

## 🛡 Limitations

* Only supports integers and `+ - * /` operators
* No support for parentheses or precedence rules
* No functions or control flow (e.g., if/else)

## 🏁 Ideal For

* Students learning how interpreters work
* Programming competitions that require minimalism and clarity
* Simple scripting tasks for educational purposes
