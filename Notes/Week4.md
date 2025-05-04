# Week 4 Summary

This week was where things really started to feel *powerful*. Instead of just writing code, I learned how to **extend** Python by importing **modules**, working with **APIs**, and using third-party tools like `cowsay` that somehow made everything unexpectedly entertaining.

This week was about **Python's modular magic**. I learned how to import standard modules like `random`, `statistics`, and `sys`, and how to use `from x import y` to grab only what I needed. Working with **command-line arguments** using `sys.argv` helped me build scripts that actually respond to input—kind of like making tiny command-line apps.
I hit a few bumps too—like when I learned the hard way what an `IndexError` is—but handling those errors using `sys.exit()` and smart conditional checks made my programs more bulletproof.
And then came the real game changers: **packages, pip, and PyPI**. The idea that I could install Python packages made me feel like I’d unlocked the internet for my code.

---
# Working with APIs & JSON

I had so much fun learning how APIs work. Using the `requests` module, I could fetch real data from external services. Once I pulled the data, **parsing JSON** using Python’s built-in `json` module was straightforward and deeply satisfying. It felt like I was finally speaking the language of the web.

Here’s a quick sample of how I handled an API response:

```python
import requests
import json

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = response.json()
print(f"🪙 Bitcoin price in USD: ${data['bpi']['USD']['rate']}")
```
My Favourite part of this week was this....!!!
```python
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow(f"Hey there, {sys.argv[1]}! Keep coding!")
else:
    cowsay.trex("You're supposed to pass your name, hooman.")
```
Output of above program:
```
  _______________________________
< Hey there, world! Keep coding! >
  ===============================
         \
          \   ^__^
           \  (oo)\_______
              (__)\       )\/\
                  ||----w |
                  ||     ||
```
This is my favourite one !!
```
 _______________________
< Hello from the dragon! >
 -----------------------
        \                    / \  //\
         \    |\___/|      /   \//  \\
              /0  0  \__  /    //  | \ \    
             /     /  \/_/    //   |  \  \  
             @_^_@'/   \/_   //    |   \   \ 
             //_^_/     \/_ //     |    \    \ 
          ( //) |        \///      |     \     \ 
        ( / /) _|_ /   )  //       |      \     _\
      ( // /) '/,_ _ _/  ( ; -.    |    _ _\.-~        .-~~~^-.
    (( / / )) ,-{        _      `-.|.-~-.           .~         `.
   (( // / ))  '/\      /                 ~-. _ .-~      .-~^-.  \
   (( /// ))      `.   {            }                   /      \  \
    (( / ))     .----~-.\        \-'                 .~         \  `. \^-.
               ///.----..>        \             _ -~             `.  ^-`  ^-_
                 ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
