import logging
from selenium.common.exceptions import NoSuchWindowException
from webdriver_engine import WebdriverEngine
import webdriver_setting as ws

class Crawler:
    """
    Core Crawler class providing a high-level API for browser automation.
    Wraps Selenium primitives to handle common web interactions, window management,
    and alert handling safely.
    """

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger('Crawler')
        self.webdriver = None
        self.driver_engine = WebdriverEngine()

    # --- Initialization ---
    def initiate_webdriver(self, the_chosen_browser=ws.BROWSER_DEFAULT_TYPE):
        """Initializes the browser driver based on configuration."""
        if self.webdriver:
            self.logger.warning("Webdriver already initialized.")
            return
        self.webdriver = self.driver_engine.open_the_browser(the_chosen_browser)

    # --- Element Interaction ---
    def get_element_by_xpath(self, xpath):
        """Finds and returns a single element by XPath."""
        return self.webdriver.find_element_by_xpath(xpath)

    def locate_element_by_xpath(self, xpath):
        """Locates an element and stores it in self.located_element for subsequent operations."""
        self.located_element = self.webdriver.find_element_by_xpath(xpath)

    def get_element_attribute(self, element, attribute):
        """Retrieves a specific attribute from an element."""
        return element.get_attribute(attribute)

    def get_attribute(self, attribute):
        """Retrieves attribute from the currently located element."""
        return self.located_element.get_attribute(attribute)

    def get_element_text(self, element):
        return element.text

    def get_text(self):
        return self.located_element.text

    # --- Alert Handling ---
    def get_alert_text(self):
        """Switches to alert and retrieves its text."""
        return self.webdriver.switch_to.alert.text

    def accept_alert_window(self):
        """Accepts (clicks OK) on the alert window."""
        self.webdriver.switch_to.alert.accept()

    def cancel_alert_window(self):
        """Dismisses (clicks Cancel) the alert window."""
        self.webdriver.switch_to.alert.dismiss()

    # --- Frame Management ---
    def switch_to_frame_element(self, element):
        """Switches context to the specified iframe."""
        self.webdriver.switch_to.frame(element)
        self.logger.info('Switched to child frame.')

    def switch_back_to_main_frame(self):
        """Returns context to the default content."""
        self.webdriver.switch_to.default_content()

    # --- Window/Tab Management ---
    def open_new_window_by_href(self, href):
        """Opens a link in a new tab/window via JavaScript execution."""
        self.webdriver.execute_script(f"window.open('{href}', '_blank');")

    def switch_to_next_window(self):
        """
        Safely switches to the next available window handle.
        Includes logic to handle cases where the current window was closed unexpectedly.
        """
        current_handles = self.webdriver.window_handles
        try:
            # Implementation logic simplified for demo
            current_handle = self.webdriver.current_window_handle
            next_index = (current_handles.index(current_handle) + 1) % len(current_handles)
            self.webdriver.switch_to.window(current_handles[next_index])
        except NoSuchWindowException:
            self.logger.warning("Current window lost, falling back to last active window.")
            self.webdriver.switch_to.window(current_handles[-1])

    def switch_to_previous_window(self):
        """Safely switches to the previous window handle."""
        # Logic similar to switch_to_next_window, but in reverse direction
        current_handles = self.webdriver.window_handles
        try:
            current_handle = self.webdriver.current_window_handle
            prev_index = (current_handles.index(current_handle) - 1) % len(current_handles)
            self.webdriver.switch_to.window(current_handles[prev_index])
        except NoSuchWindowException:
            self.webdriver.switch_to.window(current_handles[0])

    def close_current_window(self):
        """Closes the current tab and focuses on the remaining last tab."""
        try:
            self.webdriver.close()
            if self.webdriver.window_handles:
                self.webdriver.switch_to.window(self.webdriver.window_handles[-1])
        except Exception as e:
            self.logger.error(f"Error closing window: {e}")

    def quit(self):
        if self.webdriver:
            self.webdriver.quit()
