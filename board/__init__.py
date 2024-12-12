from flask import Flask, render_template, request
from soft import API_calls, CourseList

app = Flask(__name__)

GE_CATEGORIES = ['GE-1A', 'GE-1B', 'GE-2', 'GE-3', 'GE-4',
                 'GE-5A', 'GE-5B', 'GE-6', 'GE-7', 'GE-8']

@app.route("/")
def home():
    return render_template("index.html", ge_categories=GE_CATEGORIES)

@app.route("/ge-courses", methods=["GET"])
def ge_courses():
    # get GE category from form
    ge_category = request.args.get("ge_category")

    # create course list
    retrieved_courses = API_calls.get_all_GE_courses_web(ge_category)
    course_list = CourseList.CourseList(retrieved_courses)

    # run course search and sort
    open_courses = course_list.get_course_list()

    if not open_courses:
        message = f"No open courses found for {ge_category}."
        return render_template("courses.html", message=message, courses=[])

    return render_template("courses.html", courses=open_courses, ge_category=ge_category)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)