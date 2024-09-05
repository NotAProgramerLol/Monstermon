from .monster import Monster

class Player:
    def __init__(
        self,
        name: str,
        current_monster: Monster,
        party,

    ):
        self.name = name
        self.current_monster = current_monster
        self.party = party

    def get_name(self):
        return self.name

    def get_current_monster(self):
        return self.current_monster

    def get_party(self):
        return self.party
