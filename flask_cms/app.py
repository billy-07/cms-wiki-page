from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    contents = Content.query.all()
    return render_template('index.html', contents=contents)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        new_content = Content(title=title, body=body)
        db.session.add(new_content)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:content>', methods=['POST'])
def edit_task(task_id):
    new_text = request.form['updated_content']
    return #not finished

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
