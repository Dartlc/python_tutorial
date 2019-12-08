main_dict = {}
for i in range(10, 12):
    sub_set = set()
    name = input("Enter the student name: ")
    class_name = input("Enter the class name: ")
    roll_number = int(input("Enter the roll number: "))
    sub_set.add(class_name)
    sub_set.add(roll_number)
    main_dict[name] = sub_set
    print(main_dict)
