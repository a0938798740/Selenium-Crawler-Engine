import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.chrome.options import Options as ChromeOptions
import webdriver_setting as ws

class WebdriverEngine:
    """
    Factory responsible for creating and configuring webdriver instances.
    """
    
    def __init__(self):
        self.logger = logging.getLogger('WebdriverEngine')

    def open_the_browser(self, the_chosen_browser):
        """Main factory method to dispatch browser creation."""
        if the_chosen_browser == ws.BROWSER_NAME_FIREFOX:
            return self.initiate_firefox()
        elif the_chosen_browser == ws.BROWSER_NAME_CHROME:
            return self.initiate_chrome()
        else:
            self.logger.error(f"Unsupported browser: {the_chosen_browser}")
            return None

    def initiate_firefox(self):
        """Configures Firefox specific options (headless, language, timeouts)."""
        options = FirefoxOptions()
        
        # Apply configurations from settings
        if ws.BROWSER_DEFAULT_HEADLESS_MODE:
            options.headless = True
            
        if ws.BROWSER_DEFAULT_LANGUAGE:
            options.set_preference('intl.accept_languages', ws.BROWSER_DEFAULT_LANGUAGE)

        # Initialize Driver
        driver = webdriver.Firefox(
            options=options,
            executable_path=ws.EXECUTABLE_PATH_OF_FIREFOX
        )
        
        # Apply Global Timeouts
        if ws.BROWSER_DEFAULT_IMPLICITLY_TIMEOUT:
            driver.implicitly_wait(ws.BROWSER_DEFAULT_IMPLICITLY_TIMEOUT)
            
        if ws.BROWSER_DEFAULT_PAGE_LOAD_TIMEOUT:
            driver.set_page_load_timeout(ws.BROWSER_DEFAULT_PAGE_LOAD_TIMEOUT)
            
        return driver

    def initiate_chrome(self):
        """Placeholder for Chrome initialization logic."""
        # Logic mirroring initiate_firefox but for ChromeOptions
        pass
