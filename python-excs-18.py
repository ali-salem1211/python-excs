def simple_statistics(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    above_average = [n for n in numbers if n > average]

    print("Sum:", total)
    print("Average:", average)
    print("Numbers above average:", len(above_average))

simple_statistics([3, 7, 10, 2, 5])
