# Week 3:Summary

In Week 3 of CS50's Introduction to Programming with Python, I stepped into one of the most practical parts of programming: **handling errors** and writing code that doesn’t break under pressure. This week was focused on how Python deals with **runtime errors**, the kind that don’t show up until your code actually runs—like dividing by zero or converting a word into an integer. Instead of letting the program crash, I learned how to use `try` and `except` blocks to handle these issues gracefully.

We explored how the `else` clause works in conjunction with `try`, allowing us to write code that only runs if no exceptions were raised—making the logic clearer and safer. Another interesting part of the week was creating a function that keeps prompting the user until they give a valid integer. It’s a simple but powerful example of combining loops, exception handling, and clean design.

We also touched on the `pass` keyword, which is Python’s way of saying “do nothing here for now”—something that’s surprisingly handy when structuring functions or placeholder blocks.

---

## 🧪 Sample Code: Getting a Valid Integer

```python
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()
