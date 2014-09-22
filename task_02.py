#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task_02.py: Homework 4 Task 2."""

VALID = False
INPUT_NUM = 0
FACTORIAL = 1
PRODUCT = 1
IDX = 1

while not VALID:
    print "Enter number:"
    s = raw_input()
    try:
        INPUT_NUM = int(s)
        if INPUT_NUM < 0:
            # Invalid input.
            print "Invalid number: Please enter a number greater than zero."
            continue
        VALID = True
    except ValueError:
        # Invalid input.
        print "Invalid number: Please enter a valid number."
        continue

while IDX <= INPUT_NUM:
    PRODUCT *= IDX
    IDX += 1

print 'FACTORIAL: {}, PRODUCT: {}'.format(INPUT_NUM, PRODUCT)