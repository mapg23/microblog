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

@bp.app_errorhandler(418)
def teapot_error(error):
    """Handle the I'm a teapot error"""
    app_errors.labels(type="418").inc()
    return "I'm a teapot ☕", 418

@bp.app_errorhandler(Exception)
def unhandled_exception(error):
    """
    Catch-all for unexpected exceptions (5xx)
    """
    current_app.logger.exception(error)
    app_errors.labels(type="exception").inc()
    db.session.rollback()
    raise error
