from json import load


def get_config():
    file = 'config.json'
    with open(file) as config:
        config = load(config)
    return config
