def automaton(n):
    bin_str = bin(n)[2:]
    reversed_bin = bin_str[::-1]
    reversed_bin_stripped = reversed_bin.lstrip('0')
    if reversed_bin_stripped == '':
        return 0
    return int(reversed_bin_stripped, 2)

max_n = 0
for n in range(1, 101):
    if automaton(n) == 7:
        if n > max_n:
            max_n = n

print("Наибольшее N ≤ 100, дающее 7:", max_n)