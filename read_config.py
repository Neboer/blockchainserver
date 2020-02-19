from json import load


def get_config():
    with open("secret.json") as config_file:
        json_data = load(config_file)
    return json_data