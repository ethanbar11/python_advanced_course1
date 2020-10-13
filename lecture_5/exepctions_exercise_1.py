def get_num():
    while True:
        num = input('Please enter a number: ')
        try:
            num_as_int = float(num)
            if num_as_int > 10000 or num_as_int < 0:
                raise ValueError()
            return num_as_int
        except Exception:
            pass


print(get_num())
