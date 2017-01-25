from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    rows = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
        first=first,
        last=last,
        github=github,
        rows=rows)
    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/new_student")
def new_student():
    """Add a student."""

    return render_template("student_add.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""
    first_name = request.form.get('firstname')
    last_name = request.form.get('lastname')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("student_confirm.html",
        github=github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
