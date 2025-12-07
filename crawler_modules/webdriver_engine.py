import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.chrome.options import Options as ChromeOptions
import webdriver_setting as ws

class WebdriverEngine:
    """
    Factory class for instantiating and configuring Selenium Webdrivers.
    Abstracts browser-specific setup logic (Firefox/Chrome).
    """

    def __init__(self):
        self.logger = logging.getLogger('WebdriverEngine')

    def open_the_browser(self, the_chosen_browser):
        """
        Factory method to initiate the requested browser driver.
        """
        if the_chosen_browser == ws.BROWSER_NAME_FIREFOX:
            self.logger.info("Browser Firefox is initiating.")
            return self.initiate_firefox()
            
        elif the_chosen_browser == ws.BROWSER_NAME_CHROME:
            self.logger.info("Browser Chrome is initiating.")
            return self.initiate_chrome()
            
        else:
            self.logger.error(f"Unknown browser type: {the_chosen_browser}")
            self.logger.error("Please check your webdriver_setting config.")
            return None

    def initiate_firefox(self):
        """Configures and launches Firefox webdriver."""
        options = FirefoxOptions()

        # Apply Headless Mode
        if ws.BROWSER_DEFAULT_HEADLESS_MODE:
            options.headless = True

        # Set Language Preference
        if ws.BROWSER_DEFAULT_LANGUAGE:
            options.set_preference('intl.accept_languages', ws.BROWSER_DEFAULT_LANGUAGE)

        # Initialize Driver
        driver = webdriver.Firefox(
            options=options,
            executable_path=ws.EXECUTABLE_PATH_OF_FIREFOX
        )

        # Apply Global Timeouts & Window Size
        self._apply_driver_settings(driver)
        
        return driver

    def initiate_chrome(self):
        """Placeholder for Chrome initialization logic."""
        # Implementation hidden for demo purposes
        pass

    def _apply_driver_settings(self, driver):
        """Helper method to apply common driver settings."""
        # Set Window Size
        if ws.BROWSER_DEFAULT_WINDOW_WIDTH and ws.BROWSER_DEFAULT_WINDOW_HEIGHT:
            driver.set_window_size(
                ws.BROWSER_DEFAULT_WINDOW_WIDTH, 
                ws.BROWSER_DEFAULT_WINDOW_HEIGHT
            )

        # Set Implicit Timeout
        if ws.BROWSER_DEFAULT_IMPLICITLY_TIMEOUT:
            driver.implicitly_wait(ws.BROWSER_DEFAULT_IMPLICITLY_TIMEOUT)

        # Set Page Load Timeout
        if ws.BROWSER_DEFAULT_PAGE_LOAD_TIMEOUT:
            driver.set_page_load_timeout(ws.BROWSER_DEFAULT_PAGE_LOAD_TIMEOUT)
