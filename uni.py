#!/usr/bin/env python3
# coding=utf-8

import os
import sys

UNI_DIR = os.getenv("HOME") + "/Documents/uni"

if os.path.exists(UNI_DIR + "/" + course):
    pass
else:
    course.create()
