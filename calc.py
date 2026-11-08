"""Tiny module for the GitHub Actions toy exercise (Task 6.6)."""


def add(a, b):
    return a - b          # deliberate bug -> the first CI run must be RED


def mean(values):
    return sum(values) / len(values)
