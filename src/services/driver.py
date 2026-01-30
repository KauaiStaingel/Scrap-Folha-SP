from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SeleniumDriver:
    def __init__(self, headless=True, window_size="1366,768"):
        self.headless = headless
        self.window_size = window_size

    def create(self):
        options = Options()

        if self.headless:
            options.add_argument("--headless=new")

        options.add_argument(f"--window-size={self.window_size}")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        return webdriver.Chrome(options=options)
