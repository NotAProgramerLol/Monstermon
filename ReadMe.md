# This is a Pokemon inspired game named Monstermon

The goal of the game is to battle an opponent that has a few Monsters at his side.

This game is for now pretty boring since i have not implemented a way to choose moves and the monsters are badly balanced.
I also have not implemented things like hit chance, dodging, mana (since i haven't implemented moves yet) and items (for instance a healing potion).
This game is primarily made to show of programming skills (code when writing is still a small mess but thats "fine". since it's readable enough for now).

but if do continue developing I would change/ add the following things:

- Add more stats with inspiration from Pokemon
- Add usable items
- Make it possible to fight multiple monsters
- Being able to choose from a big list of monsters with the limit of 5 (it's not limited since I could not find a clean and fast way to put a limit on the checkboxes with the current library. Though I did not really read the documentation so thats that.)
- Make it possible to choose another monster as your partner when losing your partner and having monsters left in your party
- Make the enemy choose another monster when losing his partner (this is the same for the player since they use the same class and the data model does support it. I just need to make the logic and implement it)
- Design a way better ui since my current implementation kind of sucks

## Running the game

To run this game you need to have `python` and `pipenv` installed.
Sync the dependencies with:

```shell
make dependencies
```

Now the game should launch when using the following command:

```shell
make run
```
