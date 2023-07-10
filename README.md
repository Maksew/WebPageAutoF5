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

1. Open the Python script in your Python editor.
2. Update the `config.json` file with the URLs you wish to auto-refresh and the refresh time:

```json
{
    "urls": [
        "URL_1",
        "URL_2"
        // Add more URLs here
    ],
    "edge_driver_path": "Your_Edge_Driver_Path",
    "refresh_time": 30
}
```

3. Execute the script. Each URL will open in a new Microsoft Edge window and refresh based on the configured interval.

## Customization

To adjust the refresh interval, modify the `refresh_time` value in the `config.json` file. This value is in seconds.

## Limitations

This script is specific to Microsoft Edge. For other browsers, you will need a different WebDriver and may need to adjust the script.

Remember to replace the placeholders such as `URL_1`, `URL_2`, and `Your_Edge_Driver_Path` with the actual values.
