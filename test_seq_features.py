import pytest
from seq_features import *


def test_n_neg_for_single_E_or_D():
    """Perform unit tests on n_neg."""

    assert n_neg('E') == 1
    assert n_neg('D') == 1
    
def test_n_neg_for_empty_sequence():
    assert n_neg('') == 0

def test_n_neg_for_longer_sequences():
    assert n_neg('ACKLWTTAE') == 1
    assert n_neg('DDDDEEEE') == 8

def test_n_neg_for_lower_case_sequences():
    assert n_neg('acklwttae') == 1

def test_n_neg_for_invalid_aminoacid():
    with pytest.raises(RuntimeError) as excinfo:
        n_neg('Z')
    excinfo.match("Z is not a valid amino acid")

    with pytest.raises(RuntimeError) as excinfo:
        n_neg('z')
    excinfo.match("Z is not a valid amino acid")

    with pytest.raises(RuntimeError) as excinfo:
        n_neg('KAACABAYABADDLKPPSD')
    excinfo.match("B is not a valid amino acid")
