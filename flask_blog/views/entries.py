from flask_blog import app


@app.route("/")
def show_entries():
    return "hello world!"
