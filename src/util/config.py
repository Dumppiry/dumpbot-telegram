import dotenv

_config = dotenv.dotenv_values(".env")

BOT_TOKEN = _config["BOT_TOKEN"]
DEV_TOKEN = _config["DEV_TOKEN"]
