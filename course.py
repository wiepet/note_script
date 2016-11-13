#!/usr/bin/env python3
# coding=utf-8

import os
import datetime
import subprocess

class Course:
    """Creates a course object.

    Attributes: name of the course."""
    def __init__(self, home_directory, name):
        self.home_directory=home_directory
        self.name=name
        directory = home_directory + "/" + name
        note_file = directory + "/notes" + name + ".md"

    def current_time():
        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M")

    def create():
        """Create the course folders notes, slides"""
        os.mkdir(directory)
        os.mkdir(directory + "/notes")
        os.mkdir(directory + "/slides")

        header_file = open(os.getcwd() + "course_layout.md", "r")
        header = header_file.read()
        header_file.close()

        note_in = open(note_file)
        note_in.write(header.format(name.title(), current_time()))
        note_in.close()

    def work():
        """Appends date and time to notes file and opens it using VIM"""
        work_layout_file = open(os.getcwd() + "work_layout.md", "r")
        header = work_layout_file.read()
        work_layout_file.close()

        note_file = open(directory + "/notes/" + name + ".md", "a")
        note_file.write(header.format(current_time()))
        note_file.close()

        subprocess.run("vim " + note_file)

    def copy_from_download():
        """Copys all files from download folder to slides"""
        pass
