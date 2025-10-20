from .log import setup_logging, get_logger

# Create a log object that can be imported directly
class LogManager:
    def __init__(self):
        self._setup_done = False
    
    def setup_logging(self, log_dir, config_fpath="logger_config.yml"):
        """Setup logging configuration"""
        from .log import setup_logging as _setup_logging
        _setup_logging(log_dir, config_fpath)
        self._setup_done = True
    
    def get_logger(self, name):
        """Get a logger instance"""
        from .log import get_logger as _get_logger
        return _get_logger(name)

# Create a singleton instance
log = LogManager()
