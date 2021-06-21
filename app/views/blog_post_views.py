from flask import Blueprint, request, render_template, redirect, jsonify
from app import db
from ipdb import set_trace
from app.models.blog_post_model import BlogPostModel
from datetime import datetime

bp = Blueprint("bp_posts_route", __name__, url_prefix="/api")


@bp.get("")
def all_posts():
    posts =  BlogPostModel.query.all()

    if not posts:
        return render_template("no_posts.html"), 200


    return render_template("posts.html", posts=posts), 200


@bp.post("/posts")
def create_post():

    data = {
        "post_name": request.form.get("post_name"),
        "genre": request.form.get("genre"),
        "content": request.form.get("content"),
        "image_url": request.form.get("image_url"),
        "creator_name": request.form.get("creator_name"),
        "creator_email": request.form.get("creator_email")
    }

    null_fields = [key for key, value in data.items() if not value]
    if null_fields:
        return {"error": {"missing_keys": null_fields}}, 400

    data["creation_date"] = datetime.now()




    post = BlogPostModel(**data)

    db.session.add(post)
    db.session.commit()


    return redirect("/api")


@bp.get("/posts/<int:post_id>")
def get_post(post_id):
    post = BlogPostModel.query.get(post_id)

    if not post:
        return render_template("not_found.html"), 404

    return render_template("posts.html", posts=[post])


@bp.post("/posts/search")
def create_search():
    search = request.form.get("search")

    if search:
        return redirect(f"/api/posts/{search}")

    return redirect("/api")


@bp.get("/posts")
def post_form():

    return render_template("create_post_form.html"), 200
