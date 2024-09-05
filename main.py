from prompt_toolkit.shortcuts import input_dialog, radiolist_dialog, button_dialog, message_dialog

from src.classes.monster import Monster
from src.classes.player import Player
from src.data.monsterdex import monsters_data



def get_monsters() -> list[tuple[Monster, str]]:
    """Initialize and return monster data"""

    monsters: list[tuple[Monster, str]] = []

    for monster in monsters_data:
        monster = Monster(name=monster["name"], stats=monster["stats"], moves=monster["moves"])
        monsters.append((monster, monster.get_name()))

    return monsters


def init_player():
    """Get the players name and their first monster"""

    name = input_dialog(title="Welcome to MonsterMon!", text="Please type your name:").run()
    monsters = get_monsters()
    current_monster = radiolist_dialog(
        title="Choose your main monster!",
        text="You can switch at any time!",
        values=monsters,
    ).run()

    return Player(name=name, current_monster=current_monster, party=monsters)

player = init_player()

print(player.get_name())
print(player.get_current_monster().get_name())
print(player.get_party())
# print(player.get_party()[player.get_current_monster().get_name()])
# for monster in player.get_party():
#     print(monster[0].get_hp())
