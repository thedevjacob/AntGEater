"""
CourseList Set-Up
"""


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
            school_added.departments = self.set_up_departments(school_added.departments)

    # set up departments
    def set_up_departments(self, departments) -> list:
        all_departments = []
        for department in departments:
            department_added = Department(department)
            all_departments.append(department_added)
            department_added.courses = self.set_up_courses(department_added.courses)
        return all_departments

    # set up courses
    def set_up_courses(self, courses) -> list:
        all_courses = []
        for course in courses:
            course_added = Course(course)
            all_courses.append(course_added)
            course_added.sections = self.set_up_sections(course_added.sections)
        return all_courses

    # set up sections
    def set_up_sections(self, sections) -> list:
        all_sections = []
        for section in sections:
            section_added = Section(section)
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

class School:
    def __init__(self, school):
        self.name = school['schoolName']
        self.departments = school['departments']

class Department:
    def __init__(self, department):
        self.code = department['deptCode']
        self.name = department['deptName']
        self.courses = department['courses']

class Course:
    def __init__(self, course):
        self.title = course['courseTitle']
        self.department_code = course['deptCode']
        self.number = course['courseNumber']
        self.sections = course['sections']

class Section:
    def __init__(self, section):
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
    def is_full(self) -> bool:
        return self.status == "OPEN"