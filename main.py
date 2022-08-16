from tkinter import *
from PIL import ImageTk,Image
import random
import time


root = Tk()
root.title("AAAAAAAAA")


def guessing_game():
    word_list_animals = ["elephant", "snake", "giraffe", "cat", "dog", "bee", "mosquito", "turtle", "ant", "horse",
                         "squirrel", "bird", "hamster", "fish", "sheep", "lamb", "goose", "turkey", "rabbit",
                         "tiger", "monkey", "wolf", "fox", "bear", "deer", "camel", "rhino", "mouse", "shark",
                         "zebra", "hedgehog", "frog", "lizard", "crocodile", "penguin", "dolphin", "iguana",
                         "chicken", "cow", "bull", "goat", "pig", "lion", "whale", "kangaroo", "owl", "parrot",
                         "eagle", "dove", "seagull", "falcon", "swan", "cobra", "phyton", "donkey", "ostrich",
                         "pelican", "woodpecker", "ox", "hippopotamus", "rat", "badger", "leopard", "panda",
                         "cheetah", "octopus", "mussel", "crab", "lobster", "shrimp", "eel", "squid",
                         "worm", "butterfly", "caterpillar", "flea", "fly", "scorpion", "slug"]
    word_list_plants = ["acacia", "azalea", "begonia", "bergamot", "bush", "celosia", "daffodil", "jasmine",
                        "lilac", "lily", "lotus", "magnolia", "orchid", "poppy", "rose", "sunflower", "tulip",
                        "violet", "basil", "bracken", "brambles", "cactus", "cardamom", "chicory", "coriander",
                        "corn", "cumin", "dandelion", "fennel", "fern", "mushroom", "garlic", "ginger", "heather",
                        "herb", "ivy", "moss", "nettle", "parsley", "pimenta", "plantain", "rosemary", "thistle",
                        "vanilla", "wheat", "birch", "pine", "plane", "willow"]
    print("WELCOME TO THE WORD GUESSING GAME")
    print("---------------------------------")
    print("YOU HAVE 11 ATTEND TO GUESS")
    print("---------------------------")
    print("THE GAME STARTS WITH 1100 POINTS AND IF YOU MADE MISTAKE IT GETS DOWN 100 POINTS")
    print("--------------------------------------------------------------------------------")
    category_choice = input("Which category you want to compete in (Animal or Plant)? ")
    category_choice = category_choice.lower()

    all_words = word_list_animals.extend(word_list_plants)

    starting_point = 1100
    current_point = ""
    random_word = ""
    choice_limit = 5
    current_choice_number = 0
    guess = ""
    guess_limit = 11
    guess_count = 0
    continue_ask = ""
    attend_counter = 0
    category_ask = ""
    th_add = ""
    else_of_category_ask = ""
    else_limit_of_category_ask = 3
    else_of_category_ask_counter = 0
    else_of_continue_ask = ""
    else_limit_of_continue_ask = 3
    else_of_continue_ask_counter = 0

    if category_choice == "animal":
        random_word = random.choice(word_list_animals)
    elif category_choice == "plant":
        random_word = random.choice(word_list_plants)
    else:
        print("Choose Animal or Plant")
        current_choice_number += 1
        if current_choice_number < choice_limit:
            category_choice = input("Which category you want to compete in (Animal or Plant)? ")
            category_choice = category_choice.lower()
        else:
            exit()

    word_length = len(random_word)

    while guess_count < guess_limit:
        if guess == random_word:
            print("YOU WIN!")
            current_point = current_point + 500
            print(f"You made {current_point} points.")
            attend_counter += 1
            continue_ask = input("Do you want to compete with another word? (Y/N): ")
            continue_ask = continue_ask.lower()
            if continue_ask == "yes":
                guess_count = 0
                starting_point = current_point + 1000
                category_ask = input("Do you want to choose your category? (Y/N): ")
                category_ask = category_ask.lower()
                if category_ask == "yes":
                    category_choice = input("Which category do you want to compete in? (Animal or Plant): ")
                    category_choice = category_choice.lower()
                    if category_choice == "animal":
                        random_word = random.choice(word_list_animals)
                    elif category_choice == "plant":
                        random_word = random.choice(word_list_plants)
                    else:
                        print("Choose Animal or Plant")
                        current_choice_number += 1
                        if current_choice_number < choice_limit:
                            category_choice = input("Which category you want to compete in (Animal or Plant)? ")
                            category_choice = category_choice.lower()
                        else:
                            exit()

                elif category_ask == "no":
                    random_word = random.choice.__get__(all_words)
                    guess = input("Enter a guess: ")
                    guess_count += 1
                    print(f"You used {guess_count}. You have {guess_limit - guess_count}.")
                    while guess_count + 1:
                        current_point = starting_point - 100 * guess_count
                        print(f"You have {current_point}")
                        break
                        if guess_count == 3:
                            print(f"There are {word_length} letters in the word.")
                        elif guess_count == 7:
                            changing_the_word = input("Do you want to change the word? (Y/N): ")
                            changing_the_word = changing_the_word.lower()
                            if changing_the_word == "yes":
                                guess_count = 0
                                random_word = random.choice.__get__(all_words)
                                if random_word in word_list_animals:
                                    print("It is an animal")
                                else:
                                    print("It is a plant")
                            elif changing_the_word == "no":
                                continue
                            elif guess_count == 9:
                                counter_of_letter = 0
                                random_letter = ""
                                while counter_of_letter < len(random_word):
                                    letter_list = list(random_word[counter_of_letter])
                                    counter_of_letter += 1
                                    random_letter = random.choice(letter_list)
                                    if counter_of_letter == 1:
                                        th_add = "st"
                                    elif counter_of_letter == 2:
                                        th_add = "nd"
                                    elif counter_of_letter == 3:
                                        th_add = "rd"
                                    else:
                                        th_add = "th"
                                print(
                                    f"One of the letter is: {random_letter} and it is {counter_of_letter}{th_add} in the "
                                    f"word.")
                            else:
                                print("YOU LOSE!")
                                print(f"The word is {random_word}.")
                        else:
                            print("YES or NO.")
                            else_of_category_ask_counter += 1
                            if else_of_category_ask_counter < else_limit_of_category_ask:
                                else_of_category_ask = input("Choose: ")
                                else_of_category_ask = else_of_category_ask.lower()
                            else:
                                exit()
                elif continue_ask == "no":
                    print(f"Congratulations you made {current_point} from {attend_counter} attend.")
                    exit()
                else:
                    print("Choose YES or No.")
                    else_of_continue_ask_counter += 1
                    if else_of_category_ask_counter < else_limit_of_continue_ask:
                        else_of_continue_ask = input("Choose: ")
                        else_of_continue_ask = else_of_continue_ask.lower()
                    else:
                        exit()
        else:
            guess = input("Enter guess: ")
            guess_count += 1
            print(f"You used {guess_count}. You have {guess_limit - guess_count}.")
            while guess_count + 1:
                current_point = starting_point - 100 * guess_count
                print(f"You have {current_point}")
                break
            if guess_count == 3:
                print(f"There are {word_length} letters in the word.")
            elif guess_count == 7:
                changing_the_word = input("Do you want to change the word? (Y/N): ")
                changing_the_word = changing_the_word.lower()
                if changing_the_word == "yes":
                    guess_count = 0
                    random_word = random.choice.__get__(all_words)
                    if random_word in word_list_animals:
                        print("It is an animal.")
                    else:
                        print("It is a plant.")
                elif changing_the_word == "no":
                    continue

            elif guess_count == 9:
                counter_of_letter = 0
                random_letter = ""
                while counter_of_letter < len(random_word):
                    letter_list = list(random_word[counter_of_letter])
                    counter_of_letter += 1
                    random_letter = random.choice(letter_list)
                print(f"One of the letter is: {random_letter} and it is {counter_of_letter} in the word.")
        if guess_count == guess_limit and guess != random_word:
            print("Out of guesses, YOU LOSE!")
            print(f"The word is {random_word}")


