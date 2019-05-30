#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "x", getattr(magic_string, "x", -1) + 1)
    return "Holberton" + ", Holberton" * getattr(magic_string, "x", 0)
