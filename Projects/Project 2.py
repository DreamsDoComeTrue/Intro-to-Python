def main():
    preslist = []
    infile = open("USPres.txt", 'r')
    for line in infile:
        preslist.append(line.replace('\n', ''))
    print('Number of lines read: ' + str(len(preslist)))
    find = findPres(preslist)


def findPres(preslist):

    begin = input("Enter starting point: ")
    end = input("Enter ending point: ")
    for x in range(int(begin), int(end)):
        print(preslist[x])


if __name__ == "__main__":
        main()
