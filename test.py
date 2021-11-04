from selenium import webdriver
import traceback
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch
from selenium.webdriver.common.by import By

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Remote(
    command_executor='http://selenium:4444',
    options=firefox_options,
)
driver.set_window_rect(x=0, y=0, width=1920, height=1160)
try:
    print()
    print('Starting tests')
    driver.get('http://server:7000/01-index.html')
    screen_resolution = driver.get_window_size()['height'] * driver.get_window_size()['width']
    root = driver.find_element(By.XPATH, "/*");
    root_font_size = int(root.value_of_css_property('font-size').replace('px', ''))
    root_viewport_height = driver.execute_script('return window.innerHeight')
    
    print('\tChecking Task 1:')
    # Task 1 - Check 1
    score = 0
    element = driver.find_element(By.CLASS_NAME, 'hero-homepage')
    element_background_position = element.value_of_css_property('background-position')
    user_value = element_background_position.split(' ')
    if user_value[0] == '65%': score += 0.5
    if user_value[1] == str(root_font_size * 8) + 'px': score += 0.5
    
    print('\t\tCheck 1: {}/1.0'.format(score))
    
    # Task 1 - Check 2
    score = 0
    element = driver.find_element(By.CLASS_NAME, 'hero-homepage')
    element_background_size = int(element.value_of_css_property('background-size').replace('px', ''))
    if str(element_background_size // root_font_size) + 'rem' == '90rem': score += 1.0
    
    print('\t\tCheck 2: {}/1.0'.format(score))
    
    # Task 1 - Check 3
    score = 0
    element = driver.find_element(By.CSS_SELECTOR, '.section-hero .section-inner')
    element_min_height = float(element.value_of_css_property('min-height').replace('px', ''))
    if str(int((element_min_height * 100) // root_viewport_height)) + 'vh' == '35vh': score += 1.0
    
    print('\t\tCheck 3: {}/1.0'.format(score))
    
    # Task 1 - Check 4
    driver.save_screenshot('screenshot.png')
    screenshot = Image.open('screenshot.png')
    original = Image.open('original.png')
    img_diff = Image.new("RGBA", original.size)

    num_diff_pixels = pixelmatch(screenshot, original, img_diff, includeAA=True)
    difference_percentage = int((num_diff_pixels/screen_resolution) * 100)
    score = ((100 - difference_percentage) / 100) * 5
    
    print('\t\tCheck 4: {}/5.0'.format(score))
    print('Tests done successfully!')
    print()
    
    driver.quit()
except Exception as e:
    driver.quit()
    print(traceback.format_exc())
    