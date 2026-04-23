def tobase(n:int,base:int) -> str:
    ''' Эта функция переводит число из 10 системы в нужную'''
    if n==0:
        return "0"
    result=''
    while n>0:
        res=n%base
        result=str(res)+result
        n=n//base
    return result
print(tobase(10,10))

def convert_to_base(n, base):
    """Переводит число n в систему счисления с основанием base и возвращает строку с записью числа."""
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n = n // base
    return ''.join(reversed(digits))

def find_bases_with_ending(number, ending):
    """
    Находит все основания систем счисления (>=4), в которых запись number оканчивается на ending.
    Возвращает отсортированный список оснований.
    """
    bases = []
    # Минимальное основание — 4 (так как в записи есть цифра 3)
    for base in range(4, number + 20):  # Берём с запасом: number + 20
        # Переводим число в заданное основание
        num_in_base = convert_to_base(number, base)
        # Проверяем, оканчивается ли запись на нужное окончание
        if num_in_base.endswith(ending):
            bases.append(base)
    return sorted(bases)

# Исходные данные
number = 63
ending = "23"

# Находим подходящие основания
result_bases = find_bases_with_ending(number, ending)

# Выводим результат
print(f"Основания систем счисления, в которых запись числа {number} оканчивается на '{ending}':")
print(', '.join(map(str, result_bases)))
