import random, string, multiprocessing

print('We\'ve all heard that a million monkeys banging on a million typewriters will eventually reproduce the entire works of Shakespeare. Now, thanks to the Internet, we know this is not true.')

lookFor = input("What word or phrase would you like the monkey to look for?\n")
found = 1
looking = ''
while found != 0:
    looking = looking + random.choice(string.ascii_letters)
    print("The Monkey has mashed {} keys on the keyboard.".format(found), end="\r")
    if len(looking) > len(lookFor):
        looking = looking[1:]
    found += 1
    if looking == lookFor:
        print("The monkey found what you were looking for after mashing {} keys on his keyboard!".format(found))
        found = 0
