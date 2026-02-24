for d in '0123456789abcdefgh':
    s = int(f'143{d}4', 18) + int(f'1{d}315',18)
    if s % 17 == 0:
        print(s // 17)