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
        self.rrequired = set()
        # remaining required, list of string
        self.relective = set()
        # remaining elective, list of string
        self.completedclasses = []

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
        self.required = set()
        self.elective = set()

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
                    if tuparr[0] not in self.majorsDict:
                        self.majorsDict[tuparr[0]] = Major(tuparr[0])
                    if tuparr[1] == "E":
                        self.majorsDict[tuparr[0]].elective.add(tuparr[2])
                    elif tuparr[1] == 'R':
                        self.majorsDict[tuparr[0]].required.add(tuparr[2])

        for _id in self.studentDict:
            dep = self.studentDict[_id].department
            deprequired = self.majorsDict[dep].required
            classestaken = set(self.studentDict[_id].classes_taken.keys())
            passrank = ["A", "A-", "B+", "B", "B-", "C+", "C"]
            remainingrequired = [i for i in deprequired
                                 if not self.studentDict[_id].classes_taken[i] in passrank]
            passedelective = classestaken.intersection(self.majorsDict[dep].elective)
            noep = len(passedelective)
            for ele in passedelective:
                if self.studentDict[_id].classes_taken[ele] not in passrank:
                    noep -= 1
            if noep == 0:
                self.studentDict[_id].relective = list(self.majorsDict[dep].elective)
            else:
                self.studentDict[_id].relective = []
            self.studentDict[_id].rrequired = remainingrequired
            # remove empty classestaken that added from above operation
            self.studentDict[_id].classes_taken = {k: v for k, v in
                                                   self.studentDict[_id].classes_taken.items() if v}
            self.studentDict[_id].completedclasses = [i for i in classestaken
                                                      if self.studentDict[_id].classes_taken[i]
                                                      in passrank]

    def print_table(self):
        """ Method to print the result """
        ptable = prettytable.PrettyTable()
        ptable.field_names = ["CWID", "Name", "Complited Cources",
                              "Remaining Required", "Remaining Elective"]
        for _id in self.studentDict:
            ptable.add_row(
                [self.studentDict[_id].cwid,
                 self.studentDict[_id].name,
                 sorted(self.studentDict[_id].completedclasses),
                 sorted(list(self.studentDict[_id].rrequired)),
                 sorted(list(self.studentDict[_id].relective))]
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
                [self.majorsDict[dept].department,
                 sorted(list(self.majorsDict[dept].required)),
                 sorted(list(self.majorsDict[dept].elective))]
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
