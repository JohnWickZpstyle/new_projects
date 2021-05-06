import random


class CardAnatomy:
    def __init__(self):
        self.__accounts = {}
        self.__converted_list_of_numbers = []
        self.__last_digit_card = 0
        self.__card_number_sum = 0
        self.choice = 0
        self.__balance = 0
        self.exit_point = False
        self.__function_selection = 0


    def main_menu(self):
        print("""
1. Create an account
2. Log into account
0. Exit""")
        self.choice = int(input(""))
        return self.user_choice()


    def __create_card(self):
        while True:
            random.seed(random.randint(0, 5000))
            card = 4000000000000000 + random.randint(0000000000, 9999999999)
            pin = (random.randint(0, 9999))
            pin = str(pin).zfill(4)

            self.__converted_list_of_numbers = list(map(int, list(str(card))))[::-1]
            self.__last_digit_card, self.__card_number_sum = 0, 0

            for num in range(0, len(self.__converted_list_of_numbers)):
                if not num == 0:
                    if num % 2 != 0:
                        self.__card_number_sum += self.__converted_list_of_numbers[num] * 2 - 9 \
                            if self.__converted_list_of_numbers[num] * 2 > 9 else\
                            self.__converted_list_of_numbers[num] * 2
                    else:
                        self.__card_number_sum += self.__converted_list_of_numbers[num]
                else:
                    self.__last_digit_card = self.__converted_list_of_numbers[num]

            if (self.__card_number_sum + self.__last_digit_card) % 10 == 0:
                self.__accounts[card] = int(pin)
                print(f"""
Your card has been created
Your card number:
{card}
Your card PIN:
{pin}""")
                return self.main_menu()
            else:
                continue



    def authorization(self):
        for _ in iter(int, 1):
            check_login = input("""
Enter your card number:
""")
            check_pin = input("""Enter your PIN:
""")
            if check_login.isdigit() and check_pin.isdigit():
                check_login = int(check_login)
                check_pin = int(check_pin)
                if self.__accounts.get(check_login) == check_pin:
                    print("""
You have successfully logged in!""")
                    self.__function_selection = self.user_account()
                else:
                    print("""
Wrong card number or PIN!""")
                    self.__function_selection = self.main_menu()
                return self.__function_selection
            else:
                continue


    def user_account(self):
        while not self.exit_point:
            print("""
1. Balance
2. Log out
0. Exit""")
            self.choice = int(input(" "))
            if self.choice == 1:
                print(f"""
Balance: {self.__balance}""")
                continue
            elif self.choice == 2:
                self.__function_selection = self.main_menu()
            elif self.choice == 0:
                self.exit_point = True
                self.__function_selection = self.exit_s_db()
        return self.__function_selection


    def user_choice(self):
        while not self.exit_point and self.choice in [0, 1, 2]:
            if self.choice == 1:
                self.__function_selection = self.__create_card()
            elif self.choice == 2:
                self.__function_selection = self.authorization()
            elif self.choice == 0:
                self.exit_point = True
                self.__function_selection = self.exit_s_db()
        return self.__function_selection


    def exit_s_db(self):
        return "Bye!"


ron = CardAnatomy()
print(ron.main_menu())
