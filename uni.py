#!/usr/bin/env python3
# coding=utf-8

import os
import sys

#course.py module
import course

UNI_DIR = os.getenv("HOME") + "/Documents/uni"
COURSE_FOLDERS = []
LINE = "-" * 79
OPTION_LIST = """\
[l] - list courses
[c] - create new course
[w] - work on existing course
[q] - quit program"""


def start():
    """Initiate program.

    Also checks if the uni directory exists."""
    if os.path.exists(UNI_DIR):
        pass
    else:
        print("""It appears your uni folder does not exist.
        Would you like to create one?[y/n]""")
        user_in = input("Enter command: ")
        if user_in == "y":
            os.mkdir(UNI_DIR)
        elif user_in == "n":
            print("As you wish sir. Goodbye!")
            sys.exit()
        else:
            print("Sorry please answer with [y]es or [n]o!")
            start()

def goodbye():
    """Prompt for quitiing."""
    print(LINE)
    print("Are you sure you would like to quit sir? [y/n]")
    user_in = input("Enter command: ")
    if user_in == "y":
        quit()
    elif user_in == "n":
        pass
    else:
        print("Sorry I don't know that command.")
        goodbye()

def update_folders():
    """Selects all non hidden folders"""
    ALL_FOLDERS = os.listdir(UNI_DIR)
    COURSE_FOLDERS[:] = []
    for x in ALL_FOLDERS:
        if not x.startswith("."):
            COURSE_FOLDERS.append(x)


def list_courses():
    print(LINE)
    if COURSE_FOLDERS == []:
        print("No courses have been defined yet.")
    else:
        for x in COURSE_FOLDERS:
            print(x)
    print(LINE)

print(LINE)
print("Welcome sir!")

start()

#Store all folder names
update_folders()

# Create a Course object for each folder in uni
COURSES = {}
for x in COURSE_FOLDERS:
    COURSES[x] = course.Course(UNI_DIR, x)

while True:
    print("How can I help you sir?")
    USER_IN = input("Enter command: ")
    if USER_IN == "l":
        list_courses()
    elif USER_IN == "c":
        COURSE_NAME = input("Enter course name: ")
        COURSES[COURSE_NAME] = course.Course(UNI_DIR, COURSE_NAME)
        COURSES[COURSE_NAME].new_course()
        update_folders()
    elif USER_IN == "w":
        print("Which course would you like to work on?")
        list_courses()
        WORK_ON = input("Enter course name: ")
        for x in COURSES:
            if x == WORK_ON:
                COURSES[x].work()
    elif USER_IN == "q":
        goodbye()
    else:
        print(LINE)
        print("Sorry I don't know that command sir.")
        print(OPTION_LIST)
        print(LINE)


