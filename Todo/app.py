from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Modify the task list to store tasks as dictionaries with a 'completed' status
tasks = [
    {"name": "Example task", "completed": False}
]

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    new_task = request.form.get("new_task")
    if new_task:
        tasks.append({"name": new_task, "completed": False})  # New task is not completed by default
    return redirect(url_for("home"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("home"))

@app.route("/update/<int:task_id>", methods=["GET", "POST"])
def update_task(task_id):
    if request.method == "POST":
        updated_task = request.form.get("updated_task")
        if updated_task and 0 <= task_id < len(tasks):
            tasks[task_id]["name"] = updated_task  # Update the task name
        return redirect(url_for("home"))
    return render_template("update.html", task=tasks[task_id]["name"], task_id=task_id)

@app.route("/done/<int:task_id>")
def mark_done(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True  # Mark the task as done
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
