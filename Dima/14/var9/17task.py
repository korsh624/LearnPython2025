for d in '0123456789abcdefg':
    s = int(f'1C3{d}6', 17)+  int(f'1{d}2{d}', 17)
    if s % 19 == 0:
        print(s // 19)