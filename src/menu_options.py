import sys

from prompt_toolkit.shortcuts import (
    button_dialog,
    message_dialog,
    radiolist_dialog,
    yes_no_dialog,
)

from .game_logic import (
    calculate_damage,
    calculate_order,
    player_lost,
    player_won,
)
from .classes.characters import Player


def fight(player_a: Player, player_b: Player):
    """The whole fight sequence goes as follows.

    first we calculate the order of the battle. After that we calculate the
    damage and we deal the damage to the monster. We check if the monster died.
    If the monster died idk did not get to that point yet

    """

    monster_a = player_a.get_partner()
    monster_b = player_b.get_partner()

    order = calculate_order(monster_a, monster_b)

    if order:
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


def change_monster(player):
    new_partner = radiolist_dialog(
        title="Choose a monster!",
        text="Who do you want to choose?",
        values=player.get_party(),
    ).run()

    if not new_partner:
        return

    confirm = button_dialog(
        title="Confirm",
        text=f'You chose "{new_partner.get_name()}" as your new partner.\nHP:{new_partner.get_hp()}',
        buttons=[
            ("Yes", True),
            ("No, I changed my mind", False),
            ("No, my current partner is fine", None),
        ],
    ).run()

    if confirm:
        player.set_partner(new_partner)

    if not confirm:
        change_monster(player)


def flee(player):
    result = yes_no_dialog(
        title="Flee.", text="This will quit the game!\nAre you sure?"
    ).run()

    if result:
        print(f"Goodbye, {player.get_name()}!")
        sys.exit()
