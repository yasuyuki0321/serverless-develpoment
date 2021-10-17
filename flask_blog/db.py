from flask_blog.models.entries import Entry
from flask.cli import with_appcontext
import click


def init_db():
    if not Entry.exists():
        Entry.create_table(read_capacity_units=1, write_capacity_units=1)

@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')



# from flask_script import Command
# from flask_blog.models.entries import Entry


# class InitDB(Command):
#     "create database"

#     def run(self):
#         if not Entry.exists():
#             Entry.create_table(read_capacity_units=1, write_capacity_units=1)



# from flask_script import Manager
# from flask_blog import app
# from flask_blog.scripts.db import InitDB


# if __name__ == "__main__":
#     manager = Manager(app)
#     manager.add_command("init_db", InitDB)
#     manager.run()
