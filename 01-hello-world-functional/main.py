"""
This script prints "Hello, World!" to the console using a function called main. The main function is a common convention.
The main function is called when the script is run. The if __name__ == "__main__": block is used to call the main function.
Calling the main function this way allows the script to be imported into other scripts without running the main function,
which is how scripts can be used as modules from other scripts.

Challenge: Write a function named hacker that prints "Hello, Hacker!", and have it called right after the main function is called.
"""
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
