import os
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from config import config
from forms import TaskCreate
from flask_sqlalchemy import SQLAlchemy


app_config = config[os.getenv('FLASK_ENV') or 'default']
app = Flask(__name__)
app.config.from_object(app_config)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

from models import Todo
db.create_all()


@app.route('/', methods=['GET', 'POST'])
def dashboard():

    form = TaskCreate()
    if form.is_submitted():
        new_task = Todo(name=form.name.data,
                        description=form.description.data)
        db.session.add(new_task)
        db.session.commit()
    tasks = Todo.query.all()

    return render_template('dashboard.jinja2',
                           ip_address=request.host[:request.host.find(':')],
                           version=app_config.VERSION,
                           tasks=tasks,
                           form=form,
                           db_host=app_config.MSSQL_HOST,
                           db_name=app_config.MSSQL_DB)


if __name__ == '__main__':
    app.run()
