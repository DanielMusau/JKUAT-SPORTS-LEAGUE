from flask import render_template, request, Blueprint
from JSL.models import Team
from flask_login import login_required


main = Blueprint('main', __name__)


@main.route('/')  
@main.route('/home')
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    teams = Team.query.paginate(page=page, per_page=6)
    return render_template("home.html", teams=teams)

@main.route('/about') 
def about():
    return render_template("about.html",  title= 'About')
