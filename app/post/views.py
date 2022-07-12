from flask import Blueprint, render_template,request

post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')


@post_blueprint.route('/posts/<postid>')
def post_page():

    return render_template('post.html')
