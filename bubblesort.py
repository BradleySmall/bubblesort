import random

MAX = 10

def main():
    """
    main driver. creates the random list, then prints it, then calls 
    the sort function, outputs the sorted list.
    """
    random_list = random.sample(range(MAX), MAX)

    print random_list
    passes = list_bubblesort(random_list)
    print random_list
    print "Completed in %d pass%s." % (passes, "es" if 1 != passes else "") 

def list_bubblesort(theList):
    """
    classic bubble sort
    tracking how many passes

    starting from the first item in the list
    walk the list until it can be swapped with a lower value or switch 
    to the larger value and continue down the list

    loop back to the first item in the list

    when list is passed with no swaps, it is sorted.
    returns the number of passes.
    """
    pass_no = 0
    done = False
    while not done:
        idx = 0
        swapped = False
        value = theList[idx]
        for current in range(MAX):
            if value > theList[current]:
                tmp = theList[idx]
                theList[idx] = theList[current]
                theList[current] = tmp

                idx = current
                value = theList[idx]
                
                swapped = True
            else:
                idx = current
                value = theList[idx]

        if not swapped:
            done = True
        else:
            pass_no += 1
            print theList, pass_no
    return pass_no

if __name__=="__main__":
    main()

