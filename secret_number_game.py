from secret_number_def import get_score_list,play_game,get_score_list_all

while True:
    print("")
    selection = input("Would you like to (A) play a new game, (B) see the Top 3 scores (C) see all scores or (D) quit?")

    if selection in ("A", "a", "(A)", "(a)"):
        play_game()
    elif selection in ("B", "b", "(B)", "(b)"):
        get_score_list()
    elif selection in ("C", "c", "(C)", "(c)"):
        get_score_list_all()
    elif selection in ("D", "d", "(D)", "(d)"):
        print("Thank you for playing & Goodbye!")
        break
    else:
        print("Wrong input, please execute again!")
        break
