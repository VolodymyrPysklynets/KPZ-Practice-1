import lab2
def test_prime_num_generator():
    generator = lab3.prime_num_generator()
    counter = 0

    for i in range(0, 101):
        num = next(generator)
        if (i == 2 or i % 2 != 0) and (i == 3 or i % 3 != 0) and (i == 5 or i % 5 != 0) and (i == 7 or i % 7 != 0) and counter < 12:
            assert num == i
            counter += 1
        if i == 101:
            assert num == 101
