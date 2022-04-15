def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if not number % prime:
                break
        else:
            prime_numbers.append(number)
            yield number
            
for number in prime_numbers_generator(20):
    print(number)
