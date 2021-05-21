#!/usr/bin/python3
"""
Defines lazy_matrix function
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplies one matrix by another.
    Args:
        m_a: the first matrix
        m_b: the second matrix
    Returns:
        matrix: the product
    Raises:
        TypeError: If m_a or m_b are not lists.
        TypeError: If m_a or m_b are not lists of lists.
        ValueError: If m_a or m_b are empty lists/matrices.
        TypeError: If m_a or m_b contain a non int/float.
        TypeError: If m_a or m_b are not rectangular.
        ValueError: If m_a or m_b can't be multiplied.
    """

    check_for_list(m_a)
    check_for_list(m_b)
    return numpy.matmul(m_a, m_b)


def check_for_list(value):
    """
    Check if the value is of type list
    Args:
        value (any): The value to verify.
    Raises:
        TypeError: If `value` isn't a list.
    """

    if type(value) is not list or len(value) == 0:
        raises_matrix_type_error()


def raises_matrix_type_error():
    """
    Raises:
        TypeError: If `matrix` list of lists of integers or floats.
    """

    raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
