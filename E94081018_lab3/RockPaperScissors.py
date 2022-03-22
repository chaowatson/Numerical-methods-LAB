import random


class RockPaperScissors:
    def __init__(self):
        self.lose_counter = 0  # 歸零計數器
        self.tie_counter = 0  # 歸零計數器
        self.win_counter = 0

    def play(self):
        while True:
            print("Welcome to ROCK, PAPER, SCISSORS game!")
            player_choice = input("Enter your move: (r)ock (p)apaer (s)cissors ")  # 讀取玩家選擇
            available_choices = ["ROCK", "PAPER", "SCISSORS"]
            bot_choice = random.choice(available_choices)  # 產生ai選擇

            # 玩家出剪刀的情況
            if player_choice == "r":
                print("ROCK versus...")
                print(bot_choice)
                if bot_choice == "PAPER":
                    print("You lose!")
                    self.lose_counter = self.lose_counter + 1  # 玩家輸，計數加一
                elif bot_choice == "ROCK":
                    print("It is a tie!")
                    self.tie_counter = self.tie_counter + 1  # 平手，計數加一
                elif bot_choice == "SCISSORS":
                    print("You win!")
                    self.win_counter = self.win_counter + 1
                    print(f"You have {self.tie_counter} ties and {self.lose_counter} losses and {self.win_counter} wins")
                    break  # 玩家贏，印出結果，跳出迴圈

            # 玩家出布的情況
            elif player_choice == "p":
                print("PAPER versus...")
                print(bot_choice)
                if bot_choice == "SCISSORS":
                    print("You lose!")
                    self.lose_counter = self.lose_counter + 1
                elif bot_choice == "PAPER":
                    print("It is a tie!")
                    self.tie_counter = self.tie_counter + 1
                elif bot_choice == "ROCK":
                    print("You win!")
                    self.win_counter = self.win_counter + 1
                    print(f"You have {self.tie_counter} ties and {self.lose_counter} losses and {self.win_counter} wins")

                    break

            # 玩家出石頭的情況
            elif player_choice == "s":
                print("SCISSORS versus...")
                print(bot_choice)
                if bot_choice == "ROCK":
                    print("You lose!")
                    self.lose_counter = self.lose_counter + 1
                elif bot_choice == "SCISSORS":
                    print("It is a tie!")
                    self.tie_counter = self.tie_counter + 1
                elif bot_choice == "PAPER":
                    print("You win!")
                    self.win_counter = self.win_counter + 1
                    print(f"You have {self.tie_counter} ties and {self.lose_counter} losses and {self.win_counter} wins")

                    break


game = RockPaperScissors()
game.play()