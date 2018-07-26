import config
import os
import requests


def send_results_to_cloud_mon(check: str, result):
    _config = config.Config()
    url = _config.get_api_url(os.getenv('CLOUD_MON_ENVIRONMENT', 'stageing'))
    api_key = os.getenv('CLOUD_MON_API_KEY')
    provider = os.getenv('CLOUD_MON_PROVIDER')
    server_id = os.getenv('CLOUD_MON_SERVER_ID')
    type_id = os.getenv('CLOUD_MON_TYPE_ID')
    print(api_key)
    payload = {
        'check': check,
        'result': result,
        'api_key': api_key,
        'provider': provider,
        'server_id': server_id,
        'type_id': type_id
    }
    r = requests.post(url, data=payload)
    print(r)
    print(r.text)
