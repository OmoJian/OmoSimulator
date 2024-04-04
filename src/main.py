"""
Run this to simulate omo. 
"""
import os
import json
import time
import datetime

import click

from omo import core  # pylint: disable=E0401

character: core.character
clock: int

# Actions


def drink(args):
    """Drink certain amount of water into stomach. """
    volume = int(args[0])
    character.bladder.tummy_water += volume


def toilet(_):
    """Use the toilet. """
    character.bladder.empty()


def hold(_):
    """Do hold. """
    character.sphincter.power += 20


# Display

DISPLAY = """{name}'s {time}
 Fullness: {fullness}% ({urine}/{max_urine})
 Power: {power}%
 Tummy: {tummy}
 Clothes: Underwear( {underwear} ) | Outerwear( {outerwear} )"""


def status():
    """Show character status. """
    print(
        DISPLAY.format(name=character.name,
                       time=time.strftime('%m/%d/%Y %I:%M %p',
                                          time.localtime(clock)),
                       fullness=str(character.bladder.urine_decimal_ratio *
                                    100)[0:4],
                       urine=character.bladder.urine,
                       max_urine=character.bladder.maximal_urine,
                       power=str(character.sphincter.power)[0:4],
                       tummy=character.bladder.tummy_water,
                       underwear=character.underwear.dryness,
                       outerwear=character.outerwear.dryness))


# Start


@click.command()
@click.option("-c",
              "--config",
              type=click.File('r'),
              default="./src/Jane.json",
              show_default="./src/Jane.json")
@click.option("-t",
              "--time",
              "start",
              type=click.DateTime(),
              default=datetime.datetime.now(),
              show_default="Now")
@click.option("-b", "--bladder", type=int, default=0, show_default="0")
def simulate(config, start, bladder):
    """Start simulating. """
    global character, clock  # pylint: disable=W0603

    _config = json.load(config)

    character = core.character.Character(_config, bladder)

    clock = start.timestamp()

    status()

    while True:

        cmd = input("> ").split(" ")
        if cmd and cmd[0] == "quit": exit(1)  # pylint: disable=C0321

        os.system('cls')
        exec(f"{cmd[0]}({cmd[1:]})")  # pylint: disable=W0122

        clock += 2 * 60
        character.tick()

        status()


if __name__ == "__main__":
    simulate()  # pylint: disable=E1120
