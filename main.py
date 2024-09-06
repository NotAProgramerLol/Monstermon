from prompt_toolkit.shortcuts import (
    button_dialog,
)

from src.menu_options import fight, change_monster, flee
from src.game_start import init_player, init_enemy


player = init_player()
enemy = init_enemy()

playing = True

while playing == True:
    dialog_menu_text = f"""
        {player.get_name()}:
            {player.get_partner().get_name()} HP: {player.get_partner().get_hp()}

        {enemy.get_name()}:
            {enemy.get_partner().get_name()} HP: {enemy.get_partner().get_hp()}
    """

    choice = button_dialog(
        title=f"{player.get_name()}, please choose an action.",
        text=dialog_menu_text,
        buttons=[
            ("Fight", "fight"),
            ("Change monster", "change"),
            ("Flee", "flee"),
        ],
    ).run()

    match choice:
        case "fight":
            fight(player, enemy)
        case "change":
            change_monster(player)
        case "flee":
            flee(player)
