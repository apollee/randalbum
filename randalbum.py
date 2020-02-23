import sys
import asyncio
import random
import spotify

client = spotify.Client('e05eaa83adef40d880e370a1c0685e53', 'f5e057bbed864fdeb793bf725d23a3f3')

async def research_album(album):
    results = await client.search(album, types=["artist", "album"])
    print(results.albums[0])

#to be implemented
def arguments():
    if  3 >= len(sys.argv) > 2:
        if sys.argv[1] == '-i':
            finished_album(int(sys.argv[2]))
        elif sys.argv[1] == '-r':
            remove_listened(int(sys.argv[2]))
        else:
            print("Error: command invalid. Use -h for help.")
    elif 2 >= len(sys.argv) > 1:
        if sys.argv[1] == '-h':
            print("Help missing.")
        else:
            print("Error: command invalid. Use -h for help.")
    else:
        print("Running normally")
        running()


def remove_listened(number):
    if not check_album_existence(number, "listened"):
        print("The number of the album does not exist.\nFinishing.")
        return
    with open("listened", "r") as fp:
        lines = fp.readlines()
    with open("listened", "w") as fp:
        for line in lines:
            if line.strip() != lines[number]:
                fp.write(line)


def random_number():
    return random.randint(0,12) #1-1001


def album_by_number(number):
    fp = open("test")
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
    if not check_album_existence(number, "test"):
        print("The number of the album does not exist.\nFinishing.")
        return
    if album_been_listened(number):
        print("Album has already been listened before.\nFinishing.")
    else:
        fp = open("listened", "a")
        fp.write(album_by_number(number))
        print("The album was added to the listened list.\nFinishing.")
        fp.close()


def album_been_listened(number_line):
    fp = open("test")
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
        #number: album without newline
        print(str(number_line) + ": " + album) 


def main():
    arguments()
    asyncio.get_event_loop().run_until_complete(research_album("21 - Adele"))

main()