def hangman_game():
    print("WELCOME TO HANGMAN GAME")
    print("-----------------------")
    name = input("Enter your name: ")
    print(f"Welcome, {name}. Best of luck!")
    time.sleep(1)
    print(f"Don't forget {name}, sometimes words have the same letter several times!!")
    time.sleep(2)
    print("----------------")
    print("The game starts!")
    print("----------------")
    time.sleep(2)

    def main_of_the_game():
        global count
        global display
        global word
        global already_guessed
        global length
        global play_game
        words_to_guess = ["computer", "programming", "electronics", "mouse", "temperature", "robot", "phone", "smart",
                          "motor", "facebook", "machine", "sadness", "television", "coffee", "button", "curtain",
                          "plane",
                          "light", "electric", "copper", "silver", "bottle", "picture", "lotion", "shampoo", "chain",
                          "religion", "chair", "jacket", "radio", "cable", "internet", "bicycle", "money"]
        word = random.choice(words_to_guess)
        length = len(word)
        count = 0
        display = "_" * length
        already_guessed = []
        play_game = ""

    def playing_loop():
        global play_game
        play_game = input(f"Do you want to play again {name} (Y/N)? ")
        play_game = play_game.lower()
        while play_game not in ["y", "yes", "no", "n"]:
            play_game = input(f"Do you want to play again {name} (Y/N)? ")
        if play_game == "yes" or "y":
            main_of_the_game()
        elif play_game == "no" or "n":
            print(f"Thanks for playing! I hope you enjoyed it {name}")
            time.sleep(2)
            exit()

    def hangman():
        global count
        global display
        global word
        global already_guessed
        global play_game
        limit = 5

        guess = input("This is the Hangman word: " + display + " Enter your guess: \n")
        guess = guess.strip()

        if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
            print(f"Invalid input {name}, try a letter.\n")
            hangman()

        elif guess in word:
            already_guessed.extend([guess])
            index = word.find(guess)
            word = word[:index] + "_" + word[index + 1:]
            display = display[:index] + guess + display[index + 1:]
            print(display + "\n")

        elif guess in already_guessed:
            print(f"You already guessed this letter {name}, Try another letter.\n")

        else:
            count += 1

            if count == 1:
                time.sleep(1)
                print("   _____\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__")
                print("Wrong guess. " + str(limit - count) + "guesses remaining.\n")

            elif count == 2:
                time.sleep(1)
                print("  _____\n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__")
                print("Wrong guess. " + str(limit - count) + "guesses remaining.\n")

            elif count == 3:
                time.sleep(1)
                print("  _____\n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     |\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__")
                print("Wrong guess. " + str(limit - count) + "guesses remaining.\n")

            elif count == 4:
                time.sleep(1)
                print("  _____\n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     |\n"
                      "  |     O\n"
                      "  |      \n"
                      "  |      \n"
                      "__|__")
                print("Wrong guess. " + str(limit - count) + "last guess remaining.\n")

            elif count == 5:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |    / \ \n"
                      "__|__")
                print(f"Wrong guess. You are hanged, {name}!\n")
                print("The word was: ", already_guessed, word)
                playing_loop()

        if word == '_' * length:
            print(f"Congrats {name}! You guessed correctly!")
            playing_loop()
        elif count != limit:
            hangman()

    main_of_the_game()
    hangman()


