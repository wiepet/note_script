#!/usr/bin/env python3
# coding=utf-8

import os
import sys

#course.py module
import course

UNI_DIR = os.getenv("HOME") + "/Documents/uni"
COURSE_FOLDERS = []
LINE = "-" * 79
WORKING = 1
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
    """Prints all course folders"""
    print(LINE)
    if COURSE_FOLDERS == []:
        print("No courses have been defined yet.")
    else:
        for x in COURSE_FOLDERS:
            print(x)

def unknown_command():
    print(LINE)
    print("Sorry I don't know that command sir.")
    print(OPTION_LIST)

def create_course():
    print(LINE)
    print("Which course would you like to add?")
    COURSE_NAME = input("Enter course name: ")
    COURSES[COURSE_NAME] = course.Course(UNI_DIR, COURSE_NAME)
    COURSES[COURSE_NAME].new_course()
    update_folders()

def work_on_course():
    working = 1
    while working == 1:
        print(LINE)
        print("Which course would you like to work on?")
        list_courses()
        print(LINE)
        WORK_ON = input("Enter course name: ")
        for x in COURSES:
            if x == WORK_ON:
                COURSES[x].work()
                working = 0
        if working == 1:
            print("Sorry no course named '" + WORK_ON + "' found.")


# Initial welcome message
print(LINE)
print("Welcome sir!")

start()

#Store all folder names
update_folders()

# Create a Course object for each folder in uni
COURSES = {}
for x in COURSE_FOLDERS:
    COURSES[x] = course.Course(UNI_DIR, x)

# Keep the program in a loop
while True:
    print(LINE)
    print("How can I help you sir?")
    user_in = input("Enter command: ")
    if user_in == "l":
        list_courses()
    elif user_in == "c":
        create_course()
    elif user_in == "w":
# opens note file and slides
        work_on_course()
    elif user_in  == "q":
        goodbye()
    else:
        unknown_command()

