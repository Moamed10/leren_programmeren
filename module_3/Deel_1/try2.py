def gulden(n):
    # Check for cases where n is 0 or 1
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    # Initialize the sequence with the first two Fibonacci numbers
    getal = [0, 1]
    for x in range(2, n):
        volgend_getal = getal[-1] + getal[-2]
        getal.append(volgend_getal)
    return getal


def calculate_golden_ratio(fibonacci_sequence):

    if len(fibonacci_sequence) < 2:
        return None
    
    return fibonacci_sequence[-1] / fibonacci_sequence[-2]

print(gulden(7))
print(calculate_golden_ratio)
