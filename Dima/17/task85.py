
count = 0
max_num = 0

for i in range(1111, 10000):
    digits = [int(d) for d in str(i)]
    s = sum(digits)
    p = 1
    for d in digits:
        p *= d

    try:
        # Проверяем делимость на сумму и произведение цифр
        if i % s == 0 and i % p == 0:
            count += 1
            if i > max_num:
                max_num = i
    except Exception as e:
        # Если p == 0 (произведение цифр нулевое), пропускаем число
        print(e)
        continue

print(count, max_num)