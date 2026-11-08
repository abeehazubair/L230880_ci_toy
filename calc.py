"""Tiny module for the GitHub Actions toy exercise (Task 6.6)."""


def add(a, b):
    return a + b          # bug fixed -> CI turns GREEN


def mean(values):
    return sum(values) / len(values)
