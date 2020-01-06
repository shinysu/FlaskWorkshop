from flask import Flask, render_template,request,redirect,url_for
from db_operations import get_tasks, add_tasks

app = Flask(__name__)


@app.route('/')
def index():
    tasks = get_tasks()
    print("getting",tasks)
    return render_template('task.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    task = request.form['new_item']
    print(task)
    add_tasks(task)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)