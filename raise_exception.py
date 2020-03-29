import re


class MobileNumberFormatException(Exception):
    """
      class sending message mobile number format is invalid
    """

    def __init__(self, value):
        self.error_message = value

    def __str__(self):
        return self.error_message


def valid_mobile_number(mob_num: str):
    pattern = re.compile("^[6-9]\d{9}$")
    return pattern.match(mob_num)


def get_mobile_number():
    mob_num = input("Enter the mobile number: ")
    if valid_mobile_number(mob_num=mob_num):
        print("Mobile number is valid..")
    else:
        while True:
            try:
                raise MobileNumberFormatException("The given mobile is invalid....")
            except Exception as e:
                print(e)
                get_mobile_number()
                break


get_mobile_number()
