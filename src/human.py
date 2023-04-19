"""This module for human classes
"""

from enum import Enum
from random import randrange

from blood_type import BloodType


class Sex(Enum):
    """Sex Enum"""
    F = 'female'
    M = 'male'

    def __str__(self):
        return f'{self.value}'


class Human:
    """Human class"""

    def __init__(self, sex, feature1, feature2):
        try:
            if not isinstance(sex, Sex):
                sex = Sex[sex]
        except KeyError as exc:
            raise TypeError('sex has to be F or M') from exc
        self.sex = sex
        self.blood = BloodType(feature1, feature2)
        self.mate = None
        self.children = []
        self.parent = None

    def marriage(self, mate):
        """marriage for calculating next generation"""
        if not isinstance(mate, Human):
            raise TypeError('mate has to be Human instance')
        if self.sex == mate.sex:
            # TODO: It is not reflect current society # pylint: disable=fixme
            raise TypeError('mate\'s sex has to be different')
        self.mate = mate
        mate.mate = self

    def childbirth(self):
        """childbirth for calculating next generation"""
        if self.mate is None:
            return
        if self.sex is not Sex.F:
            return
        sex = Sex.F if randrange(0, 2) == 0 else Sex.M
        feature1 = self.blood.feature1 if randrange(
            0, 2) == 0 else self.blood.feature2
        feature2 = self.mate.blood.feature1 if randrange(
            0, 2) == 0 else self.mate.blood.feature2
        child = Human(sex, feature1, feature2)
        child.parent = self
        self.children.append(child)
        self.mate.children.append(child)

    def __str__(self):
        return f'sex : {self.sex}\nblood type : {self.blood}'
