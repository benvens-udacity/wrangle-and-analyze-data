import util.config as config

def test_read_creds():
    creds = config.read_creds('../config/private/creds.yaml')
    assert isinstance(creds, dict)
