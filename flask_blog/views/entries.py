from flask_blog import app


@app.route("/")
def show_entries():
    return "全ての記事を表示"


@app.route("/entries", methods=["POST"])
def add_entry():
    return "新しい記事が登録されました"


@app.route("/entries/new", methods=["GET"])
def new_entry():
    return "記事の入力フォームを表示"


@app.route("/entries/<int:id>", methods=["GET"])
def show_entry(id):
    return f"記事{id}を表示"


@app.route("/entries/<int:id>/edit", methods=["GET"])
def edit_entry(id):
    return f"記事{id}の編集フォームを表示"


@app.route("/entries/<int:id>/update", methods=["POST"])
def update_entry(id):
    return f"記事{id}が更新されました"


@app.route("/entries/<int:id>/delete", methods=["POST"])
def delete_entry(id):
    return f"記事{id}が削除されました"
