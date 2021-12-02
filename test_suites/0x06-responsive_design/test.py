from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch
from selenium.webdriver.common.by import By
import time

def run_test():
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=opts)
    try:
        print()
        print('Starting tests')
        driver.get('http://localhost:7000/01-index.html')
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
        
        # Task 1 - Check 4 # ERROR: Causes problems needs fixing
        el = driver.find_element(By.TAG_NAME, 'body')
        el.screenshot('screenshot.png')
        # original = Image.open('original.png')
        # img_diff = Image.new("RGBA", original.size)

        # num_diff_pixels = pixelmatch(screenshot, original, img_diff, includeAA=True)
        # difference_percentage = int((num_diff_pixels/screen_resolution) * 100)
        # score = ((100 - difference_percentage) / 100) * 5
        
        # print('\t\tCheck 4: {}/5.0'.format(score))
        # print('Tests done successfully!')
        print()
        
    finally:
        driver.quit()
        