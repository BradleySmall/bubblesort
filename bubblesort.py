import random

MAX = 10
random_list = random.sample(range(MAX), MAX)


def main():
    print random_list
    pass_no = 0
    done = False
    while not done:
        pass_no += 1
        idx = 0
        swapped = False
        value = random_list[idx]
        for current in range(MAX):
            if value > random_list[current]:
                tmp = random_list[idx]
                random_list[idx] = random_list[current]
                random_list[current] = tmp

                idx = current
                value = random_list[idx]
                
                swapped = True
            else:
                idx = current
                value = random_list[idx]

        if not swapped:
            done = True
        else:
            print random_list, pass_no


if __name__=="__main__":
    main()

