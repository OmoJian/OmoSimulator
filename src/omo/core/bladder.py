"""
Bladder has basic properties like maximal urine and deals with urine increasing. 
"""

from random import randint

from .utils import clamp


class Bladder:
    """
    Character's urinary bladder. 

    60% < fullness <= 80%  WARNING
    80% < fullness < 100%  CRITICAL
    """

    def __init__(self, state, bladder, maximal_urine, urine_income_bounds):
        self.maximal_urine, *self._urine_income_bounds = maximal_urine, *urine_income_bounds

        self.maximal_urine *= 0.9

        self._urine = bladder
        self._tummy_water = 0

        self._state = state

    @property
    def urine(self):
        """Current urine volume in milliliters."""
        return self._urine

    @urine.setter
    def urine(self, value):
        self._urine = clamp(value, 0, self.maximal_urine)

    @property
    def urine_decimal_ratio(self):
        """``urine / maximal_urine``"""
        return self.urine / self.maximal_urine

    @property
    def tummy_water(self):
        """Current volume of water in tummy in milliliters."""
        return self._tummy_water

    @tummy_water.setter
    def tummy_water(self, value):
        self._tummy_water = max(0, value)

    def empty(self):
        """Empties this bladder and requires a corresponding character thought."""
        self.urine = 0
        self._state.character.thinker.think_about_peeing()

    def tick(self):
        """Game element tick function."""
        self._state.character.thinker.think_about_bladder_fullness()

        self._add_urine()

    def _add_urine(self):
        """Adds some urine."""
        self.urine += randint(*self._urine_income_bounds)

        if self.tummy_water > 0:
            self.tummy_water -= 3
            self.urine += 3

    @property
    def is_fullness_critical(self):
        """Return True if fullness is critical. """
        return self.urine_decimal_ratio > 0.8
