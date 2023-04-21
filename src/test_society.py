import pytest

from .society import Society


def test_society_construction(mocker):
    # 1 means male, 0 means female
    mocker.patch('src.society.randrange', side_effect=[1, 1, 0, 0, 1, 1, 0, 0])

    target = Society(8, [0.25, 0.25, 0.25, 0.25], 10)
    assert f'{target}' == (
        'gen : 1\n'
        'population : 8\n'
        'female portion 0.50, male portion 0.50\n'
        'A : 0.25,B : 0.25,O : 0.25,AB : 0.25'
    )
    assert target.get_blood_feature_proportion() == (5.0/16, 5.0/16, 6.0/16)

    with pytest.raises(Exception):
        Society('10', [0, 0, 1, 0], 10)
    with pytest.raises(Exception):
        Society(10, [0, 0, 1], 10)


def test_society_next_gen(mocker):
    """
    fix initial generation as below.
    person1: male with A(AA) blood type
    person2: male with A(AO) blood type
    person3: male with B(BB) blood type
    person4: female with B(BO) blood type
    person5: female with O(OO) blood type
    person6: female with O(OO) blood type
    person7: female with AB(AB) blood type
    person8: female with AB(AB) blood type
    """
    # 0: female, 1: male
    mocker.patch('src.society.randrange', side_effect=[1, 1, 1, 0, 0, 0, 0, 0])
    target = Society(8, [0.25, 0.25, 0.25, 0.25])

    """
    fix next generation as bellow.
    person1: female with AB(BA) blood type
    person2: female with AB(BA) blood type
    person3: female with A(AO) blood type
    person4: female with O(OO) blood type
    person5: male with B(BO) blood type
    person6: male with B(BO) blood type
    """
    # incapacitate shuffle, shuffle do nothing.
    mocker.patch('src.society.shuffle')
    # all females birth just 2 children
    mocker.patch('src.society.gauss', return_value=2)
    mocker.patch('src.human.randrange', side_effect=[
        0, 0, 0,
        0, 0, 1,
        0, 1, 0,
        0, 1, 1,
        1, 0, 0,
        1, 0, 1,
    ])

    target.next_gen()
    assert f'{target}' == (
        'gen : 2\n'
        'population : 6\n'
        'female portion 0.67, male portion 0.33\n'
        'A : 0.17,B : 0.33,O : 0.17,AB : 0.33'
    )
    assert target.get_blood_feature_proportion() == (3.0/12, 4.0/12, 5.0/12)
