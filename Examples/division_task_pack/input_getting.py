def get_integer_input():
    global input_1
    while True:
        try:
            input_1 = int(input("Enter the 'range': "))
        except Exception as e:
            print(f"error: {e}")
            continue
        else:
            break
    return input_1
