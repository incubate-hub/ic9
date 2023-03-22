def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    """
    total_sum = 0
    for number in numbers:
        total_sum += number
    average = total_sum / len(numbers)
    return average
    
numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print("The average of the numbers is: " + average)
