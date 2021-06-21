from flask import Flask


def init_app(app: Flask):
    from .blog_post_views import bp as bp_blog_posts

    app.register_blueprint(bp_blog_posts)
