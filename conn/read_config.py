from json import load


def get_config():
    with open("config.json") as config:
        config = load(config)
    return config
