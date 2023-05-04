from selenium import webdriver

# Set the path to the Chromium browser executable
chrome_path = '/usr/bin/chromium-browser'

# Create a ChromiumOptions object to configure the browser
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path
# chrome_options.add_argument('--headless')  # Run Chromium in headless mode

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chrome_options=chrome_options)

# Navigate to a web page
driver.get('https://www.google.com')
input()
# Get the page title
print(driver.title)

# Close the browser
driver.quit()