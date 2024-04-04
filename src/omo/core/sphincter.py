"""
Sphincter deals with sphincter power and power-caused leaking. 
"""

from random import randint

from .utils import clamp, occurs, difficulty_dependent


class Sphincter:
    """Bladder's sphincter."""

    def __init__(self, state, leaking_level, leak_volume_bounds):

        self._power = 100
        self._leaking_level, *self._leak_volume_bounds = leaking_level, *leak_volume_bounds
        self.incontinence = 1
        self._state = state

    @property
    def power(self):
        """Power of this sphincter."""
        return self._power

    @power.setter
    def power(self, value):
        self._power = clamp(value, 0, 100)

    def tick(self):
        """Combined power decreasing and leak checking while looping. """
        self._decrease_power()
        self._check_leak()

        self._state.character.thinker.think_about_low_sphincter_power()

    def _decrease_power(self):
        bladder = self._state.character.bladder
        if bladder.urine_decimal_ratio < 0.2:
            self.power += difficulty_dependent(self._state, 8, 6, 4)
        elif bladder.urine_decimal_ratio > 0.5:
            self.power -= 4 \
                          * self.incontinence \
                          * self._state.character.embarrassment \
                          * (bladder.urine / bladder.maximal_urine)

    def _check_leak(self):
        if self.power < self._leaking_level:
            leak_possibility = (self._leaking_level -
                                self.power) / self._leaking_level * 100
            if occurs(leak_possibility):
                self._leak()

    def _leak(self):
        volume = randint(*self._leak_volume_bounds)
        self._state.character.pee_into_wear(volume)  # TODO: Add leaking tip

        self._state.character.thinker.think_about_leaking()

    def die_if_bladder_is_too_full(self):
        """Pee all when too much urine is held. """
        bladder = self._state.character.bladder
        if bladder.urine >= bladder.maximal_urine:
            self._state.character.sphincter.power = 0

    @property
    def is_power_critical(self):
        """Return True if sphincter power too low. """
        return self.power < 20
