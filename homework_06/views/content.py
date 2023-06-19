from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import render_template
from flask import flash

from models import db, Content
from .forms.contents import ContentForm


content_app = Blueprint(
    "content_app",
    __name__,
    url_prefix="/content",
)


@content_app.get("/", endpoint="list")
def get_content_list():
    things: list[Content] = Content.query.order_by(Content.id).all()
    return render_template("content/list.html", things=things)


def get_content_by_id(content_id: int) -> Content:
    return Content.query.get_or_404(
        content_id,
        description=f"Product #{content_id} not found!",
    )


@content_app.get("/<int:content_id>/", endpoint="details")
def get_product_details(content_id: int):
    thing = get_content_by_id(content_id=content_id)
    return render_template("content/details.html", thing=thing)


@content_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def create_new_thing():
    form = ContentForm()
    if request.method == "GET":
        return render_template("content/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("content/add.html", form=form), 400

    thing = Content(name=form.data["name"])
    db.session.add(thing)
    db.session.commit()
    url = url_for("content_app.details", content_id=thing.id)
    flash(f"Created thing {thing.name!r}", category="success")
    # flash(f"Created product {product.name!r}")
    return redirect(url)


@content_app.route(
    "/<int:content_id>/confirm-delete/",
    methods=["GET", "POST"],
    endpoint="confirm-delete",
)
def confirm_delete_thing(content_id: int):
    thing = get_content_by_id(content_id=content_id)
    if request.method == "GET":
        return render_template("content/confirm-delete.html", thing=thing)

    thing_name = thing.name
    db.session.delete(thing)
    db.session.commit()
    flash(f"Deleted thing {thing_name!r}", category="warning")
    url = url_for("content_app.list")
    return redirect(url)
