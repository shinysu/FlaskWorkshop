from flask import Flask, render_template,request,redirect,url_for
from db_operations import get_tasks, add_tasks,edit_task

app = Flask(__name__)


@app.route('/')
def index():
    tasks = get_tasks()
    return render_template('task.html', tasks=tasks, task_id=0, task_name="")


@app.route('/modify/<task_id>', methods=['POST'])
def modify(task_id):
    print(task_id)
    new_task = request.form['new_item']
    if request.form['operation'] == "add":
        add_tasks(new_task)
    elif request.form['operation'] == "edit":
        task_id = int(task_id)
        edit_task(task_id,new_task)
    return redirect(url_for('index'))


@app.route('/edit/<task_id>/<task_name>')
def edit(task_id, task_name):
    tasks = get_tasks()
    print("task_id",task_id)
    print("task_name",task_name)
    return render_template('task.html', task_id=task_id, task_name=task_name, tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True)