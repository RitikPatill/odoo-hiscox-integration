import logging

_logger = logging.getLogger(__name__)

def log_error(message):
    """Logs errors in Odoo's server logs."""
    _logger.error(message)
