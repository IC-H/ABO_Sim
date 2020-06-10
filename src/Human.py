from enum import Enum
from src.BloodType import BloodFeature, BloodType
from random import randrange

class Sex(Enum):
    F = 'femail'
    M = 'mail'

    def __str__(self):
        return f'{self.value}'

class Human:
    def __init__(self, sex, f1, f2):
        try:
            if not isinstance(sex, Sex):
                sex = Sex[sex]
        except KeyError:
            raise TypeError('sex has to be F or M')
        self.sex = sex
        self.blood = BloodType(f1, f2)
        self.mate = None
        self.children = []
        self.parent = None

    def marriage(self, mate):
        if not isinstance(mate, Human):
            raise TypeError('mate has to be Human instance')
        if self.sex == mate.sex:
            # TODO It is not refelt current society
            raise TypeError('mate\'s sex has to be diffrent')
        self.mate = mate
        mate.mate = self

    def childbirth(self):
        if self.mate is None:
            return
        if self.sex is not Sex.F:
            return
        sex = Sex.F if randrange(0,2) == 0 else Sex.M
        f1 = self.blood.f1 if randrange(0,2) == 0 else self.blood.f2
        f2 = self.mate.blood.f1 if randrange(0,2) == 0 else self.mate.blood.f2
        child = Human(sex, f1, f2)
        child.parent = self
        self.children.append(child)
        self.mate.children.append(child)

    def __str__(self):
        return f'sex : {self.sex}\nblood type : {self.blood}'
