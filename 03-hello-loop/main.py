"""
Loops can be used to repeat an action for a given number of times, until a condition is met, or indefinitely, waiting for an external signal to break the loop.
Ranges can be a way to give a start value (inclusive), end value (exclusive), and an increment, either positive or negative. Just giving a single number parameter
to range will create a list of that many numbers plus 1, starting with 0.

Challenge: Use a loop to make the output say "Hello, and have a very, very, very, very, very nice day.".
"""

def main():
    loopRange = range(1)
    print(f"loopRange is a list of numbers: {loopRange}")
    verys = []
    for i in loopRange:
        verys.append("very")
    print(f"Hello, and have a {', '.join(verys)} nice day.")

if __name__ == "__main__":
    main()
