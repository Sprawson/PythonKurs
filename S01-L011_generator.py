# Write a Python program that creates a generator function that generates all prime numbers between two given number.

a = int(input("Input a starting number: "))
b = int(input("Input a ending number: "))


def generate_prime_number(start,end):
    for n in range(start, end):
        if is_prime(n):
            yield n
def is_prime(n):
    if n < 2:
        return False
    if n in [2, 3, 5, 7]:
        return True
    for i in range(2, 10):
        if n % i == 0:
            return False
    return True

prime_generator = generate_prime_number(a,b)

print(next(prime_generator))

for prime in prime_generator:
    print(prime)