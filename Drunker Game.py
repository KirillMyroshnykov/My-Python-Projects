from random import shuffle

class Card:
    suits = ["пик", "треф", "бубен", "червей"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __lt__(self, card2):
        if self.value < card2.value:
            return True
        if self.value == card2.value:
            if self.suit < card2.suit:
                return True
            else:
                return False
        return False
    
    def __gt__(self, card2):
        if self.value > card2.value:
            return True
        if self.value == card2.value:
            if self.suit > card2.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        return self.values[self.value] + ' ' + self.suits[self.suit]

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)
    
    def random_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.name = name

class Game:
    def __init__(self):
        player_name1 = input("Имя игрока 1: ")
        player_name2 = input("Имя игрока 2: ")
        self.deck = Deck()
        self.p1 = Player(player_name1)
        self.p2 = Player(player_name2)

    def wins (self, winner):
        win = "{} забирает карты"
        win = win.format(winner)
        print(win)
    
    def draw(self, player1_name, player1_card, player2_name, player2_card):
        draw = f"{player1_name} кладёт {player1_card}, а {player2_name} кладёт {player2_card}"
        print(draw)

    def play_game(self):
        cards = self.deck.cards
        print("Поехали!")
        while len (cards) >= 2:
            message = "Нажмите X для выхода. Нажмите любую другую клавишу для начала игры."

            response = input(message)

            if response == "X":
                break
            p1c = self.deck.random_card()
            p2c = self.deck.random_card()
            p1n = self.p1.name
            p2n = self.p2.name

            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win = self.winner(self.p1, self.p2)

        print(f"Игра окончена. {win} выиграл!")
    
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        elif p1.wins < p2.wins:
            return p2.name
        else:
            return "Ничья"
        
game = Game()
game.play_game()