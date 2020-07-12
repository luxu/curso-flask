from flask import request, render_template
from flask import Blueprint
from flask import current_app

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    print("entrei na função main")
    current_app.logger.debug("Entrei na função main")
    return render_template("index.html")


@bp.route("/sobre")
def about():
    return render_template("about.html")

@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")