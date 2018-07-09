class Config:
    PROD_API_URL = {
        "Germany": "https://cloud-mon.net/api/_internal/check/{check_id}",
        "sing": "https://sing.cloud-mon.net/api/_internal/check/{check_id}",
        "ny": "https://do.cloud-mon.net/api/_internal/check/{check_id}"
    }

    TEST_API_URL = "https://test.cloud-mon.net/api/_internal/check/{check_id}"

    def get_api_url(self, environment: str, check_id: str):
        if environment == 'test':
            return self.TEST_API_URL.replace('{check_id}', check_id)
        else:
            if environment in self.PROD_API_URL:
                return self.PROD_API_URL[environment].replace('{check_id}', check_id)
            else:
                return 0
