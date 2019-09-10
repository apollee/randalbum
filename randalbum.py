import sys
import random

def random_number():
    return random.randrange(5)

def getline(number_line):
    fp = open("test")
    lines = fp.readlines()
    return lines[number_line]

def filtrate_line(line):
    final_line = line.split('(')[0]
    print(final_line)

def running():
    number_line = random_number()
    line = getline(number_line)
    if(line[0] == '#'):
        running()
    else:
        print(number_line)
        filtrate_line(line)

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '-i':
            print("missing")
        elif sys.argv[1] == '-h':
            print("Help missing.")
        else:
            print("Error: command invalid. Use -h for help.")
    else:
        print("Running normally")
        running()

main()