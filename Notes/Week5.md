# Week 5 Summary
In this fifth week of CS50 Python, things got really interesting. I was introduced to the idea of checking whether my code works or not and that to by myself only ! With the use of : `assert`.
I learned how to use `assert` to set up conditions in my programs that must be true. If they’re not, Python throws an `AssertionError`, which honestly felt like my program calling me out. At first, it was a bit annoying, but it turned out to be super helpful. It’s like giving your code checkpoints to make sure it's not lying to you.

Then came **`pytest`**, and let me just say—it’s kind of addicting. I could write little tests to check if my functions were behaving, and `pytest` would tell me instantly if things were broken. It felt like having my own personal code critic that wasn’t mean about it. Super useful, especially for catching small mistakes before they become huge headaches.
Suppose we have a calculator.py file :
```python
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n + n


if __name__ == "__main__":
    main()
```
Now using this file's function in another file test_calculator.py
```python

  import pytest

  from calculator import square


  def test_positive():
      assert square(2) == 4
      assert square(3) == 9


  def test_negative():
      assert square(-2) == 4
      assert square(-3) == 9


  def test_zero():
      assert square(0) == 0


  def test_str():
      with pytest.raises(TypeError):
          square("cat")
```
Running this file using "$ pytest test_calculator.py" produces the following output : 
``` 
..F.                                                                     [100%]

=================================== FAILURES ===================================
________________________________ test_negative _________________________________

    def test_negative():
>       assert square(-3) == 9
E       assert -6 == 9
E        +  where -6 = square(-3)

test_calculator.py:11: AssertionError
=========================== short test summary info ============================
FAILED test_calculator.py::test_negative - assert -6 == 9
========================= 1 failed, 3 passed in 0.12s ==========================
```
We also explored how to take plain old modules and level them up into **packages** using `__init__.py`. That one small file made everything click—I could finally organize related functions neatly across multiple files and still keep everything connected. 
