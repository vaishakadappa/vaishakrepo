from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to the Microsoft Edge WebDriver executable
edge_driver_path = r'C:\edgedriver_win64\msedgedriver.exe'

# Create an instance of the Edge browser with the Edge WebDriver executable path
driver = webdriver.Edge(executable_path=edge_driver_path)

# Set up the Edge browser with the specified options
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True  # Use Chromium Edge
edge_options.add_argument('--headless')  # Run in headless mode (no GUI)

# Pass the options to the browser instance
driver = webdriver.Edge(executable_path=edge_driver_path, options=edge_options)

# Define the URL of the webpage you want to visit
url = 'https://ds.yuden.co.jp/TYCOMPAS/ap/detail?pn=RSVV5331M1LEH0002U&u=M'

try:
    # Navigate to the webpage
    driver.get(url)

    # Wait for a specific element to be visible, indicating the page is fully loaded
    wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
    element = wait.until(EC.presence_of_element_located((By.ID, 'element_id')))

    # Your interaction with the webpage can go here:
    # For example, you can click a button or close a pop-up

    # After handling the pop-up or any other interactions, you can save the page as a PDF
    driver.save_screenshot('output.png')

finally:
    # Close the browser window
    driver.quit()