def image_viewer():
    root = Tk()
    root.title("Image Viewer")

    my_img1 = ImageTk.PhotoImage(Image.open("images/suku.png"))
    my_img2 = ImageTk.PhotoImage(Image.open("images/image.png"))
    my_img3 = ImageTk.PhotoImage(Image.open("images/ilkdeneme.png"))
    my_img4 = ImageTk.PhotoImage(Image.open("images/linkedin.png"))
    my_img5 = ImageTk.PhotoImage(Image.open("images/img_forest.jpg"))

    image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

    status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

    my_label = Label(image=my_img1)
    my_label.grid(row=0, column=0, columnspan=3)

    def forward(image_number):
        global my_label
        global button_forward
        global button_back

        my_label.grid_forget()
        my_label = Label(image=image_list[image_number - 1])
        button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
        button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

        if image_number == 5:
            button_forward = Button(root, text=">>", state=DISABLED)

        status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                       anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W + E)

        my_label.grid(row=0, column=0, columnspan=3)
        button_back.grid(row=1, column=0)
        button_forward.grid(row=1, column=2)

    def back(image_number):
        global my_label
        global button_forward
        global button_back

        my_label.grid_forget()
        my_label = Label(image=image_list[image_number - 1])
        button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
        button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

        if image_number == 1:
            button_back = Button(root, text="<<", state=DISABLED)

        status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                       anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W + E)

        my_label.grid(row=0, column=0, columnspan=3)
        button_back.grid(row=1, column=0)
        button_forward.grid(row=1, column=2)

    button_back = Button(root, text="<<", command=back, state=DISABLED)
    button_exit = Button(root, text="exit", command=root.quit)
    button_forward = Button(root, text=">>", command=lambda: forward(2))

    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2, pady=10)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def cal():
    root = Tk()
    root.title("Calculator")
    menubar = Menu(root)

    entry_bar = Entry(root, width=30, borderwidth=5, bg='#bbffff')
    entry_bar.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    # img_of_square_root = ImageTk.PhotoImage(Image.open("square root.png"))

    def button_click(number):
        current_variable = entry_bar.get()
        entry_bar.delete(0, END)
        entry_bar.insert(0, str(current_variable) + str(number))

    def button_clear():
        entry_bar.delete(0, END)

    def button_add():
        first_number = entry_bar.get()
        global fst_number
        fst_number = int(first_number)
        global math1
        math1 = "addition"
        entry_bar.delete(0, END)

    def button_equal():
        second_number = entry_bar.get()
        entry_bar.delete(0, END)
        global answer

        if math1 == "addition":
            entry_bar.insert(0, fst_number + int(second_number))
        elif math1 == "subtraction":
            entry_bar.insert(0, fst_number - int(second_number))
        elif math1 == "multiplication":
            entry_bar.insert(0, fst_number * int(second_number))
        elif math1 == "division":
            entry_bar.insert(0, fst_number / int(second_number))
        elif math1 == "square root":
            entry_bar.insert(0, math.sqrt(fst_number))
        elif math1 == "log":
            entry_bar.insert(0, math.log(fst_number, 10))
        elif math1 == "ln":
            entry_bar.insert(0, numpy.log(fst_number))
        elif math1 == "power":
            entry_bar.insert(0, math.pow(fst_number, int(second_number)))
        elif math1 == "square":
            entry_bar.insert(0, math.pow(fst_number, 2))
        elif math1 == "factorial":
            entry_bar.insert(0, math.factorial(fst_number))
        elif math1 == "power on 10":
            entry_bar.insert(0, math.pow(10, fst_number))
        elif math1 == "sin":
            entry_bar.insert(0, math.sin(fst_number))
        elif math1 == "cos":
            entry_bar.insert(0, math.cos(fst_number))

    def button_subtract():
        first_number = entry_bar.get()
        global fst_number
        fst_number = int(first_number)
        global math1
        math1 = "subtraction"
        entry_bar.delete(0, END)

    def button_multiply():
        first_number = entry_bar.get()
        global fst_number
        fst_number = int(first_number)
        global math1
        math1 = "multiplication"
        entry_bar.delete(0, END)

    def button_divide():
        first_number = entry_bar.get()
        global fst_number
        fst_number = int(first_number)
        global math1
        math1 = "division"
        entry_bar.delete(0, END)

    def button_square_root():
        first_number = entry_bar.get()
        global fst_number
        fst_number = int(first_number)
        global math1
        math1 = "square root"

    def button_log():
        first_number = entry_bar.get()
        global fst_number
        fst_number = int(first_number)
        global math1
        math1 = "log"

    def button_ln():
        first_number = entry_bar.get()
        global fst_number
        fst_number = int(first_number)
        global math1
        math1 = "ln"

    def button_pow():
        first_number = entry_bar.get()
        global fst_number
        fst_number = int(first_number)
        global math1
        math1 = "power"
        entry_bar.delete(0, END)

    def button_square():
        first_number = entry_bar.get()
        global fst_number
        fst_number = int(first_number)
        global math1
        math1 = "square"

    def button_factorial():
        first_number = entry_bar.get()
        global fst_number
        fst_number = int(first_number)
        global math1
        math1 = "factorial"

    def button_sin():
        first_number = entry_bar.get()
        global fst_number
        fst_number = int(first_number)
        global math1
        math1 = "sin"

    def button_cos():
        first_number = entry_bar.get()
        global fst_number
        fst_number = int(first_number)
        global math1
        math1 = "cos"

    def button_power_on_10():
        first_number = entry_bar.get()
        global fst_number
        fst_number = int(first_number)
        global math1
        math1 = "power on 10"

    ##################
    ##################

    main_menu = Menu(menubar, tearoff=0)
    main_menu.add_command(label="Exit", command=root.quit)

    button_0 = Button(root, text="0", padx=39, pady=20, command=lambda: button_click(0), bg='#686161', fg='#FFFFFF')
    button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), bg='#686161', fg='#FFFFFF')
    button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), bg='#686161', fg='#FFFFFF')
    button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), bg='#686161', fg='#FFFFFF')
    button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), bg='#686161', fg='#FFFFFF')
    button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), bg='#686161', fg='#FFFFFF')
    button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), bg='#686161', fg='#FFFFFF')
    button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), bg='#686161', fg='#FFFFFF')
    button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), bg='#686161', fg='#FFFFFF')
    button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), bg='#686161', fg='#FFFFFF')
    button_add = Button(root, text="+", padx=38, pady=20, command=button_add, bg='#686161', fg='#FFFFFF')
    button_equal = Button(root, text="=", padx=87, pady=20, command=button_equal, bg='#686161', fg='#FFFFFF')
    button_clear = Button(root, text="C", padx=87, pady=20, command=button_clear, bg='#686161', fg='#FFFFFF')
    button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract, bg='#686161', fg='#FFFFFF')
    button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply, bg='#686161', fg='#FFFFFF')
    button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide, bg='#686161', fg='#FFFFFF')
    button_square_root = Button(root, text="√", padx=47, pady=20, command=button_square_root, bg='#686161',
                                fg='#FFFFFF')
    button_log = Button(root, text="log", padx=43, pady=20, command=button_log, bg='#686161', fg='#FFFFFF')
    button_ln = Button(root, text="ln", padx=46, pady=20, command=button_ln, bg='#686161', fg='#FFFFFF')
    button_pow = Button(root, text="x^y", padx=40, pady=20, command=button_pow, bg='#686161', fg='#FFFFFF')
    button_square = Button(root, text="x^2", padx=40, pady=20, command=button_square, bg="#686161", fg="#FFFFFF")
    button_factorial = Button(root, text="n!", padx=45, pady=20, command=button_factorial, bg="#686161", fg="#FFFFFF")
    button_power_on_10 = Button(root, text="10^x", padx=36, pady=20, command=button_power_on_10, bg="#686161",
                                fg="#FFFFFF")
    button_sin = Button(root, text="sin", padx=43, pady=20, command=button_sin, bg="#686161", fg="#FFFFFF")
    button_cos = Button(root, text="cos", padx=40, pady=20, command=button_cos, bg="#686161", fg="#FFFFFF")

    button_9.grid(row=1, column=0)
    button_7.grid(row=1, column=1)
    button_8.grid(row=1, column=2)
    button_square_root.grid(row=1, column=4)
    button_sin.grid(row=1, column=5)
    button_6.grid(row=2, column=0)
    button_4.grid(row=2, column=1)
    button_5.grid(row=2, column=2)
    button_log.grid(row=2, column=4)
    button_cos.grid(row=2, column=5)
    button_3.grid(row=3, column=0)
    button_1.grid(row=3, column=1)
    button_2.grid(row=3, column=2)
    button_ln.grid(row=3, column=4)
    button_power_on_10.grid(row=3, column=5)
    button_0.grid(row=4, column=0)
    button_clear.grid(row=4, column=1, columnspan=2)
    button_pow.grid(row=4, column=4)
    button_add.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)
    button_square.grid(row=5, column=4)
    button_subtract.grid(row=6, column=0)
    button_multiply.grid(row=6, column=1)
    button_divide.grid(row=6, column=2)
    button_factorial.grid(row=6, column=4)

    root.config(menu=main_menu)


Button(root, text="Open the calculator", command=lambda: cal()).pack(padx=40, pady=20)
Button(root, text="Open the image viewer", command=lambda: image_viewer()).pack(padx=40, pady=20)
Button(root, text="Open the hangman game", command=lambda: hangman_game()).pack(padx=40, pady=20)
Button(root, text="Open the guessing game", command=lambda: guessing_game()).pack(padx=40, pady=20)

mainloop()