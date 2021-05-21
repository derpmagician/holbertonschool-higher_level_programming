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

    m_a_empty = False
    m_b_empty = False
    m_a_notrect = False
    m_b_notrect = False
    m_a_notnum = False
    m_b_notnum = False
    m_a_scalar = False
    m_b_scalar = False
    for row in m_a:
        if not isinstance(row, list):
            m_a_scalar = True
        if len(row) != len(m_a[0]):
            m_a_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_a_notnum = True

    for row in m_b:
        if not isinstance(row, list):
            m_b_scalar = True
        if len(row) != len(m_b[0]):
            m_b_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_b_notnum = True

    if m_a_scalar:
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if m_b_scalar:
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if m_a_notnum:
        raise TypeError("invalid data type for einsum")

    if m_b_notnum:
        raise TypeError("invalid data type for einsum")

    if m_a_notrect:
        raise ValueError("setting an array element with a sequence.")

    if m_b_notrect:
        raise ValueError("setting an array element with a sequence.")

    return numpy.matrix(m_a) * numpy.matrix(m_b)
