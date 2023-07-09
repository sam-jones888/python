def sum_multiples(n):
    if n < 0:
        return 0
    total_sum = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum

print(sum_multiples(10))
