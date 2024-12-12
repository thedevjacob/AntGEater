"""
CourseList Set-Up
"""
from soft.API_calls import get_average_gpa


class CourseList:
    """
    Sets up a CourseList built upon Schools, Departments, and Courses

    CourseList Hierarchy ('->' contains, '!' start, '.' end)
    - ! Schools -> Departments
    - Departments -> Courses
    - Courses -> Sections.
    """
    def __init__(self, json):
        self.list_json = json

        # info to get set up
        self.schools = []

        # set up
        self.set_up_list()

    # set up list
    def set_up_list(self):
        self.set_up_schools(self.list_json['schools'])

    # set up schools
    def set_up_schools(self, schools):
        for school in schools:
            school_added = School(school)
            self.schools.append(school_added)
            school_added.departments = self.set_up_departments(school_added.departments, school_added)

    # set up departments
    def set_up_departments(self, departments, school) -> list:
        all_departments = []
        for department in departments:
            department_added = Department(department, school)
            all_departments.append(department_added)
            department_added.courses = self.set_up_courses(department_added.courses, department_added)
        return all_departments

    # set up courses
    def set_up_courses(self, courses, department) -> list:
        all_courses = []
        for course in courses:
            course_added = Course(course, department)
            all_courses.append(course_added)
            course_added.sections = self.set_up_sections(course_added.sections, course_added)
        return all_courses

    # set up sections
    def set_up_sections(self, sections, course) -> list:
        all_sections = []
        for section in sections:
            section_added = Section(section, course)
            all_sections.append(section_added)
        return all_sections

    def get_lectures(self) -> tuple:
        """
        goes through every school, department,
        course, and section to get a tuple of all
        lectures. *ONLY LECTURES*
        :return: tuple of all lectures in the CourseList
        """
        return tuple(
            section
            for school in self.schools
            for department in school.departments
            for course in department.courses
            for section in course.sections
            if section.is_lecture()
        )

    def get_course_list(self) -> list:
        all_lectures = self.get_lectures()
        open_lectures = [
            lecture for lecture in all_lectures
            if not lecture.full() and lecture.get_gpa() and not lecture.restrictions]
        open_lectures.sort(key = lambda item: item.get_gpa(), reverse = True)
        return open_lectures

class School:
    def __init__(self, school):
        self.name = school['schoolName']
        self.departments = school['departments']

class Department:
    def __init__(self, department, school):
        self.school = school
        self.code = department['deptCode']
        self.name = department['deptName']
        self.courses = department['courses']

class Course:
    def __init__(self, course, department):
        self.department = department
        self.title = course['courseTitle']
        self.department_code = course['deptCode']
        self.number = course['courseNumber']
        self.sections = course['sections']

class Section:
    def __init__(self, section, course):
        # course info
        self.course = course
        self.average_gpa = -1

        # section info
        self.code = section['sectionCode']
        self.type = section['sectionType']
        self.number = section['sectionNum']
        self.units = section['units']

        # specific specs
        self.instructors = section['instructors']
        self.meetings = section['meetings']
        self.final = section['finalExam']

        # capacity
        self.max_capacity = section['maxCapacity']
        self.num_enrolled = section['numCurrentlyEnrolled']
        self.nun_waitlist = section['numOnWaitlist']

        # restrictions
        self.restrictions = section['restrictions']
        self.status = section['status']
    def is_lecture(self) -> bool:
        return self.type == 'Lec'
    def full(self) -> bool:
        return self.status != "OPEN"
    def get_gpa(self) -> float:
        if self.average_gpa == -1:
            self.average_gpa = get_average_gpa(self.code)
        return self.average_gpa