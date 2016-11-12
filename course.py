#!/usr/bin/env python3
# coding=utf-8

import os
import datetime

class Course:
    """Creates a course object.

    Attributes: name of the course."""
    def __init__(self, home_directory, name, teacher):
        self.home_directory=home_directory
        self.name=name
        self.teacher=teacher
        directory = directory + "/" + name

    def create():
        """Create the course folders notes, slides"""
        os.mkdir(directory)
        os.mkdir(directory + "/notes")
        os.mkdir(directory + "/slides")

        header_file = open(os.getcwd() + "course_layout.md", "r")
        header = header_file.read()
        header_file.close()

        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M")

        note_file = open(directory + "/notes/" + name + ".md", "c")
        note_file.write(header.format(name.title(), time, teacher))
        note_file.close()

    def work():
        """Appends date and time to notes file and opens it using VIM"""
        work_layout_file = open(os.getcwd() + "work_layout.md", "r")
        header = work_layout_file.read()
        work_layout_file.close()

        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M")

        note_file = open(directory + "/notes/" + name + ".md", "a")
        note_file.write(header.format(time, teacher))
        note_file.close()

        # TODO: Create subprocess for VIM

    def copy_from_download():
        """Copys all files from download folder to slides"""
