import random, string, multiprocessing

def startUp():
    print('We\'ve all heard that a million monkeys banging on a million typewriters will eventually reproduce the entire works of Shakespeare. Now, thanks to the Internet, we know this is not true.\n\n')
    lookFor = input("What word or phrase would you like the monkey to look for?\n")
    found = 1
    return found,lookFor

def monkey(found, lookFor):
    if found ==  1:
        looking = '0'
    looking = looking + random.choice(string.ascii_letters)
    print("The Monkey has mashed {} keys on the keyboard.".format(found), end="\r")
    if len(looking) > len(lookFor):
        looking = looking[1:]
    found += 1
    return looking,found



if __name__ == '__main__':
    found, lookFor = startUp()
    while found != 0:
        jobs = []
        for i in range(5):
            found = []
            if jobs[:-1] == lookFor:
                print("The monkey found what you were looking for after mashing {} keys on his keyboard!".format(found))
                found = 0
                break
            p = multiprocessing.Process(target=monkey ,args=((found, lookFor)))
            jobs.append(p)
            p.start()

            p.join()
