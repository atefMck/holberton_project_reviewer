import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import JavascriptException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def run_test():
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--no-sandbox")
    d = DesiredCapabilities.CHROME
    d['goog:loggingPrefs'] = { 'browser':'ALL' }
    driver = webdriver.Chrome(options=opts, desired_capabilities=d)
    try:
        print()
        print('Starting tests')
        driver.get('http://localhost:7000/index.html')
        
        print('\tTask 0:', end='')
        # Task 0
        score = 0
        with open('./0x0C-Javascript_advanced/0-welcome.js') as file:
            script = file.read()
        try:
            driver.execute_script(script + '\nwelcome("Atef", "Mechken");')
            alert = driver.switch_to.alert
            if alert.text == 'Welcome Atef Mechken!': score += 0.5
            alert.accept()
        except:
            pass
        try:
            driver.execute_script(script + 'alert(fullName)')
        except JavascriptException as e:
            if 'fullName is not defined' in e.msg: score += 0.5
        print(' {}/1.0'.format(score))

        print('\tTask 1:', end='')
        # Task 1
        score = 0
        with open('./0x0C-Javascript_advanced/1-nested_functions.js') as file:
            script = file.read()
        try:
            driver.execute_script(script)
            alert = driver.switch_to.alert
            if alert.text == 'Welcome': score += 0.5
            alert.accept()
            alert = driver.switch_to.alert
            if alert.text == 'Welcome Holberton': score += 0.5
            alert.accept()
            alert = driver.switch_to.alert
            if alert.text == 'Welcome Holberton!': score += 0.5
            alert.accept()
            alert = driver.switch_to.alert
        except:
            pass
        print(' {}/1.5'.format(score))

        print('\tTask 2:', end='')
        # Task 2
        score = 0
        with open('./0x0C-Javascript_advanced/2-function_me.js') as file:
            script = file.read()
        try:
            driver.execute_script(script + '\nguillaume();\nalex();\nfred();')
            alert = driver.switch_to.alert
            if alert.text == 'Welcome Guillaume': score += 0.5
            alert.accept()
            alert = driver.switch_to.alert
            if alert.text == 'Welcome Alex': score += 0.5
            alert.accept()
            alert = driver.switch_to.alert
            if alert.text == 'Welcome Fred': score += 0.5
            alert.accept()
            alert = driver.switch_to.alert
        except:
            pass
        print(' {}/1.5'.format(score))

        print('\tTask 3:', end='')
        # Task 3
        score = 0
        with open('./0x0C-Javascript_advanced/3-classrooms.js') as file:
            script = file.read()
        try:
            value = driver.execute_script(script + '\nreturn classRoom[0]();')
            if value == 1: score += 0.5
            value = driver.execute_script(script + '\nreturn classRoom[3]();')
            if value == 4: score += 0.5
            value = driver.execute_script(script + '\nreturn classRoom[9]();')
            if value == 10: score += 0.5
            value = driver.execute_script(script + '\nnewClassRoom = createClassRoom(16);\nreturn newClassRoom[12]();')
            if value == 13: score += 0.5
        except:
            pass
        print(' {}/2'.format(score))

        print('\tTask 4:', end='')
        # Task 4
        score = 0
        with open('./0x0C-Javascript_advanced/4-math.js') as file:
            script = file.read()
        try:
            value = driver.execute_script(script + '\nreturn addBy100(20);')
            if value == 120: score += 0.5
            value = driver.execute_script(script + '\nreturn divideBy10(20);')
            if value == 2: score += 0.5
            value = driver.execute_script(script + '\nreturn divideBy100(200);')
            if value == 2: score += 0.5
            value = driver.execute_script(script + '\nreturn addBy1000(20);')
            if value == 1020: score += 0.5
            value = driver.execute_script(script + '\nreturn addBy100(101);')
            if value == 201: score += 0.5
            value = driver.execute_script(script + '\nreturn addBy1000(234);')
            if value == 1234: score += 0.5
            value = driver.execute_script(script + '\nreturn divideBy10(200);')
            if value == 20: score += 0.5
            value = driver.execute_script(script + '\nreturn divideBy100(200);')
            if value == 2: score += 0.5
        except:
            pass
        print(' {}/4'.format(score))

        print('\tTask 5:', end='')
        # Task 5
        score = 0
        buttons = True
        with open('./0x0C-Javascript_advanced/5-mode.js') as file:
            script = file.read()
        try:
            driver.execute_script(script)
            score += 0.5
        except:
            pass
        try:
            text = driver.find_element(By.XPATH, '//*[text()="Welcome Holberton!"]')
            if text: score += 0.5
        except NoSuchElementException:
            pass
        try:
            spooky = driver.find_element(By.XPATH, '//*[text()="Spooky"]')
            if text: score += 0.5
            root = driver.find_element(By.CSS_SELECTOR, 'body')
            spooky.click()
            # css = root.value_of_css_property('font-size') # Check Manually!!!!
            # if css == "9px": score += 0.1
            css = root.value_of_css_property('font-weight')
            if css == "700": score += 0.1
            css = root.value_of_css_property('text-transform')
            if css == "uppercase": score += 0.1
            css = root.value_of_css_property('background-color')
            if css == "rgba(255, 192, 203, 1)": score += 0.1
            css = root.value_of_css_property('color')
            if css == "rgba(0, 128, 0, 1)": score += 0.1
        except NoSuchElementException:
            buttons = buttons and False
        try:
            dark = driver.find_element(By.XPATH, '//*[text()="Dark mode"]')
            if text: score += 0.5
            root = driver.find_element(By.CSS_SELECTOR, 'body')
            dark.click()
            # css = root.value_of_css_property('font-size') # Check Manually!!!!
            # if css == "9px": score += 0.1
            css = root.value_of_css_property('font-weight')
            if css == "700": score += 0.1
            css = root.value_of_css_property('text-transform')
            if css == "capitalize": score += 0.1
            css = root.value_of_css_property('background-color')
            if css == "rgba(0, 0, 0, 1)": score += 0.1
            css = root.value_of_css_property('color')
            if css == "rgba(255, 255, 255, 1)": score += 0.1
        except NoSuchElementException:
            buttons = buttons and False
        try:
            scream = driver.find_element(By.XPATH, '//*[text()="Scream mode"]')
            if text: score += 0.5
            root = driver.find_element(By.CSS_SELECTOR, 'body')
            scream.click()
            # css = root.value_of_css_property('font-size') # Check Manually!!!!
            # if css == "9px": score += 0.1
            css = root.value_of_css_property('font-weight')
            if css == "400": score += 0.1
            css = root.value_of_css_property('text-transform')
            if css == "lowercase": score += 0.1
            css = root.value_of_css_property('background-color')
            if css == "rgba(255, 255, 255, 1)": score += 0.1
            css = root.value_of_css_property('color')
            if css == "rgba(0, 0, 0, 1)": score += 0.1
        except NoSuchElementException:
            buttons = buttons and False
        if buttons: score += 0.5
        print(' {:.1F}/4.2'.format(score, ))

        print('\tTask 6:', end='')
        # Task 6
        score = 0
        with open('./0x0C-Javascript_advanced/6-hogwarts.js') as file:
            script = file.read()
        try:
            value = driver.execute_script(script + '\nreturn harry.getScore();')
            if value == 'Harry: 4': score += 0.5
            value = driver.execute_script(script + '\nreturn draco.getScore();')
            if value == 'Draco: -2': score += 0.5
            value = driver.execute_script(script + '\nharry.penalizeStudent(); \nreturn harry.getScore();')
            if value == 'Harry: 3': score += 0.5
            value = driver.execute_script(script + '\ndraco.rewardStudent(); \nreturn draco.getScore();')
            if value == 'Draco: -1': score += 0.5
            _ = driver.get_log('browser')
        except:
            pass
        print(' {}/2'.format(score))

        print('\tTask 7:', end='')
        # Task 7
        score = 1
        with open('./0x0C-Javascript_advanced/7-timeout.js') as file:
            script = file.read()
        try:
            value = driver.execute_script(script)
            logs = driver.get_log('browser')
            for i in range(0, len(logs))  :
                line = logs[i]['message'].split(' ', 2)[2]
                if i == 0 and "Start of the execution queue" not in line: score = 0
                elif int(line) != i + 1: score = 0
                elif i == len(logs) - 2 and "End of the loop printing" not in line: score = 0
                elif i == len(logs) - 1 and "Final code block to be executed" not in line: score = 0
        except:
            pass
        print(' {}/1'.format(score))

        print('\tTask 8:', end='')
        # Task 8
        score = 0
        with open('./0x0C-Javascript_advanced/8-payments.js') as file:
            script = file.read()
        try:
            correct_output = "Processing orders\n12321 is being processed\nCollecting payment of 10.99\n12321 has been fully processed\n12322 is being processed\nCollecting payment of 12.99\n12322 has been fully processed\n12323 is being processed\nCollecting payment of 15\n12323 has been fully processed\nAll the orders have been processed"
            value = driver.execute_script(script)
            logs = [log['message'].split(' ', 2)[2].replace('"', '') for log in driver.get_log('browser')]
            logs = "\n".join(logs)
            first_set = set(correct_output)
            second_set = set(logs)
            difference = first_set.symmetric_difference(second_set)
            if len(difference) < 10: score += 0.5
            value = driver.execute_script(script + '\nprocessOrder(12324, 3.14);')
            logs = [log['message'].split(' ', 2)[2].replace('"', '') for log in driver.get_log('browser')][-3:]
            logs = "\n".join(logs)
            correct_output = "12324 is being processed\nCollecting payment of 3.14\n12324 has been fully processed"
            first_set = set(correct_output)
            second_set = set(logs)
            difference = first_set.symmetric_difference(second_set)
            if len(difference) < 10: score += 0.5
        except:
            pass
        print(' {}/1'.format(score))

        print('\tTask 9:', end='')
        # Task 9
        score = 0
        with open('./0x0C-Javascript_advanced/9-prime.js') as file:
            script = file.read()
        try:
            correct_output = "Execution time of printing countPrimeNumbers was 0.2700000002514571 milliseconds."
            value = driver.execute_script(script)
            logs = [log['message'].split(' ', 2)[2].replace('"', '') for log in driver.get_log('browser')]
            logs = "\n".join(logs)
            first_set = set(correct_output)
            second_set = set(logs)
            difference = first_set.symmetric_difference(second_set)
            if len(difference) < 19: score += 0.5
        except:
            pass
        print(' {}/0.5'.format(score))

        print('\tTask 10:', end='')
        # Task 10
        score = 0
        with open('./0x0C-Javascript_advanced/10-prime.js') as file:
            script = file.read()
        try:
            correct_output = "Execution time of calculating prime numbers 100 times was 40.865000002551824 milliseconds."
            value = driver.execute_script(script)
            logs = [log['message'].split(' ', 2)[2].replace('"', '') for log in driver.get_log('browser')]
            logs = "\n".join(logs)
            first_set = set(correct_output)
            second_set = set(logs)
            difference = first_set.symmetric_difference(second_set)
            if len(difference) < 18: score += 0.5
        except:
            pass
        print(' {}/0.5'.format(score))

        print('\tTask 11: Check manually')
        print('\tTask 12: Check manually')

        print('\tTask 13:', end='')
        # Task 10
        score = 0
        with open('./0x0C-Javascript_advanced/13-bind_user.js') as file:
            script = file.read()
        try:
            correct_output = "Welcome, Buillaume. Your occupation is: Engineer"
            value = driver.execute_script(script)
            logs = [log['message'].split(' ', 2)[2].replace('"', '') for log in driver.get_log('browser')]
            logs = "\n".join(logs)
            first_set = set(correct_output)
            second_set = set(logs)
            difference = first_set.symmetric_difference(second_set)
            if len(difference) < 4: score += 0.5
            correct_output = "Greetings, Buillaume. Your occupation is: Engineer"
            value = driver.execute_script(script)
            logs = [log['message'].split(' ', 2)[2].replace('"', '') for log in driver.get_log('browser')]
            logs = "\n".join(logs)
            first_set = set(correct_output)
            second_set = set(logs)
            difference = first_set.symmetric_difference(second_set)
            if len(difference) < 4: score += 0.5
        except:
            pass
        print(' {}/1'.format(score))

        print('\tTask 14: Check manually')

        print('\tTask 100: Check manually')
    finally:
        driver.quit()
        