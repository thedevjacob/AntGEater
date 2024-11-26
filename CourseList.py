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
        self.departments = []
        self.courses = []

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
            self.set_up_departments(school_added.departments)

    # set up departments
    def set_up_departments(self, departments):
        for department in departments:
            department_added = Department(department)
            self.departments.append(department_added)
            self.set_up_courses(department_added.courses)

    # set up courses
    def set_up_courses(self, courses):
        for course in courses:
            course_added = Course(course)
            self.courses.append(course_added)

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