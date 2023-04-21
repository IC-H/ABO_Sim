"""This module for define blood type classes
"""

from enum import Enum
from copy import deepcopy


class BloodFeature(Enum):
    """ABO Feature of Blood Type"""
    O = 0
    A = 1
    B = 2

    def __str__(self):
        return f'{self.name}'


class BloodType:
    """Blood Type class"""

    def __init__(self, feature1, feature2):
        try:
            if not isinstance(feature1, BloodFeature):
                feature1 = BloodFeature[feature1]
            if not isinstance(feature2, BloodFeature):
                feature2 = BloodFeature[feature2]
        except KeyError as exc:
            raise TypeError('f1 and f2 has to be A, B or O') from exc
        if feature2.value > feature1.value:
            tmp = deepcopy(feature1)
            feature1 = feature2
            feature2 = tmp
        self.feature1 = feature1
        self.feature2 = feature2

    @property
    def feature(self):
        """returning blood type feature"""
        if self.feature1 is BloodFeature.O:
            return 'O'
        if self.feature1 is BloodFeature.A:
            return 'A'
        if self.feature2 is BloodFeature.A:
            return 'AB'
        return 'B'

    def __str__(self):
        return f'{self.feature}'
