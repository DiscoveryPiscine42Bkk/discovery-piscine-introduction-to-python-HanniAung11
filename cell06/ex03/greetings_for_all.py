#!/usr/bin/env python3
def greetings(name="noble stranger"):
    if isinstance(name,str):
        return print(f"Hello, {name}")
    else:return print("Error! It was not name.")
greetings('alexandra')
greetings('Wil')
greetings()
greetings(42)