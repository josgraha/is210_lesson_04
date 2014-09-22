#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task_01.py: Homework 4 Task 1."""

__author__ = "Joe Graham"

from data import SHAKESPEARE

MAXIMUM_WORDS = 0.0
MINIMUM_WORDS = 0.0
AVERAGE_WORDS = 0.0
TOTAL_WORDS = 0.0
TOTAL_LINES = 0.0
NUM_CRISPIAN = 0.0
LINES = SHAKESPEARE.split("\n")

for line in LINES:
    TOTAL_LINES += 1
    words = line.split(" ")
    if line.lower().find("crispian") > 0:
        NUM_CRISPIAN += 1
    TOTAL_WORDS += len(words)
    AVERAGE_WORDS = TOTAL_WORDS / TOTAL_LINES
    if len(words) <= MINIMUM_WORDS:
        MINIMUM_WORDS = len(words)
    elif MINIMUM_WORDS == 0:
        MINIMUM_WORDS = len(words)
    if len(words) > MAXIMUM_WORDS:
        MAXIMUM_WORDS = len(words)

print SHAKESPEARE
print '''

STATISTICS
--------------------------------------------------

TOTAL_LINES:        {}
MINIMUM_WORDS:      {}
MAXIMUM_WORDS:      {}
TOTAL_WORDS:        {}
AVERAGE_WORDS:      {}
NUM_CRISPIAN:       {}
'''.format(TOTAL_LINES,
           MINIMUM_WORDS,
           MAXIMUM_WORDS,
           TOTAL_WORDS,
           AVERAGE_WORDS,
           NUM_CRISPIAN)