"""
(To be completed. )
"""

from .leaker import Leaker
from .bladder import Bladder
from .sphincter import Sphincter
from .thinker import Thinker
from .utils import clamp
from .wear import Wear


def game_over(*args, **kwargs):
    print(f"DEBUG: game_over({args, kwargs}) from {__name__}")


class TempState():

    def __init__(self, char) -> None:
        self.character = char
        self.mode = 'StateMode.LESSON'


class Character:
    _THINK_DELAY = 5

    def __init__(self, config, bladder):
        self._state = TempState(self)

        self.name = config["name"]
        self.gender = config["gender"]
        self.bladder = Bladder(self._state, bladder, config["maximal_urine"],
                               config["urine_income_bounds"])
        self.sphincter = Sphincter(self._state,
                                   config["min_sphincter_leaking_power"],
                                   config["leak_volume_bounds"])
        self.thinker = Thinker(self._state)
        self.leaker = Leaker(self._state)

        self.stay_after_lessons = False
        self.stay_on_break = False
        self._embarrassment = 1
        self._embarrassment_decay = config["embarrassment_decay"]
        self._thirst_increase = config["thirst_increase"]

        self.underwear = Wear(config["underwear"]["name"],
                              config["underwear"]["pressure"],
                              config["underwear"]["absorption"],
                              config["underwear"]["drying"])
        self.outerwear = Wear(config["outerwear"]["name"],
                              config["outerwear"]["pressure"],
                              config["outerwear"]["absorption"],
                              config["outerwear"]["drying"])
        self._thirst = 0
        self._holding_block_duration = 0

    @property
    def embarrassment(self):
        return self._embarrassment

    @embarrassment.setter
    def embarrassment(self, value):
        self._embarrassment = clamp(value, 1, 100)

    @property
    def thirst(self):
        return self._thirst

    @thirst.setter
    def thirst(self, value):
        self._thirst = clamp(value, 0, 100)
        if self.thirst == 100:
            self.drink(100)

    @property
    def holding_blocked(self):
        return self._holding_block_duration != 0

    def tick(self):
        self.thinker.tick()
        self.bladder.tick()
        self.sphincter.tick()
        self.underwear.tick()
        self.outerwear.tick()
        self.leaker.tick()

        self.embarrassment -= self._embarrassment_decay
        self.thirst += self._thirst_increase

        self._holding_block_duration = max(0, self._holding_block_duration - 1)

        if self.embarrassment > 5:
            self.thinker.think_about_embarrassment()
        if self.thirst > 75:
            self.thinker.think_about_thirst()

    def pee_into_wear(self, how_much: int):  # TODO: Add leaking tip
        self.bladder.urine -= how_much
        if self.underwear.dryness > how_much:
            self.underwear.dryness -= how_much
        else:
            how_much -= self.underwear.dryness
            self.underwear.dryness = 0
            self.outerwear.dryness -= how_much

        if self.outerwear.dryness == 0:
            game_over()

    def drink(self, how_much_percent):
        self.thirst -= how_much_percent
        self.bladder.tummy_water += how_much_percent * 3

    def block_holding(self, turns):
        self._holding_block_duration += turns

    @property
    def something_is_critical(self):
        return self.bladder.is_fullness_critical \
               or self.sphincter.is_power_critical \
               or self.underwear.is_dryness_critical \
               or self.outerwear.is_dryness_critical
