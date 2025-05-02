# Week 1 Summary

This week was all about making decisions in code. I learned how to use `if`, `elif`, and `else` to let programs react differently based on conditions. We explored logical operators like `and`, `or`, and `not`, and how Boolean logic (`True`/`False`) controls flow.  


```python
# Check if number is even or odd using modulo
n = 4
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```
Then we moved on to something called conditional expressions, which are basically one-liner if-else statements. Like this:
Using conditional expression to return True/False based on condition
```python
return True if n % 2 == 0 else False
```
It looks clean and concise, but then came the Pythonic twist — this whole expression just returns the result of n % 2 == 0, which is already a boolean! So it can be simplified even further to:
```python
# Pythonic way to return result directly without the need for full conditional expression
return n % 2 == 0
```

At last I learned about the `match` statement, which kind of works like switch-case, and lets you match multiple values using the `|` symbol — like:  
```python
match choice :
  case "yes" | "y":
  case "no" | "n" :
```
```python 
# A basic program using match-case to handle mathematical operations

operation = input("Enter the operation (add | subtract): ").lower()

match operation:
    case "add" | "sum":
        print("You chose to add numbers!")
    case "subtract" | "minus":
        print("You chose to subtract numbers!")
    case _:
        print("Invalid operation. Please choose 'add' or 'subtract'.")
```


