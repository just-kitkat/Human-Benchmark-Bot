"""
This is a simple project to try and use code to get
the lowest time possible on Human benchmark.

Website: https://humanbenchmark.com/tests/reactiontime
"""

import time
import argparse
from Autos import reaction, aim

SUPPORTED_TESTS = [
    "reaction",
    "aim"
]

parser = argparse.ArgumentParser(
    prog="Human Benchmark Autoclicker",
    description="This program helps you gain a very low score for reaction tests on Human benchmark!",
    )
parser.add_argument("test_type", choices=SUPPORTED_TESTS)
parser.add_argument("-l", "--loop", action="store_true")
test_type = parser.parse_args().test_type
loop = parser.parse_args().loop


def main():
    if test_type == "reaction":
        print("Starting Reaction Time")
        reaction.start(loop)

    elif test_type == "aim":
        print("Starting Aim Trainer")
        aim.start(loop)


if __name__ == "__main__":
    print("""
Welcome! Please make sure you have https://humanbenchmark.com/tests/reactiontime opened.

This program will run until either:
1. The test is over. (unless otherwise specified using --loop)
2. Your cursor goes to one of the 4 corners of your screen.

IMPORTANT: 
Using --loop is NOT recommended.
Do not leave it running for too long or it *might* lag your device.
""")
    
    print("Starting in 3 seconds...")
    time.sleep(3)

    main()


print("Program Ended")