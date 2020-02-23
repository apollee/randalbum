import sys
import asyncio
import random
import spotify
import time
import warnings
from subprocess import call

client = spotify.Client('e05eaa83adef40d880e370a1c0685e53', 'f5e057bbed864fdeb793bf725d23a3f3')

async def research_album(album):
    results = await client.search(album, types=["artist", "album"])
    album = await client.get_album(str(results.albums[0]))
    all_tracks = await album.get_all_tracks()
    call(["spotify", "--uri=" + str(all_tracks[0]) + "#0:0.01"])

async def f():
    asyncio.get_running_loop().set_exception_handler(lambda loop, context: None)

def help_menu():
    print(" ____   ____ ____  ___    ____ _     ____  __ __ ___ ___ \n|    \ /    |    \|   \  /    | |   |    \|  |  |   |   |\n|  D  |  o  |  _  |    \|  o  | |   |  o  |  |  | _   _ |\n|    /|     |  |  |  D  |     | |___|     |  |  |  \_/  |\n|    \|  _  |  |  |     |  _  |     |  O  |  :  |   |   |\n|  .  |  |  |  |  |     |  |  |     |     |     |   |   |\n|__|\_|__|__|__|__|_____|__|__|_____|_____|\__,_|___|___|")                  
    print("\nUsage: python3 randalbum.py [OPTION...]")
    print("\n OPTIONS:")
    print("\n -l num    Use this to define the album with the number=num as a listened album")
    print("\n -r num    Use this to remove the album with the number=num from the listened albums")
    print("\n -h        Use this to access the help page")
    print("\n If no option is provided the program will run as supposed to.\n")


#to be implemented
def arguments():
    if  3 >= len(sys.argv) > 2:
        if sys.argv[1] == '-l':
            finished_album(int(sys.argv[2]))
        elif sys.argv[1] == '-r':
            remove_listened(int(sys.argv[2]))
        else:
            print("Error: command invalid. Use -h for help.")
    elif 2 >= len(sys.argv) > 1:
        if sys.argv[1] == '-h':
            help_menu()
        else:
            print("Error: command invalid. Use -h for help.")
    else:
        print(" ____   ____ ____  ___    ____ _     ____  __ __ ___ ___ \n|    \ /    |    \|   \  /    | |   |    \|  |  |   |   |\n|  D  |  o  |  _  |    \|  o  | |   |  o  |  |  | _   _ |\n|    /|     |  |  |  D  |     | |___|     |  |  |  \_/  |\n|    \|  _  |  |  |     |  _  |     |  O  |  :  |   |   |\n|  .  |  |  |  |  |     |  |  |     |     |     |   |   |\n|__|\_|__|__|__|__|_____|__|__|_____|_____|\__,_|___|___|")                  
        print("\n")
        running()


def remove_listened(number):
    if not check_album_existence(number, "original"):
        print("The number of the album does not exist.\nFinishing.")
        return
    with open("listened", "r") as fp:
        lines = fp.readlines()
    with open("listened", "w") as fp:
        for line in lines:
            if line != album_by_number(number):
                fp.write(line)


def random_number():
    return random.randint(0,1000) #1-1001


def album_by_number(number):
    fp = open("original")
    lines = fp.readlines()
    fp.close()
    return lines[number]

def check_album_existence(n_album, file_name): 
    with open(file_name) as fp:
        size = len([0 for _ in fp])
    if n_album < size:
        fp.close()
        return True
    fp.close()
    return False


def finished_album(number):
    if not check_album_existence(number, "original"):
        print("Error: The number of the album does not exist.\nFinishing.")
        return
    if album_been_listened(number):
        print("Error: Album has already been listened before.\nFinishing.")
    else:
        fp = open("listened", "a")
        fp.write(album_by_number(number))
        print("Success: The album was added to the listened list.\nFinishing.")
        fp.close()


def album_been_listened(number_line):
    fp = open("original")
    lines = fp.readlines()
    fp.close()
    album = lines[number_line]
    fp_listened = open("listened")
    if album in fp_listened.read():
        fp_listened.close()
        return True
    fp_listened.close()
    return False    


def running():
    number_line = random_number()
    album = album_by_number(number_line).rstrip() #string
    if(album_been_listened(number_line)):
        running()
    else:
        print("The choosen album is:\n")
        print(str(number_line) + ": " + album)
        print("\nLeave the terminal open or else spotify will close. Use -h if you need help.\n") 

        asyncio.get_event_loop().run_until_complete(research_album(album))


def main():
    sys.tracebacklimit = 0 #to suppress the traceback warnings
    asyncio.get_event_loop().run_until_complete(f()) #to suppress the warnings from aiohttp
    arguments()

main()