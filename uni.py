#!/usr/bin/env python3
# coding=utf-8

import os
import sys
import course

UNI_DIR = os.getenv("HOME") + "/Documents/uni"
OPTIONS = """\
[l] - list courses
[n] - create new course
[c] - copies all files from downloads to course
[w] - work on existing course
[q] - quit program"""

def line():
    print("-" * 79)

def prompt():
    x = input("Enter command: ")
    return x

def create_courses():
    course_list = []
    print("Initializing COURSES:")
    for x in os.listdir(UNI_DIR):
        if x.startswith(".") is False:
            y = (x, course.Course(UNI_DIR, x))
            course_list.append(y)
    return course_list

def list_courses(mylist):
    for x, y in enumerate(mylist):
        print("[" + str(x) + "]", y[0])

line()
print("Welcome sir!")

if not os.path.exists(UNI_DIR):
    print("It appears your uni folder does not exist.")
    os.mkdir(UNI_DIR)
    print("Created:",  UNI_DIR)

COURSES = create_courses()

if COURSES == {}:
    line()
    print("It appears no courses exist.")
    while True:
        print("Would you like to create one? [y/n]")
        i = prompt()
        if i == "y":
            line()
            print("What would you like to name your course?")
            x = prompt()
            y = (x, course.Course(UNI_DIR, x))
            COURSES.append(y)
            COURSES.sort()
            break
        elif i == "n":
            print("As you wish sir! Goodbye.")
            quit()
        else:
            line()
            print("Sorry, please answer with [y]es or [n]o!")

while True:
    line()
    print("How can I help you sir?")
    COMMAND = prompt()
    if COMMAND == "l":
        line()
        list_courses(COURSES)
    elif COMMAND == "n":
        line()
        print("What would you like to name your course?")
        x = prompt()
        y = (x, course.Course(UNI_DIR, x))
        COURSES.append(y)
        COURSES.sort()
    elif COMMAND == "c":
        line()
        print("Which course would you like to copy your file to?")
        list_courses(COURSES)
        x = int(prompt())
        line()
        y = COURSES[x]
        y[1].copy_from_download()
        print("Finished copying!")
    elif COMMAND == "o":
        line()
        print("Which course would you like to work on?")
        list_courses(COURSES)
        x = int(prompt())
        y = COURSES[x]
        line()
        y[1].work_on()
    elif COMMAND == "q":
        line()
        print("As you wish sir! Goodbye.")
        quit()
    else:
        line()
        print("Sorry, I do not know that command.")
        print(OPTIONS)

