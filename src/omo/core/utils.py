"""
Store some utils. 
"""

from random import random


def occurs(possibility):
    """Determine whether an event occurs based on the given probability."""
    return random() < possibility / 100


def clamp(n, smallest, largest):
    """Limit a number within a specified range."""
    return max(smallest, min(n, largest))


def difficulty_dependent(*args, **kwargs):
    """Temp function. """
    return args[3]
