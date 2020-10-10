import yaml

def read_creds(conf_path):
    with open(conf_path, 'r') as cf:
        config = yaml.load(cf, Loader=yaml.FullLoader)
        return config
