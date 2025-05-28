# web-scraping---wikipedia
- with Selenium

This Python script automates a search on Wikipedia and extracts the first meaningful paragraph from the article for a given query using Selenium WebDriver.

---

## Features

- Opens Wikipedia homepage
- Searches for the term "Artificial Intelligence"
- Extracts and prints the first non-empty paragraph from the article page
- Closes the browser automatically after completion

---

## Requirements

- Python 3.x
- Selenium
- Chrome browser
- ChromeDriver compatible with your Chrome version (make sure `chromedriver` is in your system PATH)

---

## Installation

1. Install Selenium via pip:
   ```bash
   pip install selenium
2. Download ChromeDriver and add it to your system PATH.
   
Usage
Clone this repository or download the script file.
Run the script:
python slwiki.py
The script will open a Chrome browser window, perform the search on Wikipedia, print the first meaningful paragraph of the article, then close the browser.
