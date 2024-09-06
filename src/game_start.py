import sys
import random

from prompt_toolkit.shortcuts import (
    input_dialog,
    message_dialog,
    radiolist_dialog,
)

from src.classes.monster import Monster
from src.classes.characters import Player
from src.data.monsterdex import monsters_data


def get_monsters() -> list[tuple[Monster, str]]:
    """Initialize and return monster data."""

    monsters: list[tuple[Monster, str]] = []

    for monster in monsters_data:
        monster = Monster(
            name=monster["name"], stats=monster["stats"], moves=monster["moves"]
        )
        monsters.append((monster, monster.get_name()))

    return monsters


def init_player():
    """Get the players name and their first monster."""

    name = input_dialog(title="Welcome to MonsterMon!", text="What is your name:").run()

    try:
        name.strip()
    except AttributeError:
        pass

    if name == None or name == "":
        name = "Mario"
        message_dialog(
            title="Nameless?",
            text="No name huh?\nWell from now on you are Mario, enjoy!",
        ).run()

    monsters = get_monsters()
    partner = radiolist_dialog(
        title="Choose your partner!",
        text="You can switch at any time!",
        values=monsters,
    ).run()

    if partner == None or partner == "":
        print("Fine then don't play this game :(")
        sys.exit()

    return Player(name=name, partner=partner, party=monsters, main_character=True)

def init_enemy():
    """Gives the enemy a random monster"""
    name = "Enemy"
    monsters = get_monsters()
    partner = random.choice(monsters)

    return Player(name=name, partner=partner[0], party=monsters, main_character=False)
