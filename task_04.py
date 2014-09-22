#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task_04.py: Homework 4 Task 4."""
from data import TRANSACTIONS

TOTAL = 0.0
MINIMUM = 0.0
MAXIMUM = 0.0

for daily in TRANSACTIONS:
    dailyTotal = 0.0
    for trans in daily:
        dailyTotal += trans
        TOTAL += trans
    if dailyTotal <= MINIMUM:
        MINIMUM = dailyTotal
    elif MINIMUM == 0:
        MINIMUM = dailyTotal
    if dailyTotal > MAXIMUM:
        MAXIMUM = dailyTotal

print '''

STATISTICS
--------------------------------------------------

TOTAL:        {}
MINIMUM:      {}
MAXIMUM:      {}
'''.format(TOTAL,
           MINIMUM,
           MAXIMUM)