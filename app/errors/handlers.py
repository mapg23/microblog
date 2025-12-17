"""
Contains error handlers
"""
from flask import render_template, current_app
from prometheus_client import Counter
from app import db
from app.errors import bp

# Prometheus counter for application errors
app_errors = Counter(
    "microblog_errors_total",
    "Total number of application errors",
    ["type"]
)

@bp.app_errorhandler(404)
def not_found_error(error):
    """
    Error handler for code 404
    """
    current_app.logger.info(error)
    app_errors.labels(type="404").inc()
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    """
    Error handler for code 500
    """
    current_app.logger.info(error)
    app_errors.labels(type="500").inc()
    db.session.rollback()
    return render_template('errors/500.html'), 500

@bp.app_errorhandler(IndexError)
def index_error_handler(_error):
    """
    Error handler for IndexError
    """
    app_errors.labels(type="IndexError").inc()
    return render_template("errors/500.html"), 500
