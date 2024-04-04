"""
Test file. 
"""
import time
import os

from omo import core  # pylint: disable=E0401

character = core.character.Character()

START = "03/24/2024 09:00 AM"
clock = int(time.mktime(time.strptime(START, "%m/%d/%Y %I:%M %p"))) - 2 * 60


def drink(args):
    volume = int(args[0])
    character.bladder.tummy_water += volume


def toilet(args):
    character.bladder.empty()


def hold(args):
    character.sphincter.power += 20


while True:
    inp = input("> ")
    if inp == "quit": exit(1)  # pylint: disable=C0321
    os.system('cls')

    clock += 2 * 60
    character.tick()

    cmd = inp.split(" ")
    print(cmd)

    exec(f"{cmd[0]}({cmd[1:]})")

    print(f"""{time.strftime('%m/%d/%Y %I:%M %p', time.localtime(clock))}
 Fullness: {str(character.bladder.urine_decimal_ratio*100)[0:4]}%({character.bladder.urine}/{character.bladder.maximal_urine})
 Power: {str(character.sphincter.power)[0:4]}%
 Tummy: {character.bladder.tummy_water}""")
