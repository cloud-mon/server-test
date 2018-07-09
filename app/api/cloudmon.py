import requests, app.config, os


def send_results_to_cloud_mon(check_id: str, test: str, result: float):
    config = app.config.Config()
    url = (config.get_api_url(os.getenv('CLOUD_MON_ENVIRONMENT', 'test'), check_id))
    api_key = os.getenv('CLOUD_MON_API_KEY')
    requests.put(url, {
        test: test,
        result: result,
        api_key: api_key
    })
