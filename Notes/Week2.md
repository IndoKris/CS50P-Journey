# Week 2 Summary

In week 2 of CS50 Python, I tackled loops and data structures. I learned `while` loops (repeating code until a condition changes) and `for` loops (looping over items in a list). It was cool how `range()` can automatically generate numbers for me, so I don't have to manually count. I played with `continue` and `break` to control loops – `continue` skips to the next iteration and `break` stops the loop early, which turned out handy when validating input.

I used `len(my_list)` to get a list’s length easily. I was intrigued by dictionaries: they let me associate keys with values (like mapping names to houses) in a single variable. Lastly, learning that Python’s special value `None` basically means no value gave me an **aha** moment about how empty or missing values are handled. I did hit bumps (like an infinite loop when I forgot to update a counter), but fixing that felt satisfying.

I understood more about python dictionay , I got to know how to write dictionary in a more efficient way , as before I used to create a dictionary and then mark it values in a list of strings and accessing it using their index but now i have learned a new way to create a dicionary with such kind and acccessing the value here is also very easy :
```python
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student], sep=", ")
```

 Now, further modify the code as follows:
```python
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
```
