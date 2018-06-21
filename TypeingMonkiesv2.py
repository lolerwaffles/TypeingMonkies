import random, string, multiprocessing

print('We\'ve all heard that a million monkeys banging on a million typewriters will eventually reproduce the entire works of Shakespeare. Now, thanks to the Internet, we know this is not true.\n\n')

lookFor = input("What word or phrase would you like the monkey to look for?\n")
found = 1

while found != 0:
    for i in range(len(lookFor)):
        looking = ''
        looking = looking + random.choice(string.ascii_letters)
        print("The Monkey has tried {} random words.".format(found), end="\r")
    found += 1
    if looking == lookFor:
        print("The monkey found what you were looking for after {} random words!".format(found))
        found = 0
