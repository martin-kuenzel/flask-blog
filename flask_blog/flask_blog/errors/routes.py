from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@errors.app_errorhandler(400)
def error_400(error):
    return render_template('errors/400.html'), 400

@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(418)
def error_418(error):
    return render_template('errors/418.html'), 418

@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500
