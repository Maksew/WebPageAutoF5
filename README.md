# Web Page Auto-Refresh Script

This is a Python script designed to automate the process of refreshing multiple web pages simultaneously using Selenium WebDriver and Python threading. It employs the Microsoft Edge browser.

## Requirements

- Python 3.6 or above
- Selenium WebDriver
- Microsoft Edge WebDriver

## Installation

1. **Python**: If not installed, download from [here](https://www.python.org/downloads/)

2. **Selenium**: Use pip to install Selenium as follows:

```shell
pip install selenium
```
3. **Microsoft Edge WebDriver**: Download the correct version of Edge WebDriver based on your Microsoft Edge version from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/). After download and extraction, replace `'chemin_vers_le_pilote/msedgedriver.exe'` in the script with your webdriver path.

## Usage

1. Open the script in your Python editor.
2. Update the `urls` list with the URLs you wish to auto-refresh:

```python
urls = [
    'URL_1',
    'URL_2',
    # Add more URLs here
]
```

3. Execute the script. Each URL opens in a new Microsoft Edge window and refreshes every 30 seconds.

## Customization

To adjust the refresh interval, modify the sleep value in the `refresh_page` function. This value is in seconds:

```python
time.sleep(30)  # Change this to the number of seconds you want to wait between refreshes
```

## Disclaimer

Respect the terms of service for each website. Do not refresh a page at an interval that might be considered abusive.

## Limitations

This script is specific to Microsoft Edge. For other browsers, different WebDriver is required and the script might need adjustments.

Please replace the placeholders like `'URL_1'`, `'URL_2'` and `'chemin_vers_le_pilote/msedgedriver.exe'` with the actual values.
