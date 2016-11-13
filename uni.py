#!/usr/bin/env python3
# coding=utf-8

import os
import course

UNI_DIR = os.getenv("HOME") + "/Documents/uni"
ALL_FOLDERS = os.listdir(UNI-DIR)
COUSE_FOLDERS = []

def start():
    """Initiate program.

    Also checks if the uni directory exists."""
    if os.path.exists(UNI_DIR):
        break
    else:
        print("""It appears your uni folder does not exist.
        Would you like to create one?[y/n]""")
        user_in = input("Enter command: ")
        if user_in == "y" or "yes":
            os.mkdir(UNI_DIR)
        elif user_in == "n" or "no":
            print("As you wish sir. Goodbye!")
            quit()
        else:
            print("Sorry please answer with [y]es or [n]o!")
            start()

def goodbye():
    """Prompt for quitiing."""
    prompt = "Are you sure you would like to quit sir? [y/n]"
    user_in = input("Enter command: ")
    if user_in == y:
        quit()
    elif user_in == n:
        break
    else:
        print("Sorry I don't know that command.")
        goodbye()

def list_courses():
    for x in COURSE_FOLDERS:
        print(x)

print("Welcome sir!")

start()

# Only select non hidden folders
for x in ALL_FOLDERS:
    if not x.startswith(".")
        COURSE_FOLDERS.append(x)

# Create a Course object for each folder in uni
COURSES = {}
for x in COURSE_FOlDERS:
    COURSES[x] = Course(UNI_DIR, x)

while True:
    print("How can I help you sir?")
    USER_IN = input("Enter command: ")
    if USER_IN == "l":
        list_courses()
    elif USER_IN == "c":
        COURSE_NAME = input("Enter course name: ")
        COURSES[COURSE_NAME] = Course(UNI_DIR, COURSE_NAME)
    elif USER_IN == "w":
        print("Which course would you like to work on?")
        list_courses()
        WORK_ON = input("Enter course name: ")
        for x in COURSES[x]:
            if x == WORK_ON:
                COURSES[x].work()
    elif USER_IN == "q":
        goodbye()
    else:
        print("Sorry I don't know that command sir."
        print("""[l] - list courses
        [c] - create new course
        [w] - work on existing course
        [q] - quit program"""




