#!/usr/bin/env python3
# coding=utf-8

import os
import datetime
import subprocess

class Course:
    """Creates a course object.

    Attributes: name of the course."""
    def __init__(self, home_directory, name):
        self.name = name
        self.directory = home_directory + "/" + name
        self.notes_folder = self.directory + "/notes"
        self.note_file = self.notes_folder + "/" + name + ".md"
        self.slides_folder = self.directory + "/slides"

# Create folders and files of course
        if os.path.exists(self.directory) is False:
            os.mkdir(self.directory)
            print("Created " + self.directory)

        if os.path.exists(self.notes_folder) is False:
            os.mkdir(self.notes_folder)
            print("Created " + self.notes_folder)

        if os.path.exists(self.slides_folder) is False:
            os.mkdir(self.slides_folder)
            print("Created " + self.slides_folder)

        if os.path.exists(self.note_file) is False:
            header_file = open(os.path.dirname(os.path.realpath(__file__)) + "/course_layout.md", "r")
            header = header_file.read()
            header_file.close()
            note_file = open(self.note_file, "w")
            note_file.write(header.format(self.name.title(), self.current_time()))
            note_file.close()

        print("Course", self.name, "initialized.")


    def current_time(self):
        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M")
        return time

    def work_on(self):
        """Appends date and time to notes file and opens it using VIM

        Additionally opens all files in /slides folder."""
        # Open slides
        if not os.path.exists(self.slides_folder):
            self.new_course()

        all_files = []
        for x in os.listdir(self.slides_folder):
            if not x.startswith("."):
                full_path = self.slides_folder + "/" + x
                all_files.append(full_path)

        if all_files == []:
            print("No files found in /slides.")
        else:
            for x in all_files:
                print("Opening", x, ".")
                subprocess.run(["open", x])

        # Open notes
        if not os.path.exists(self.note_file):
            self.new_course()

        header_file = open(os.path.dirname(os.path.realpath(__file__)) + "/work_layout.md", "r")
        header = header_file.read()
        header_file.close()
        print("Getting header from: " + os.path.dirname(os.path.realpath(__file__)) + "/work_layout.md")

        note_file = open(self.note_file , "a")
        note_file.write(header.format(self.current_time()))
        note_file.close()
        print("Added header to " + self.note_file)

        subprocess.run(["vim", self.note_file])
        print("Opening " + self.note_file)

    def copy_from_download(self):
        """Copys all files from download folder to slides"""
        downloadfolder = os.getenv("HOME") + "/Downloads"
        for x in os.listdir(downloadfolder):
            if not x.startswith("."):
                file_from = downloadfolder + "/" + x
                file_to = self.slides_folder + "/" + x
                subprocess.run(["cp", file_from, file_to])
                print(x + " was copied to " + self.slides_folder)


