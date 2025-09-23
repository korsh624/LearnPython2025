def find_numbers(target):
    results = []
    for num in range(1000, 10000):
        digits = [int(d) for d in str(num)]
        s1 = digits[0] + digits[1]
        s2 = digits[1] + digits[2]
        s3 = digits[2] + digits[3]
        sums = [s1, s2, s3]
        min_sum = min(sums)# Удаляем минимальную сумму
        sums.remove(min_sum)
        sums.sort()
        if sums == [5, 11]:
            results.append(num)
    return min(results), max(results)

min_num, max_num = find_numbers(511)
print(f"Наименьшее число: {min_num}")
print(f"Наибольшее число: {max_num}")