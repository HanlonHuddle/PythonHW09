"""
    Repo Class to hold all the data in single place
    Hanrun Li
"""

import collections
from os import chdir
import prettytable

class Student:
    """ class Student"""
    def __init__(self, cwid, name, department):
        self.cwid = cwid
        self.name = name
        self.department = department
        self.classes_taken = collections.defaultdict(str)
        # <string -> string>
        # defaultdict(str) to store the classes taken and the grade where the course
        # is the key and the grade is the value.

class Instructure:
    """ class Instructure"""
    def __init__(self, cwid, name, department):
        self.cwid = cwid
        self.name = name
        self.department = department
        self.classes_taught = collections.defaultdict(int)
        # classes_taught = collections.defaultdict(int)
        # <string -> int>
        # defaultdict(int) to store the names of the courses
        # taught along with the number of students

class Major:
    """ class Major """
    def __init__(self, department):
        self.department = department
        self.required = []
        self.elective = []

class Repository:
    """ class repository """
    studentDict = {}
    # list of students
    instructureDict = {}
    # list of instructures
    majorsDict = {}

    # def __init__(self):
    #     """ nothing special """

    def load(self, directory):
        """ function to read in data and load """
        flist = ["students.txt", "instructors.txt", "grades.txt", "majors.txt"]
        chdir(directory)

        # read in student info
        try:
            fprocess = open(flist[0], 'r')
        except FileNotFoundError:
            print("Can't open", flist[0])
        else:
            with fprocess:
                for line in fprocess:
                    tuparr = line.strip().split('\t')
                    self.studentDict[tuparr[0]] = Student(tuparr[0], tuparr[1], tuparr[2])

        # read in instructures info
        try:
            fprocess = open(flist[1], 'r')
        except FileNotFoundError:
            print("Can't open", flist[1])
        else:
            with fprocess:
                for line in fprocess:
                    tuparr = line.strip().split('\t')
                    self.instructureDict[tuparr[0]] = Instructure(tuparr[0], tuparr[1], tuparr[2])

        # read in grades info and update students and instructures
        try:
            fprocess = open(flist[2], 'r')
        except FileNotFoundError:
            print("Can't open", flist[2])
        else:
            with fprocess:
                for line in fprocess:
                    tuparr = line.strip().split('\t')
                    if len(tuparr) == 4:
                        self.studentDict[tuparr[0]].classes_taken[tuparr[1]] = tuparr[2]
                        self.instructureDict[tuparr[3]].classes_taught[tuparr[1]] += 1
                    else:
                        self.studentDict[tuparr[0]].classes_taken[tuparr[1]] = "NA"
                        self.instructureDict[tuparr[2]].classes_taught[tuparr[1]] += 1

        # read in major info and update students
        try:
            fprocess = open(flist[3], 'r')
        except FileNotFoundError:
            print("Can't open", flist[3])
        else:
            with fprocess:
                for line in fprocess:
                    tuparr = line.strip().split('\t')
                    if tuparr[0] in self.majorsDict:
                        if tuparr[1] == "E":
                            self.majorsDict[tuparr[0]].elective.extend(tuparr[2])
                        elif tuparr[1] == "R":
                            self.majorsDict[tuparr[0]].required.extend(tuparr[2])

        return [self.studentDict, self.instructureDict]

    def print_table(self):
        """ Method to print the result """
        ptable = prettytable.PrettyTable()
        ptable.field_names = ["CWID", "Name", "Complited Cources"]
        for _id in self.studentDict:
            ptable.add_row(
                [self.studentDict[_id].cwid,
                 self.studentDict[_id].name,
                 sorted(list(self.studentDict[_id].classes_taken))]
            )

        ptable2 = prettytable.PrettyTable()
        ptable2.field_names = ["CWID", "Name", "Dept", "Cource", "Students"]
        for _id in self.instructureDict:
            for course in self.instructureDict[_id].classes_taught:
                ptable2.add_row(
                    [self.instructureDict[_id].cwid,
                     self.instructureDict[_id].name,
                     self.instructureDict[_id].department,
                     course,
                     self.instructureDict[_id].classes_taught[course]]
                )

        ptable3 = prettytable.PrettyTable()
        ptable3.field_names = ["Dept", "Required", "Elective"]
        for dept in self.majorsDict:
            ptable3.add_row(
                [self.majorsDict[dept].name,
                 self.majorsDict[dept].required,
                 self.majorsDict[dept].elective]
            )

        # result[file_name] = subdic
        print("\nMajor Summary")
        print(ptable3)
        print("\nStudent Summary")
        print(ptable)
        print("\nInstructure Summary")
        print(ptable2)
        # return result

        return [ptable.get_string(), ptable2.get_string()]
