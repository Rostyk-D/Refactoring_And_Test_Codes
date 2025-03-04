import pytest
import numpy as np
from Lab2 import generate_random_matrix, fuzzy_composition, fuzzy_composition_minmax

def test_generate_random_matrix():
    rows, cols = 3, 4
    matrix = generate_random_matrix(rows, cols)
    assert matrix.shape == (rows, cols)
    assert (matrix >= 0).all() and (matrix <= 1).all()

def test_fuzzy_composition_basic():
    prof_attr = np.array([[0.5, 0.7], [0.2, 0.9]])
    attr_cand = np.array([[0.6, 0.3], [0.8, 0.4]])
    expected = np.array([[0.7, 0.4], [0.8, 0.4]])
    result = fuzzy_composition(prof_attr, attr_cand)
    np.testing.assert_almost_equal(result, expected, decimal=2)

def test_fuzzy_composition_minmax_basic():
    prof_attr = np.array([[0.5, 0.7], [0.2, 0.9]])
    attr_cand = np.array([[0.6, 0.3], [0.8, 0.4]])
    expected = np.array([[0.6, 0.5], [0.6, 0.3]])
    result = fuzzy_composition_minmax(prof_attr, attr_cand)
    np.testing.assert_almost_equal(result, expected, decimal=2)

def test_fuzzy_composition_zeros():
    zero_matrix = np.zeros((3, 3))
    result = fuzzy_composition(zero_matrix, zero_matrix)
    np.testing.assert_array_equal(result, zero_matrix)

def test_fuzzy_composition_minmax_zeros():
    zero_matrix = np.zeros((3, 3))
    result = fuzzy_composition_minmax(zero_matrix, zero_matrix)
    np.testing.assert_array_equal(result, zero_matrix)

def test_fuzzy_composition_ones():
    ones_matrix = np.ones((3, 3))
    result = fuzzy_composition(ones_matrix, ones_matrix)
    np.testing.assert_array_equal(result, ones_matrix)

def test_fuzzy_composition_minmax_ones():
    ones_matrix = np.ones((3, 3))
    result = fuzzy_composition_minmax(ones_matrix, ones_matrix)
    np.testing.assert_array_equal(result, ones_matrix)

def test_fuzzy_composition_different_sizes():
    prof_attr = np.array([[0.5, 0.6, 0.7], [0.2, 0.3, 0.4]])
    attr_cand = np.array([[0.8, 0.1], [0.5, 0.9], [0.3, 0.7]])
    result = fuzzy_composition(prof_attr, attr_cand)
    assert result.shape == (2, 2)

def test_fuzzy_composition_random_values():
    np.random.seed(42)
    prof_attr = np.random.rand(4, 5)
    attr_cand = np.random.rand(5, 6)
    result = fuzzy_composition(prof_attr, attr_cand)
    assert result.shape == (4, 6)

def test_fuzzy_composition_minmax_random_values():
    np.random.seed(42)
    prof_attr = np.random.rand(4, 5)
    attr_cand = np.random.rand(5, 6)
    result = fuzzy_composition_minmax(prof_attr, attr_cand)
    assert result.shape == (4, 6)