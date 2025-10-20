import yaml
import logging 
import logging.config 
from pathlib import Path
import os
import sys

# Add parent directory to path to find utils module
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

try:
    from utils.utils import create_dir
except ImportError:
    # Fallback function if utils module is not available
    def create_dir(path):
        os.makedirs(path, exist_ok=True)


def setup_logging(log_dir, config_fpath="logger_config.yml"):
    create_dir(log_dir)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    log_config = Path(config_fpath)
    if log_config.is_file():
        with open(log_config, "r") as f:
            config = yaml.safe_load(f.read())
            # modify logging paths based on log_dir
            for __, handler in config["handlers"].items():
                if "filename" in handler:
                    handler["filename"] = "/".join([log_dir, handler["filename"]])

        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)
        print(f"Warning: logging configuration file is not found in {log_config}.")

def get_logger(name):
    return logging.getLogger(name)