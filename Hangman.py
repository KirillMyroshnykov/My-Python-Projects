import random
words = ["инструкция", "кот", "телевизор", "компьютер", "корабль", "плитка", "отрыв", "магнитофон", "алгоритм", "консенсус", "идиосинкразия"]


def hangman (word):
    
    wrong = 0
    stages = ["",
             "________        ",
             "|       |       ",
             "|       |       ",
             "|       0       ",
             "|      /|\      ",
             "|      / \      ",
             "|               "]
    real_letters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Добро пожаловать на казнь!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву: "
        guess = input(msg)
        if guess in real_letters:
            cind = real_letters.index(guess)
            board[cind] = guess
            real_letters[cind] = '$'
        else:
            wrong += 1
        print(("".join(board)))

        #Вывод фигуры висельника
        e = wrong + 1
        print("\n".join(stages[0: e]))
        
        #Условие победы
        if "_" not in board:
            print("Вы выиграли! Было загадано слово: ")
            print("".join(board))
            win = True
            break
    #Условие поражения
    if not win:
        print("\n".join(stages[0: wrong]))
        print("Вы проиграли! Было загадано слово: {}.".format(word))

hangman(words[random.randint(0, len(words)-1)])