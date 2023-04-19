"""this module for define society class
"""

from random import randrange, shuffle, gauss

from .human import Human, Sex
from .blood_type import BloodFeature


class Society:
    """class for group of human"""

    def __init__(self, n_count, proportion, max_iter=10000):
        self.gen = 1
        a_type, b_type, o_type, ab_type = [
            int(n_count * p) for p in proportion]

        def human_generator(blood_type, n_count):
            tmp = [None] * n_count
            idx = 0
            feature1 = blood_type[0]
            feature2 = blood_type[1]
            for _ in range(n_count):
                sex = 'F' if randrange(0, 2) == 0 else 'M'
                human = Human(sex, feature1, feature2)
                tmp[idx] = human
                idx += 1
            return tmp
        tmp = []
        tmp += human_generator('AA', int(a_type / 2))
        tmp += human_generator('AO', int(a_type / 2))
        tmp += human_generator('BB', int(b_type / 2))
        tmp += human_generator('BO', int(b_type / 2))
        tmp += human_generator('OO', o_type)
        tmp += human_generator('AB', ab_type)
        self.people = tmp
        self.max = max_iter

    def get_proportion(self):
        """get proportion of ABO blood type"""
        f_c = 0
        a_c = 0
        b_c = 0
        o_c = 0
        t_c = 0
        try:
            i = iter(self.people)
            while True:
                human = next(i)
                f_c += int(human.sex is Sex.F)
                a_c += int(human.blood.feature == 'A')
                b_c += int(human.blood.feature == 'B')
                o_c += int(human.blood.feature == 'O')
                t_c += 1
        except StopIteration:
            pass
        f_p = f_c / t_c
        m_p = 1 - f_p
        a_p = a_c / t_c
        b_p = b_c / t_c
        o_p = o_c / t_c
        ab_p = 1 - a_p - b_p - o_p
        return (f_p, m_p, a_p, b_p, o_p, ab_p)

    def get_blood_feature_portion(self):
        """get proportion of ABO blood feature"""
        a_c = 0
        b_c = 0
        o_c = 0
        t_c = 0
        try:
            i = iter(self.people)
            while True:
                human = next(i)
                a_c += int(human.blood.f1 is BloodFeature.A) + \
                    int(human.blood.f2 is BloodFeature.A)
                b_c += int(human.blood.f1 is BloodFeature.B) + \
                    int(human.blood.f2 is BloodFeature.B)
                o_c += int(human.blood.f1 is BloodFeature.O) + \
                    int(human.blood.f2 is BloodFeature.O)
                t_c += 2
        except StopIteration:
            pass
        return (a_c/t_c, b_c/t_c, o_c/t_c)

    def __str__(self):
        f_p, m_p, a_p, b_p, o_p, ab_p = self.get_proportion()
        return (
            f'gen : {self.gen}\n'
            f'population : {len(self.people)}\n'
            f'female portion {f_p:.2f}, male portion {m_p:.2f}\n'
            f'A : {a_p:.2f},B : {b_p:.2f},O : {o_p:.2f},AB : {ab_p:.2f}'
        )

    def next_gen(self):
        """calculate next society"""
        f_g = []
        m_g = []
        shuffle(self.people)
        try:
            i = iter(self.people)
            f_c = 0
            m_c = 0
            while True:
                human = next(i)
                if human.sex is Sex.F:
                    f_g.append(human)
                    f_c += 1
                else:
                    m_g.append(human)
                    m_c += 1
        except StopIteration:
            pass
        if f_c > m_c:
            f_g = f_g[0:m_c]
        else:
            m_g = m_g[0:f_c]
        try:
            i = iter(f_g)
            j = iter(m_g)
            tmp = []
            while True:
                female = next(i)
                male = next(j)
                female.marriage(male)
                next_gen = int(gauss(2, 1)) if f_c + \
                    m_c > self.max else int(gauss(3, 1))
                next_gen = next_gen if next_gen > 0 else 0
                for _ in range(next_gen):
                    female.childbirth()
                tmp += female.children
        except StopIteration:
            pass
        self.people = tmp
        self.gen += 1
