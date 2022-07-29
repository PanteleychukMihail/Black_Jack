import random


class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    def get_value(self) -> int:
        if self.rank in 'DVK':
            return 10
        elif self.rank in 'T':
            return 11
        else:
            return ' A2345789'.index(self.rank)

    def get_rank(self, ):
        return f'{self.suit}{self.rank}'


class DeskCard:
    def __init__(self):
        _rank = 'A23456789DVKT'
        _suit = 'ПКБЧ'
        self.__cards = [Card(r, s) for s in _suit for r in _rank]
        random.shuffle(self.__cards)

    def get_card(self) -> Card:
        return self.__cards.pop()


class Player:
    def __init__(self, name: str):
        self._hand = []
        self.count = 0
        self.name = name

    @property
    def hand(self, ) -> str:
        return f'Карты в руке: {self._hand}; Очков - {self.count} '

    @hand.setter
    def hand(self, card: Card) -> None:
        self.count += card.get_value()
        self._hand.append(card.get_rank())


class Dealer(Player):
    def get_card(self, cards: DeskCard):
        while self.count < 21:
            _card = cards.get_card()
            if _card.get_value() + self.count < 21:
                self.hand = _card
            else:
                break


class Game:
    def __init__(self, player_name: str):
        self.cards = DeskCard()
        self.player = Player(name=player_name)
        self.dealer = Dealer(name='Dealer')

    def print(self) -> str:
        return (f'\n{self.player.name}:\n {self.player.hand}\n{self.dealer.name}:\n{self.dealer.hand} ')

    def check_count(self):
        if self.player.count > 21 or (self.player.count <= self.dealer.count and self.dealer.count < 21):
            print(f"Вы проиграли", self.print())
        elif self.dealer.count > 21 and self.player.count < 21:
            print(f'Вы победили', self.print())
        elif self.dealer.count < self.player.count:
            print(f'Вы победили', self.print())

    def start(self) -> None:
        self.player.hand = self.cards.get_card()
        self.player.hand = self.cards.get_card()

        self.dealer.hand = self.cards.get_card()
        self.dealer.hand = self.cards.get_card()
        print(self.player.hand)
        while self.player.count < 21:
            answer = input('Еще?')
            if answer in "Yy":
                self.player.hand = self.cards.get_card()
                print(self.player.hand)
            elif answer in "Nn":
                self.dealer.get_card(self.cards)
                break
        self.check_count()


def main() -> None:
    name = input("Введите Имя \n")
    game = Game(name)
    game.start()


if __name__ == "__main__":
    main()
