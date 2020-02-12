import math
def main():

    primes = []
    count = 2
    index = 0

    while True:
        isprime = True
        for x in range(2, count):#int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                continue
        if isprime:
            primes.append(count)
            print(index, primes[index])
            index += 1
        count += 1

if __name__ == "__main__":
    main()
