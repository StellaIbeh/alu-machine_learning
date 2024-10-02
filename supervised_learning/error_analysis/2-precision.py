#!/usr/bin/env python3
"""Precision"""
import numpy as np


def precision(confusion):
    """Calculates the sensitivity for each class
    in a confussion matrix
    """
    classes, _ = confusion.shape
    result = np.zeros(classes)

    for class_ in range(classes):
        result[class_] = np.divide(
            confusion[class_][class_],
            np.sum(confusion[:, class_])
        )

    return result
