from art import logo
import random
print(logo)

#creating initial words and dialogs
print("I'm thinking of a number between 1 and 100.")
#generating random number 
comp_number = random.randint(0,100)
#print(comp_number)
#choice of hard and easy level
choose_diff = input("Choose a difficulty. Typec'easy' or 'hard': ")
#for easy
if choose_diff == "easy":
    print("You have 10 attemps remaining to guess the number.")
    attemps_easy = 10
    ans_not_right = True
    while ans_not_right:
        if attemps_easy > 0:
            user_ans = int(input("Make a guess: "))
        elif attemps_easy <=0:
            ans_not_right = False
            print("You have lose all attemps, you lose.")
        if user_ans > comp_number and attemps_easy > 0:
            attemps_easy -= 1
            print("To high.")
            print("Guess again.")
            print(f"You have {attemps_easy} attemps remaining to guess the number.\n")
        elif user_ans < comp_number and attemps_easy > 0:
            attemps_easy -= 1
            print("To low.")
            print("Guess again.")
            print(f"You have {attemps_easy} attemps remaining to guess the number.\n")
        elif user_ans == comp_number and attemps_easy > 0:
            ans_not_right = False
            print(f"You guess the right number {user_ans}, you Won. ")

#for hard
elif choose_diff == "hard":
    print("You have 5 attemps remaining to guess the number.")
    attemps_hard = 5
    ans_not_right = True
    while ans_not_right:
        if attemps_hard > 0:
            user_ans = int(input("Make a guess: "))
        elif attemps_hard <=0:
            ans_not_right = False
            print("You have lose all attemps, you lose.")
        if user_ans > comp_number and attemps_hard > 0:
            attemps_hard -= 1
            print("To high.")
            print("Guess again.")
            print(f"You have {attemps_hard} attemps remaining to guess the number.\n")
        elif user_ans < comp_number and attemps_hard > 0:
            attemps_hard -= 1
            print("To low.")
            print("Guess again.")
            print(f"You have {attemps_hard} attemps remaining to guess the number.\n")
        elif user_ans == comp_number and attemps_hard > 0:
            ans_not_right = False
            print(f"You guess the right number {user_ans}, you Won. ")
        
