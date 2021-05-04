import random


class RockPaperScissors:

    def __init__(self, choice):
        self.choice = choice
        self.data_players = {}
        self.winning_cases = {
            'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
            'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
            'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
            'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
            'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
            'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
            'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
            'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
            'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
            'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
            'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
            'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
            'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
            'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
            'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
        }
        self.default_params_for_user = {
            "paper": "rock",
            "rock": "scissors",
            "scissors": "paper"
        }
        self.options_not_empty = {}
        self.user_count_who_not_in_db = 0

    def user_choice(self):
        if self.choice == "I want to play":
            return self.main()
        return self.game_failure()

    def main(self):

        file = open("rating.txt", "r", encoding="utf-8")
        for name_and_score in file.readlines():
            data = name_and_score.replace("\n", "").split(" ")
            self.data_players[data[0]] = int(data[1])
        return self.game()

    def game(self):

        user_name = input("Enter your name>> ")
        print(f"Hello, {user_name}")
        select_params_for_user = input("Please. input: "
                                       "rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,"
                                       "snake,scissors,fire or press enter(you will play with default params)>>")

        # rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire
        ready_made_parameters_for_players = select_params_for_user.split(",")

        print("Okay, let's start")
        while True:
            user_try = random.randint(0, 3)
            computer_try = random.randint(0, 3)

            user_choice = input("Enter your choice>> ")

            if user_choice in self.winning_cases:

                if "".join(ready_made_parameters_for_players) != "":

                    for elem in self.winning_cases:
                        if elem in ready_made_parameters_for_players:
                            self.options_not_empty[elem] = [i for i in self.winning_cases[elem]
                                                            if i in ready_made_parameters_for_players]

                    if user_try > computer_try:

                        random_winning_val_for_user = self.options_not_empty[user_choice][
                            random.randint(0, len(self.options_not_empty[user_choice]) - 1)]

                        print(f"Well done. The computer chose {random_winning_val_for_user} and failed")
                        if user_name in self.data_players:

                            self.data_players[user_name] += 100
                        else:
                            self.user_count_who_not_in_db += 100

                    elif user_try < computer_try:
                        random_winning_val_for_comp = [key for key in self.options_not_empty
                                                       if user_choice in self.options_not_empty[key]]

                        print(f"Sorry, but the computer chose "
                              f"{random_winning_val_for_comp[random.randint(0, len(random_winning_val_for_comp) - 1)]}")

                    elif user_try == computer_try:
                        print(f"There is a draw ({user_choice})")
                        if user_name in self.data_players:

                            self.data_players[user_name] += 50
                        else:
                            self.user_count_who_not_in_db += 50

                else:

                    if user_try > computer_try:
                        print(f"Well done. The computer chose {self.default_params_for_user[user_choice]} and failed")
                        if user_name in self.data_players:

                            self.data_players[user_name] += 100
                        else:
                            self.user_count_who_not_in_db += 100
                    elif user_try < computer_try:
                        print(f"Sorry, but "
                              f"the computer"
                              f" chose "
                              f""
        f"{''.join([key for key in self.default_params_for_user if self.default_params_for_user[key] == user_choice])}")

                    elif user_try == computer_try:
                        print(f"There is a draw ({user_choice})")
                        if user_name in self.data_players:

                            self.data_players[user_name] += 50
                        else:
                            self.user_count_who_not_in_db += 50

            elif user_choice == "!rating":
                if user_name in self.data_players:
                    print(f"Your rating: {self.data_players[user_name]}")
                else:
                    print(f"Your rating: {self.user_count_who_not_in_db}")

            elif user_choice == "!exit":
                print("Bye!")
                break
            else:
                print("Invalid input")

    def game_failure(self):
        return "Dude, play next time!"


ben = RockPaperScissors("I want to pl2ay")
# rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire
print(ben.user_choice())
