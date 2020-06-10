from src.Human import Human, Sex
from src.BloodType import BloodFeature
from random import randrange, shuffle, gauss

class Society:
    def __init__(self, n, proportion, max=10000):
        self.gen = 1
        a, b, o, ab = [int(n * p) for p in proportion]
        def human_generator(blood_type, n):
            tmp = [None] * n
            idx = 0
            f1 = blood_type[0]
            f2 = blood_type[1]
            for _ in range(n):
                s = 'F' if randrange(0,2) == 0 else 'M'
                h = Human(s, f1, f2)
                tmp[idx] = h
                idx += 1
            return tmp
        tmp = []
        tmp += human_generator('AA', int(a / 2))
        tmp += human_generator('AO', int(a / 2))
        tmp += human_generator('BB', int(b / 2))
        tmp += human_generator('BO', int(b / 2))
        tmp += human_generator('OO', o)
        tmp += human_generator('AB', ab)
        self.people = tmp
        self.max = max

    def get_portion(self):
        f_c = 0
        a_c = 0
        b_c = 0
        o_c = 0
        t_c = 0
        try:
            i = iter(self.people)
            while True:
                h = next(i)
                f_c += int(h.sex is Sex.F)
                a_c += int(h.blood.feature == 'A')
                b_c += int(h.blood.feature == 'B')
                o_c += int(h.blood.feature == 'O')
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

    def get_blood_featrue_portion(self):
        a_c = 0
        b_c = 0
        o_c = 0
        t_c = 0
        try:
            i = iter(self.people)
            while True:
                h = next(i)
                a_c += int(h.blood.f1 is BloodFeature.A) + int(h.blood.f2 is BloodFeature.A)
                b_c += int(h.blood.f1 is BloodFeature.B) + int(h.blood.f2 is BloodFeature.B)
                o_c += int(h.blood.f1 is BloodFeature.O) + int(h.blood.f2 is BloodFeature.O)
                t_c += 2
        except StopIteration:
            pass
        return (a_c/t_c, b_c/t_c, o_c/t_c)

    def __str__(self):
        f_p, m_p, a_p, b_p, o_p, ab_p = self.get_portion()
        return f'gen : {self.gen}\npopulation : {len(self.people)}\nfemail portion {f_p:.2f}, mail portion {m_p:.2f}\nA : {a_p:.2f},B : {b_p:.2f},O : {o_p:.2f},AB : {ab_p:.2f}'

    def next_gen(self):
        f_g = []
        m_g = []
        shuffle(self.people)
        try:
            i = iter(self.people)
            f_c = 0
            m_c = 0
            while True:
                h = next(i)
                if h.sex is Sex.F:
                    f_g.append(h)
                    f_c += 1
                else:
                    m_g.append(h)
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
                f = next(i)
                m = next(j)
                f.marriage(m)
                n = int(gauss(2, 1)) if f_c + m_c > self.max else int(gauss(3, 1))
                n = n if n > 0 else 0
                for _ in range(n):
                    f.childbirth()
                tmp += f.children
        except StopIteration:
            pass
        self.people = tmp
        self.gen += 1
