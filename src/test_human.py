import pytest

from .blood_type import BloodFeature
from .human import Sex, Human


@pytest.fixture
def male_person():
    return Human(Sex.M, BloodFeature.O, BloodFeature.O)


@pytest.fixture
def female_person():
    return Human(Sex.F, BloodFeature.A, BloodFeature.A)


def test_sex():
    assert f'{Sex.F}' == 'female'
    assert f'{Sex.M}' == 'male'


def test_human_construction():
    person = Human("M", "A", "B")
    assert f'{person}' == 'sex : male\nblood type : AB'
    assert person.mate == None
    assert person.children == []
    assert person.parent == None
    with pytest.raises(TypeError):
        Human('男', 'A', 'O')


def test_human_marriage(male_person, female_person):
    with pytest.raises(TypeError):
        male_person.marriage('None Human instance')
    with pytest.raises(TypeError):
        male_person.marriage(Human('M', 'A', 'A'))

    male_person.marriage(female_person)
    assert male_person.mate == female_person
    assert male_person.children == []
    assert male_person.parent == None
    assert female_person.mate == male_person
    assert female_person.children == []
    assert female_person.parent == None


def test_human_childbirth(male_person, female_person):
    male_person.marriage(female_person)
    male_person.childbirth()
    assert male_person.mate == female_person
    assert male_person.children == []
    assert male_person.parent == None
    assert female_person.mate == male_person
    assert female_person.children == []
    assert female_person.parent == None

    female_person.childbirth()
    assert male_person.mate == female_person
    assert len(male_person.children) == 1
    assert male_person.parent == None
    assert female_person.mate == male_person
    assert len(female_person.children) == 1
    assert female_person.parent == None
    child = male_person.children[0]
    assert f'{child.blood}' == 'A'
    assert f'{child.blood.feature1}' == 'A'
    assert f'{child.blood.feature2}' == 'O'
