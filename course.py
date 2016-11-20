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
        self.note_file = self.note_folder + "/" + name + ".md"
        self.slides_folder = self.directory + "/slides"

    def current_time():
        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M")
        return time

    def new_course(self):
        """Create the course files

        Folders: /COURSE/notes and /COURSE/slides
        File: /COURSE/notes/COURSE.md"""
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)
            print("Created " + self.directory)
        if not os.path.exists(self.notes_folder):
            os.mkdir(self.notes_folder)
            print("Created " + self.notes_folder)
        if not os.path.exists(self.slides_folder):
            os.mkdir(self.slides_folder)
            print("Created " + self.slides_folder)
        if not os.path.exists(self.note_file)
            header_file = open(os.path.dirname(os.path.realpath(__file__)) + "/course_layout.md", "r")
            header = header_file.read()
            header_file.close()
            note_file = open(self.note_file, "w")
            note_file.write(header.format(self.name.title(), self.current_time()))
            note_file.close()

    def take_notes(self):
        """Appends date and time to notes file and opens it using VIM"""
        if not os.path.exists(self.note_file):
            self.new_course()

        header_file = open(os.path.dirname(os.path.realpath(__file__)) + "/work_layout.md", "r")
        header = header_file.read()
        header_file.close()

        note_file = open(self.note_file , "a")
        note_file.write(header.format(self.current_time()))
        note_file.close()

        subprocess.Run(["vim", self.note_file], shell=True)

    def open_slides(self):
        """Opens all files in slides folder"""
        if not os.path.exists(self.slides_folder):
            self.new_course()

        all_files = []
        for x in os.listdir(self.slides_folder):
            if not x.startswith(".")
                full_path = self.slides_folder + "/" + x
                all_files.append(full_path)

        if all_files == []:
            print("No files found in /slides.")
        else:
            subprocess.Run(["open", all_files], shell=True)

    def copy_from_download(self):
    """Copys all files from download folder to slides"""
    downloadfolder = os.getenv("HOME") + "/Downloads"
    for x in os.listdir(downloadfolder):
        if not x.startswith("."):
            file_from = downloadfolder + "/" + x
            file_to = self.slides_folder + "/" + x
            subprocess.Run(["cp", file_from, file_to])
            print(x + " was copied to " + self.slides_folder)


