class Monster:
    def __init__(
        self,
        name: str,
        stats: dict[str, int],
        moves: list[str],
    ):
        self.name = name
        self.stats = stats
        self.moves = moves

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.stats["hp"]

    def get_attack(self):
        return self.stats["attack"]

    def get_speed(self):
        return self.stats["speed"]

    def get_mana(self):
        return self.stats["mana"]

    def get_moves(self):
        return self.moves

    def lose_hp(self, damage: int) -> int:
        self.stats["hp"] = self.stats["hp"] - damage

        if self.stats["hp"] <= 0:
            return 0

        return self.stats["hp"]
