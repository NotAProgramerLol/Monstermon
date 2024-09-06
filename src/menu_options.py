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
    battle_sequence,
)
from .classes.characters import Player


def fight(player_a: Player, player_b: Player):
    """The whole fight sequence goes as follows.

    first we calculate the order of the battle. After that we calculate the
    damage and we deal the damage to the monster. We check if the monster died.
    If the monster died idk did not get to that point yet

    """

    order = calculate_order(player_a.get_partner(), player_b.get_partner())

    if order:
        battle_sequence(player_a, player_b)
        return

    battle_sequence(player_b, player_a)



def change_monster(player: Player):
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


def flee(player: Player):
    result = yes_no_dialog(
        title="Flee.", text="This will quit the game!\nAre you sure?"
    ).run()

    if result:
        print(f"Goodbye, {player.get_name()}!")
        sys.exit()
