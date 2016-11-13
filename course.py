#!/usr/bin/env python3
# coding=utf-8

import os
import datetime
import subprocess

class Course:
    """Creates a course object.

    Attributes: name of the course."""
    def __init__(self, home_directory, name):
        self.home_directory = home_directory
        self.name = name
        Course.directory = home_directory + "/" + name
        Course.note_file = Course.directory + "/notes/" + name + ".md"

    def current_time(self):
        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M")
        return time

    def new_course(self):
        """Create the course folders notes, slides"""
        os.mkdir(self.directory)
        os.mkdir(self.directory + "/notes")
        os.mkdir(self.directory + "/slides")

        header_file = open(os.getcwd() + "/course_layout.md", "r")
        header = header_file.read()
        header_file.close()

        note_in = open(self.note_file, "w")
        note_in.write(header.format(self.name.title(), self.current_time()))
        note_in.close()

    def work(self):
        """Appends date and time to notes file and opens it using VIM"""
        work_layout_file = open(os.getcwd() + "/work_layout.md", "r")
        header = work_layout_file.read()
        work_layout_file.close()

        if os.path.exists(self.note_file) == False:
            note_in = open(self.note_file, "w")
            note_in.write(header.format(self.name.title(), self.current_time()))
            note_in.close()
        else:
            note_file = open(self.directory + "/notes/" + self.name + ".md", "a")
            note_file.write(header.format(self.current_time()))
            note_file.close()

        subprocess.call(["vim", self.note_file])

    def copy_from_download(self):
        """Copys all files from download folder to slides"""
        pass
