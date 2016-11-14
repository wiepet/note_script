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
        Course.slides_folder = Course.directory + "/slides"

    def current_time(self):
        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M")
        return time

    def new_course(self):
        """Create the course folders notes, slides"""
        if os.path.exists(self.directory) == False:
            os.mkdir(self.directory)
        if os.path.exists(self.directory + "/notes") == False:
            os.mkdir(self.directory + "/notes")
        if os.path.exists(self.directory + "/slides") == False:
            os.mkdir(self.directory + "/slides")

        header_file = open(os.path.dirname(os.path.realpath(__file__)) + "/course_layout.md", "r")
        header = header_file.read()
        header_file.close()

        note_in = open(self.note_file, "w")
        note_in.write(header.format(self.name.title(), self.current_time()))
        note_in.close()

    def take_notes(self):
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

    def open_slides(self):
        """Opens all files in slides folder"""
        if os.path.exists(self.slides_folder) == True:
            all_files = os.listdir(self.slides_folder)
            if all_files == []:
                print("No files found in /slides.")
            else:
                subprocess.call(["open", " ".join(all_files)])
#                for x in all_files:
#                    slidefile = self.slides_folder + "/" + x
#                    subprocess.call(["open", slidefile])
        else:
            print("No slides folder found!")
            os.mkdir(self.slides_folder)
            print(self.slides_folder + " created.")
            print("I created one sir!")

    def work(self):
        self.open_slides()
        self.take_notes()

    def copy_from_download(self):
        """Copys all files from download folder to slides"""
        downloadfolder = os.getenv("HOME") + "/Downloads"
        for x in os.listdir(downloadfolder):
            if x.startswith(".") == False:
                print(x + " was copied to " + self.slides_folder)
                file_from = downloadfolder + "/" + x
                file_to = self.slides_folder + "/" + x
                subprocess.call(["cp", file_from, file_to])


