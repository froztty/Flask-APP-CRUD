from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer, default=0) # 1 yes or 0 no
    created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route("/", methods=["POST","GET"])
def index():
    #add a task
    if request.method == "POST":
        current_task = request.form['content']
        new_task = MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"ERROR: {e}")
            return (f"ERROR: {e}")
    #see all current tasks
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()
    
    

if __name__ in "__main__":
    app.run(debug=True)