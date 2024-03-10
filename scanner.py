from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# List of SQL injection dorks
dorks = [
    'intext:"error in your SQL syntax"',
    'inurl:"id=" intext:"Warning: mysql_fetch_array()',
    'intext:"Warning: mysql_connect()" filetype:php',
    'inurl:"search.php?search=" intext:"Powered by phpBB"',
    'inurl:news.php?id= intext:"Powered by PHP-Fusion"'
]

# Initialize the Chrome browser with Selenium
driver = webdriver.Chrome()

# Loop through each dork and search Google
for dork in dorks:
    # Navigate to Google
    driver.get('https://www.google.com')
    search_box = driver.find_element_by_name('q')
    
    # Search for the dork
    search_box.send_keys(dork)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for the page to load
    time.sleep(5)
    
    # Extract and print the search results
    search_results = driver.find_elements_by_xpath('//div[@class="g"]//a')
    for result in search_results:
        print(result.get_attribute('href'))
        
# Close the browser
driver.quit()
