#!/usr/bin/python3
"""Program to demonstrate the bubble sort in python."""
import random


MAX = 10


def main():
    """Demonstrate a bubble sort.

    * Create the random list.
    * Print.
    * Sort.
    * Output.
    """
    # This is an already sorted list
    # random_list = range(MAX)

    # This is a reverse sorted list
    # random_list = range(MAX-1,-1, -1)

    # This is a randomly unsorted list
    random_list = random.sample(range(MAX), MAX)

    print(random_list)
    passes = list_bubblesort(random_list)
    print(random_list)
    print("Completed in %d pass%s." % (passes, "es" if passes != 1 else ""))


def swap(the_list, src_idx, dst_idx):
    """Swap two values in a list."""
    the_list[dst_idx], the_list[src_idx] = the_list[src_idx], the_list[dst_idx]


def list_bubblesort(the_list):
    """Sort a list.

    Trackhow many passes.

    Start from the first item in the list.
    Walk the list until it can be swapped with a lower value or switch
    to the larger value and continue down the list.

    Loop back to the first item in the list.

    When list is passed with no swaps, it is sorted.

    Return the number of passes.
    """
    pass_no = 0
    done = False
    while not done:
        swapped = False
        for next_one, _ in enumerate(the_list[1:]):
            current = next_one - 1
            value = the_list[current]
            if value > the_list[next_one]:
                swap(the_list, current, next_one)
                swapped = True

        if not swapped:
            done = True
        else:
            pass_no += 1
            print(the_list, pass_no)

    return pass_no


if __name__ == "__main__":
    main()
