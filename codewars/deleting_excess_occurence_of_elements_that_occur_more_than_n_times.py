numbers = [1,1,3,3,7,2,2,2,2]
numbers.reverse()
occur = 3

def delete_nth(numbers, occur):
    for item in set(numbers):
        if numbers.count(item) > occur:
            for number in range(numbers.count(item) - occur):
                numbers.remove(item)

    numbers.reverse()
    print(numbers)