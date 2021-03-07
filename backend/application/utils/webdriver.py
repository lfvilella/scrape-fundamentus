import os
import time

from selenium import webdriver


class BaseScraper:
    def __init__(self):
        self._tmp_folder = '/tmp/img-scrpr-chrm/'
        self.driver = webdriver.Chrome(
            executable_path='/usr/local/bin/chromedriver',
            options=self._get_default_chrome_options(),
            service_args=[
                '--verbose',
                f"--log-path={os.path.abspath('./chromedriver.log')}",
            ],
        )

    def get_by_xpath(
        self, xpath: str, sleep: int = 2, start: int = 0, tries: int = 10,
    ):
        try:
            if start <= tries:
                element = self.driver.find_element_by_xpath(xpath)
                if element:
                    return element

                if sleep:
                    time.sleep(sleep)

        except Exception as error:
            if start <= tries:
                print('Error getting element. Retrying...')
                return self.get_by_xpath(xpath, sleep, start=start + 1)

            raise error

    def close_connection(self):
        self.driver.quit()

    def _get_default_chrome_options(self):
        chrome_options = webdriver.ChromeOptions()

        lambda_options = [
            '--autoplay-policy=user-gesture-required',
            '--disable-background-networking',
            '--disable-background-timer-throttling',
            '--disable-backgrounding-occluded-windows',
            '--disable-breakpad',
            '--disable-client-side-phishing-detection',
            '--disable-component-update',
            '--disable-default-apps',
            '--disable-dev-shm-usage',
            '--disable-domain-reliability',
            '--disable-extensions',
            '--disable-features=AudioServiceOutOfProcess',
            '--disable-hang-monitor',
            '--disable-ipc-flooding-protection',
            '--disable-notifications',
            '--disable-offer-store-unmasked-wallet-cards',
            '--disable-popup-blocking',
            '--disable-print-preview',
            '--disable-prompt-on-repost',
            '--disable-renderer-backgrounding',
            '--disable-setuid-sandbox',
            '--disable-speech-api',
            '--disable-sync',
            '--disk-cache-size=33554432',
            '--hide-scrollbars',
            '--ignore-gpu-blacklist',
            '--ignore-certificate-errors',
            '--metrics-recording-only',
            '--mute-audio',
            '--no-default-browser-check',
            '--no-first-run',
            '--no-pings',
            '--no-sandbox',
            '--no-zygote',
            '--password-store=basic',
            '--use-gl=swiftshader',
            '--use-mock-keychain',
            '--single-process',
            '--headless',
        ]

        # chrome_options.add_argument('--disable-gpu')
        for argument in lambda_options:
            chrome_options.add_argument(argument)
        chrome_options.add_argument(
            '--user-data-dir={}'.format(self._tmp_folder + '/user-data')
        )
        chrome_options.add_argument(
            '--data-path={}'.format(self._tmp_folder + '/data-path')
        )
        chrome_options.add_argument('--homedir={}'.format(self._tmp_folder))
        chrome_options.add_argument(
            '--disk-cache-dir={}'.format(self._tmp_folder + '/cache-dir')
        )

        prefs = {
            'download.default_directory': os.path.abspath('./downloads/'),
            'profile.default_content_settings.popups': 0,
        }

        chrome_options.add_experimental_option('prefs', prefs)

        return chrome_options
