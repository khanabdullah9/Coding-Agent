import os
import logging
from typing import Union

logging.basicConfig(level=logging.WARNING) 

# 2. Create a specific logger for YOUR app
logger = logging.getLogger("my_app")
logger.setLevel(logging.INFO) # Your app will log INFO and above
logger.propagate = False # This prevents logs from "bubbling up" to the root logger

# 3. Add a FileHandler specifically to your logger
log_path = os.path.join(os.path.dirname(__file__), "app.log")
file_handler = logging.FileHandler(log_path, encoding="utf-8")
formatter = logging.Formatter("{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def save_png(png_data, img_name: str = None) -> None:
    path = os.path.join("GRAPH_PNG","graph.png") if img_name is None else os.path.join("GRAPH_PNG",img_name) 
    with open(path, "wb") as png:
        png.write(png_data)


def log_err(err_msg: Union[str, Exception]):
    logger.error(str(err_msg))

def log_info(msg: str):
    logger.info(msg)