# Week 0 Summary
This week was all about getting comfortable with the basics of programming.
I explored how data types like str, int, and float work.
I learned how to define variables, write functions using def, and return values with return.

Also touched on operators (+, -, %, etc.) and started understanding how to build logical steps using pseudocode. Python’s interactive mode made it easier to test things quickly, and writing clean code with proper comments was encouraged from the start.

Used string methods such as strip() and title() , Learned new way to write strings known as f-strings or formatted string.
```python
name = input("What's your name? ").strip().title()

# Print the output
print(f"hello, {name}")
```
Creating a user-defined function using "def" keyword !
```python
def main():

    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()


# Create our own function
def hello(to="world"):
    print("hello,", to)


main()
```
At last I got to learn more about the concept of "return"
```python def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()
```
