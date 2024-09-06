import random
import sys

from prompt_toolkit.shortcuts import message_dialog

from .classes.monster import Monster
from .classes.characters import Player


def calculate_order(monster_a: Monster, monster_b: Monster):
    """Get the battle order using the speed stat.

    By comparing the speed stat we know what monster gets to go first.
    If the speed is the same we randomly choose a monster.
    And yes I am aware that speed is normally also used to dodge
    """
    if monster_a.get_speed() == monster_b.get_speed():
        return random.choice([True, False])

    if monster_a.get_speed() > monster_b.get_speed():
        return True

    return False


def calculate_damage(monster_a: Monster, monster_b: Monster):
    # Normally you would get the attack stat from the attacking monster get the attack stat from the used move,
    # look at the defense stat from the enemy and return a value based from that calculation.
    # I did not do this since i wanted to keep it as simple as possible.
    # On top of that if I would make it like that I would need to rewrite a large part of my code,
    # and if I would rewrite the code i also should improve my tui to be able to show all stats in a good way.

    return monster_a.get_attack()


def player_won():
    message_dialog(
        title="Congrats!!",
        text="You defeated a innocent man named Enemy.\nI hope you are happy with yourself.",
    ).run()
    sys.exit()


def player_lost():
    message_dialog(
        title=" :( ",
        text="Your partner died do you really want to keep going?",
    ).run()
    sys.exit()


def battle_sequence(player_a: Player, player_b: Player):
    monster_a = player_a.get_partner()
    monster_b = player_b.get_partner()

    # Turn of `monster_a`
    monster_b_damage = calculate_damage(monster_a, monster_b)
    if not monster_b.lose_hp(monster_b_damage):
        if player_a.get_main_character():
            player_won()

        player_lost()

    # Turn of `monster_b`
    monster_a_damage = calculate_damage(monster_b, monster_a)
    if not monster_a.lose_hp(monster_a_damage):
        if player_b.get_main_character():
            player_won()

        player_lost()

    message_dialog(
        title="Fighting",
        text=f"""{monster_a.get_name()} went first and did {monster_b_damage} damage to {monster_b.get_name()}.
{monster_b.get_name()} went second and did {monster_a_damage} damage to {monster_a.get_name()}.
{monster_a.get_name()} has {monster_a.get_hp()} HP
{monster_b.get_name()} has {monster_b.get_hp()} HP""",
    ).run()
