# Week 6 Summary
This week introduced me to how Python interacts with files using simple yet powerful functions like open(), readlines(), and the with statement (which I’ve come to appreciate for its cleanliness and safety).
```python
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line)
```
Then working with CSV files using the csv module. Reading structured data and using it to power my programs gave me a little peek into what real-world data handling might feel like. Learning about DictReader and DictWriter made things feel even more intuitive and Pythonic.
```python
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
```
We can modify our code to use a part of the csv library called a DictReader to treat our CSV file with even more flexibilty:
import csv
```python
students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
```
Binary Files and PIL : 
This type of file can store anything including, music and image data.
There is a popular Python library called PIL that works well with image files.
Animated GIFs are a popular type of image file that has many image files within it that are played in sequence over and over again, creating a simplistic animation or video effect.
Imagine that we have a series of costumes, as illustrated below.

Here is costume1.gif.

![image](https://github.com/user-attachments/assets/b1e4a6f2-a14d-456f-adfc-6ad687cbaa37)

Here is costume2.gif. 

![image](https://github.com/user-attachments/assets/6613317f-ac15-437a-8839-fc179c058748)


Before proceeding, we make sure that we have downloaded the source code files from the course website. It will not be possible for us to code the following without having the two images above in your possession and stored in the IDE.
In the terminal window type code costumes.py and code as follows:
```python
import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
