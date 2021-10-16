from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from datetime import datetime


@app.route("/")
def show_entries():
    entries = [
        {"id": 1, "title": "初めての投稿", "text": "初めての内容", "created_at": datetime.now()},
        {"id": 2, "title": "2つめの投稿", "text": "2つめの内容", "created_at": datetime.now()},
    ]

    return render_template("entries/index.html", entries=entries)


@app.route("/entries", methods=["POST"])
def add_entry():
    return "新しい記事が登録されました"


@app.route("/entries/new", methods=["GET"])
def new_entry():
    return render_template("entries/new.html")
    # return "記事の入力フォームを表示"


@app.route("/entries/<int:id>", methods=["GET"])
def show_entry(id):
    entry = {"id": 1, "title": "初めての投稿", "text": "初めての内容", "created_at": datetime.now()}

    return render_template("entries/show.html", entry=entry)


@app.route("/entries/<int:id>/edit", methods=["GET"])
def edit_entry(id):
    return f"記事{id}の編集フォームを表示"


@app.route("/entries/<int:id>/update", methods=["POST"])
def update_entry(id):
    return f"記事{id}が更新されました"


@app.route("/entries/<int:id>/delete", methods=["POST"])
def delete_entry(id):
    return f"記事{id}が削除されました"
