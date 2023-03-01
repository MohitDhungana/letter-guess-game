import random

MAX_CHANCES = 6

MAX_ALPHABETS_SELECTED = 3
ALPHABETS = ["Z", "X", "C", "V", "B", "N", "M"]


def get_goal_alphabets():
    return random.choices(ALPHABETS, k=MAX_ALPHABETS_SELECTED)


selected_alphabets = get_goal_alphabets()

# remove this at the end
# selected_alphabets = ["Z", "X", "C"]

print(f"selected_alphabets={ALPHABETS}")


def get_inputs():
    inputs = input(
        f"Enter {MAX_ALPHABETS_SELECTED} letters separated by space: "
    ).upper()

    user_input_list = inputs.split(" ")
    return user_input_list


for i in range(1, MAX_CHANCES + 1):

    correct_position = 0
    correct_letter = 0

    user_input = get_inputs()
    print(f"user_input {user_input}")

    for game_alphabet, user_alphabet in zip(selected_alphabets, user_input):
        # print(f"{game_alphabet=}, {user_alphabet=}")

        if user_alphabet == game_alphabet:
            correct_position += 1
        elif user_alphabet in selected_alphabets:
            correct_letter += 1

    print(f"Correct position = {correct_position}")
    print(f"Correct letter = {correct_letter}")

    if correct_position == MAX_ALPHABETS_SELECTED:
        print("Congratulations!!! You guessed correct.")
        print(f"It took you {i} tries to get it right")
        break
    elif i == MAX_CHANCES:
        print("Game Over!!! Better luck next time.")
        break

    print(f"You have {MAX_CHANCES-i} chances left!!!")
