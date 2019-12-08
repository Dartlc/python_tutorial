main_dict = {}
sub_dict = {}
seperate_dict = {}
for i in range(10, 12):
    sub_dict = {}
    class_name = input("Enter the class name: ")
    roll_number = input("Enter the roll number: ")
    sub_dict[class_name] = eval(input("Enter your section name: "))
    sub_dict[roll_number] = eval((input("Enter your roll_number: ")))
    seperate_dict = sub_dict
print(seperate_dict)

