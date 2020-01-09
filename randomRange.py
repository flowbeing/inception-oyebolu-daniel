import random


def generate_num_from_range(minimum, maximum):
    print((random.random() * (maximum - minimum)) + minimum)


generate_num_from_range(5, 10)
