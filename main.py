import sys


def sieve_of_eratosthenes(n):
    if not isinstance(n, int) or n < 2:
        return [-1]
    if n == 2:
        return [False, False, True]

    primes = [True] * (n + 1)

    #   0 and 1 are not prime, set them to false
    primes[0] = False
    primes[1] = False

    p = 2
    #   Since you're checking all multiples, we really only need to loop up to square root of n
    while p ** 2 <= n:
        if primes[p]:
            #   All multiples of p are composite, set to false
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1

    return primes


def primes_to_n(n):
    if not isinstance(n, int) or n < 2:
        return [-1]
    if n == 2:
        return [2]

    prime_numbers = sieve_of_eratosthenes(n)

    primes = []

    for i in range(n + 1):
        if prime_numbers[i]:
            primes.append(i)

    return primes


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) < 2:
        # Positive test cases
        print("Calculating for 10")
        print(primes_to_n(10))
        print("Calculating for 100")
        print(primes_to_n(100))
        print("Calculating for 100000")
        print(primes_to_n(100000))
        
        # Negative test cases, all should return [-1]
        print("Calculating for a")
        print(primes_to_n("a"))
        print("Calculating for 0")
        print(primes_to_n(0))
        print("Calculating for 1")
        print(primes_to_n(1))
    else:
        try:
            n_input = int(sys.argv[1])

            print('Calculating for', sys.argv[1])
            print(primes_to_n(int(sys.argv[1])))
        except ValueError:
            print('Please provide an integer value.')
