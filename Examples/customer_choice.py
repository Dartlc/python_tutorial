"""dic = {}
print("1. Yes")
print("2. No")
choice = int(input("Enter you choice above we given: "))
n = 0
if choice == 1:
    while n <= 5:
        product = input("Enter the item: ")
        dic[product] = eval(input("Enter your price: "))
        n += 1
    print(dic)
elif choice == 2:
    print("Thanks for coming")
else:
    print("Invalid input")"""


dic_1 = {}
print("1. Yes")
print("2. No")
choice_1 = int(input("Enter you choice above we given: "))
if choice_1 == 1:
    while choice_1 == 1:
        product = input("Enter the item: ")
        dic_1[product] = eval(input("Enter your price: "))
        choice_1 = int(input("Enter you choice above we given: "))
    print(dic_1)
elif choice_1 == 2:
    print("Thanks for coming")
else:
    print("Invalid input")

product_name = input("Enter product name: ")
if product_name in dic_1.keys():
    print("The price is: ", dic_1[product_name])
else:
    print("The product is not found..")
