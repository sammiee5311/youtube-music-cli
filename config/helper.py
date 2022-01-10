import os

from dotenv import load_dotenv

PATH = "config"
ENV_PATH = os.path.join(PATH, ".env")


def load_env() -> None:
    load_dotenv(dotenv_path=ENV_PATH)
