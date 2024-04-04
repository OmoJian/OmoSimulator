"""
Leaker deals with fullness-caused leaking. 
"""

from logging import getLogger, basicConfig, DEBUG
from random import randint

from .utils import occurs

basicConfig(level=DEBUG)
_logger = getLogger('lhh.Leaker')


class Leaker:
    """Leak according to fullness. """

    def __init__(self, state):
        self._state = state

    @property
    def _fullness_threshold(self):
        return self._state.character.bladder.urine * 0.7

    @property
    def leak_possibility(self):
        """The fuller the bladder is, the bigger possibility of leaking. """
        bladder = self._state.character.bladder
        chn = (bladder.urine - self._fullness_threshold) / 2
        return chn

    @property
    def minimal_leak_volume(self):
        "Minimal leaking volume. "
        return max(1, self._state.character.bladder.urine**2 // 35000 - 23)

    @property
    def maximal_leak_volume(self):
        "Maximal leaking volume. "
        return max(0, self._state.character.bladder.urine**2 // 20000 - 32)

    def get_leak_volume(self):
        "Random leaking volume in leaking bounds. "
        return randint(self.minimal_leak_volume, self.maximal_leak_volume + 1)

    def tick(self):
        "Try leaking every loop. "
        if occurs(self.leak_possibility):
            volume = self.get_leak_volume()
            self._state.character.pee_into_wear(volume)
            self._state.character.thinker.think_about_leaking()
