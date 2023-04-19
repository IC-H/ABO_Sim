import pytest

from .blood_type import BloodFeature, BloodType


@pytest.fixture
def blood_type_oo():
    return BloodType(feature1=BloodFeature.O, feature2=BloodFeature.O)


@pytest.fixture
def blood_type_oa():
    return BloodType(feature1=BloodFeature.O, feature2=BloodFeature.A)


@pytest.fixture
def blood_type_ob():
    return BloodType(feature1=BloodFeature.O, feature2=BloodFeature.B)


@pytest.fixture
def blood_type_ao():
    return BloodType(feature1=BloodFeature.A, feature2=BloodFeature.O)


@pytest.fixture
def blood_type_aa():
    return BloodType(feature1=BloodFeature.A, feature2=BloodFeature.A)


@pytest.fixture
def blood_type_ab():
    return BloodType(feature1=BloodFeature.A, feature2=BloodFeature.B)


@pytest.fixture
def blood_type_bo():
    return BloodType(feature1=BloodFeature.B, feature2=BloodFeature.O)


@pytest.fixture
def blood_type_ba():
    return BloodType(feature1=BloodFeature.B, feature2=BloodFeature.A)


@pytest.fixture
def blood_type_bb():
    return BloodType(feature1=BloodFeature.B, feature2=BloodFeature.B)


def test_blood_feature():
    assert f'{BloodFeature.A}' == 'A'
    assert f'{BloodFeature.B}' == 'B'
    assert f'{BloodFeature.O}' == 'O'


def test_blood_type_oo(blood_type_oo):
    assert blood_type_oo.feature == 'O'


def test_blood_type_oa(blood_type_oa):
    assert blood_type_oa.feature == 'A'


def test_blood_type_ob(blood_type_ob):
    assert blood_type_ob.feature == 'B'


def test_blood_type_ao(blood_type_ao):
    assert blood_type_ao.feature == 'A'


def test_blood_type_aa(blood_type_aa):
    assert blood_type_aa.feature == 'A'


def test_blood_type_ab(blood_type_ab):
    assert blood_type_ab.feature == 'AB'


def test_blood_type_bo(blood_type_bo):
    assert blood_type_bo.feature == 'B'


def test_blood_type_ba(blood_type_ba):
    assert blood_type_ba.feature == 'AB'


def test_blood_type_bb(blood_type_bb):
    assert blood_type_bb.feature == 'B'
