from enum import Enum
from copy import deepcopy

class BloodFeature(Enum):
    O = 0
    A = 1
    B = 2

    def __str__(self):
        return f'{self.name}'

class BloodType:
    def __init__(self, f1, f2):
        try:
            if not isinstance(f1, BloodFeature):
                f1 = BloodFeature[f1]
            if not isinstance(f2, BloodFeature):
                f2 = BloodFeature[f2]
        except KeyError:
            raise TypeError('f1 and f2 has to be A, B or O')
        if f2.value > f1.value:
            tmp = deepcopy(f1)
            f1 = f2
            f2 = tmp
        self.f1 = f1
        self.f2 = f2

    @property
    def feature(self):
        if self.f1 is BloodFeature.O:
            return 'O'
        if self.f1 is BloodFeature.A:
            return 'A'
        if self.f2 is BloodFeature.A:
            return 'AB'
        return 'B'

    def __str__(self):
        return f'{self.feature}'
