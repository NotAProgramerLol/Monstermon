from .monster import Monster

class Player:
    def __init__(
        self,
        name: str,
        partner: Monster,
        party: list[tuple[Monster, str]],
        main_character: bool

    ):
        self.name = name
        self.partner = partner
        self.party = party
        self.main_character = main_character

    def get_name(self):
        return self.name

    def get_partner(self):
        return self.partner

    def get_party(self):
        return self.party

    def get_main_character(self):
        return self.main_character

    def set_partner(self, new_partner):
        self.partner = new_partner
