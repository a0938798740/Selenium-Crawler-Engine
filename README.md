# Modular Selenium Crawler Engine

## Overview
This repository houses a custom-built **Selenium Wrapper Library** designed to abstract low-level browser automation details.
It was developed to refactor and modularize legacy web scraping scripts,
such as my [TPCrawler project](https://github.com/a0938798740/taipower-bill-crawler-demo)),
and to improve maintainability and readability.

*(Note: The full integration code utilizing this engine is currently in production use and cannot be open-sourced due to confidentiality agreements.)*

## Key Features

*   **Object-Oriented Architecture**: Encapsulates Selenium webdriver actions into a robust `Crawler` class (`crawler.py`), providing high-level methods for safe navigation and element interaction.
*   **Driver Abstraction**: The `WebdriverEngine` (`webdriver_engine.py`) separates browser initialization logic from business logic, allowing seamless switching between Firefox/Chrome and headless modes via configuration.
*   **Safe Multi-Tab Management**: Implements custom logic to handle complex window/tab switching scenarios, preventing common `NoSuchWindowException` errors during long-running scraping tasks.
*   **Integrated Image Pipeline**: Includes modularized image preprocessing (`image_process.py`) and OCR utilities (`image_identification.py`) for handling CAPTCHA challenges efficiently.

## Usage Structure

- **`crawler.py`**: Main entry point for browser interaction.
- **`webdriver_setting.py`**: Centralized configuration for browser paths and timeout settings.
- **`image_process.py`**: Utilities for cropping, gray-scaling, and denoising images.
