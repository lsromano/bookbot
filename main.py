from stats import *
import sys

print(sys.argv)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


main(sys.argv[1])

