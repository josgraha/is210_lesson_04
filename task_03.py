#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task_03.py: Homework 4 Task 3."""

from data import PASSWORD

ACCESS = False
NUM_ATTEMPTS = 3

while not ACCESS and NUM_ATTEMPTS > 0:
    print 'What is your password ({} attempts left)?'.format(NUM_ATTEMPTS)
    s = raw_input()
    NUM_ATTEMPTS -= 1
    if s == PASSWORD:
        ACCESS = True

if ACCESS == True:
    print 'Access granted.'
else:
    print 'Access is denied, please try again later.'