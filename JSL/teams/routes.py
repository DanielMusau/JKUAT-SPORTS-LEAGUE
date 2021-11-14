from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from JSL import db
from JSL.models import Team
from JSL.teams.forms import TeamForm

teams = Blueprint('teams', __name__)


@teams.route('/team/new', methods=['GET', 'POST'])
@login_required
def new_team():
    form = TeamForm()
    if form.validate_on_submit():
        team = Team(teamname=form.teamname.data, captain = form.captain.data)
        db.session.add(team)
        db.session.commit()
        flash('Your Team has been registered successfully', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_team.html', title= 'Register Team', form=form, legend= 'Register Team')


@teams.route("/team/<int:team_id>")
def team(team_id):
    team =Team.query.get_or_404(team_id)
    return render_template('team.html', title=team.teamname, team=team)

@teams.route("/team/<int:team_id>/update", methods=['GET', 'POST'])
@login_required
def update_team(team_id):
    team = Team.query.get_or_404(team_id)
    if team.captain != current_user:
        abort(403)
    form = TeamForm()
    if form.validate_on_submit():
        team.teamname = form.teamname.data
        team.captain = form.captain.data
        db.session.commit()
        flash('You have updated your team.', 'success')
        return redirect(url_for('teams.team', team_id=team.id))
    elif request.method == 'GET': 
        form.teamname.data = team.teamname
        form.captain.data = team.captain
    return render_template('create_team.html', title= 'Update Team', form=form, legend= 'Update Team')
    

@teams.route("/team/<int:team_id>/delete", methods=['POST'])
@login_required
def delete_team(team_id):
     team = Team.query.get_or_404(team_id)
     if team.captain != current_user:
        abort(403)
     db.session.delete(team)
     db.session.commit()
     flash('The team has been deleted!', 'success')
     return redirect(url_for('main.home'))
