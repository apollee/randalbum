import sys
import random

#to be implemented
def arguments():
    if len(sys.argv) > 2:
        if sys.argv[1] == '-i':
            finished_album(sys.argv[2])
        else:
            print("Error: command invalid. Use -h for help.")
    elif len(sys.argv) > 1:
        if sys.argv[1] == '-h':
            print("Help missing.")
        else:
            print("Error: command invalid. Use -h for help.")
    else:
        print("Running normally")
        running()

def check_existence(album):
    fp = open("test")
    if album in fp.read():
        fp.close()
        return True
    fp.close()
    return False

def finished_album(album):
    if album_listened(album):
        print("Album has already been listened before.\nFinishing.")
    else:
        if(check_existence(album)):
            fp = open("listened", "a")
            fp.write(album)
            fp.close()
        else:
            print("Album does not exist.\n")

#checks in the listened file for the album
def album_listened(line):
    fp = open("listened")
    if line in fp.read():
        fp.close()
        return True
    fp.close()
    return False  

def random_number():
    return random.randint(0,12) #1-1001

#fetches all the lines in the entire list
def getline(number_line):
    fp = open("test")
    lines = fp.readlines()
    fp.close()
    return lines[number_line]

def running():
    number_line = random_number()
    line = getline(number_line).rstrip() #removes the newline created by readlines
    if(album_listened(line)):
        #print("No.\n")
        running()
    else:
        print(line)

def main():
    arguments()

main()