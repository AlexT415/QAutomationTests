from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains

def setup(url):
    driver = webdriver.Firefox()
    driver.get(url)

    return driver
#
def test_automation_0():

    # Step 1: Navigate to https://www.wikipedia.org/.
    # Step 2: Locate the search input field and type "Python (programming language)".
    # Step 3: Press the Enter key.
    #   Expected Result: The page main heading (h1) is visible and displays the text "Python (programming language)".

    print("Running test Wikipedia -search page title")

    driver = setup("https://www.wikipedia.org/")


    search_field = driver.find_element(By.ID, value="searchInput")

    search_field.send_keys("Python (programming language)")
    search_field.send_keys(Keys.ENTER)
    wait = WebDriverWait(driver, 10)
    title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1#firstHeading span.mw-page-title-main")))
    assert title.text == "Python (programming language)"
    print("Test Wikipedia title PASSED")
    driver.quit()
def test_automation_1():

    # Step 1: Navigate to https://practicetestautomation.com/practice-test-login/.
    # Step 2: Locate the username field and enter "student".
    # Step 3: Locate the password field and enter "incorrectPassword".
    # Step 4: Click the Submit button.
    #   Expected Result: An error message is displayed with the exact text "Your password is invalid!".

    print("Running test automation 1 - wrong password")
    driver = setup("https://practicetestautomation.com/practice-test-login/")
    username = driver.find_element(By.ID,"username")
    username.send_keys("student")
    password = driver.find_element(By.ID,"password")
    password.send_keys("incorrectPassword")
    submit = driver.find_element(By.CLASS_NAME, "btn")
    time.sleep(2)
    submit.click()
    wait = WebDriverWait(driver, 10)
    error = wait.until(EC.visibility_of_element_located((By.ID, "error")))
    assert error.text == "Your password is invalid!"
    print("Test wrong password PASSED")
    driver.quit()

def test_automation_2():
    # Step 1: Navigate to https://practicetestautomation.com/practice-test-login/.
    # Step 2: Locate the username field and enter "fake_user".
    # Step 3: Locate the password field and enter "Password123".
    # Step 4: Click the Submit button.
    #   Expected Result: An error message is displayed with the exact text "Your username is invalid!".

    print("Running test automation 2 - wrong username")
    driver = setup("https://practicetestautomation.com/practice-test-login/")
    username = driver.find_element(By.ID,"username")
    username.send_keys("fake_user")
    password = driver.find_element(By.ID,"password")
    password.send_keys("Password123")
    submit = driver.find_element(By.CLASS_NAME, "btn")
    time.sleep(2)
    submit.click()
    wait = WebDriverWait(driver, 10)
    error = wait.until(EC.visibility_of_element_located((By.ID, "error")))
    assert error.text == "Your username is invalid!"
    print("Test wrong username PASSED")
    driver.quit()

def test_automation_3():

    # Step 1: Navigate to https://practicetestautomation.com/practice-test-login/.
    # Step 2: Type username student into Username field
    # Step 3: Type password Password123 into Password field
    # Step 4: Push Submit button
    #     Expected Result: New page contains expected text ('Congratulations' or 'successfully logged in')
    #                      Log out button is displayed on the new page
    # Step 5: Locate and click the "Log out" link.
    #     Expected result: The user is redirected back to the login page URL (https://practicetestautomation.com/practice-test-login/).

    print("Running test automation 3 - correct username& password")
    driver = setup("https://practicetestautomation.com/practice-test-login/")
    username = driver.find_element(By.ID,"username")
    username.send_keys("student")
    password = driver.find_element(By.ID,"password")
    password.send_keys("Password123")
    submit = driver.find_element(By.CLASS_NAME, "btn")
    time.sleep(2)
    submit.click()
    wait = WebDriverWait(driver, 10)
    loggedin = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "post-header")))
    assert loggedin.text == "Logged In Successfully"
    logout = driver.find_element(By.XPATH, "//a[contains(.,'Log out')]")
    logout.click()
    assert driver.current_url == "https://practicetestautomation.com/practice-test-login/"
    print("Test correct username&pass + Log out PASSED")
    driver.quit()

def test_automation_4():

    # Step 1: Navigate to https://the-internet.herokuapp.com/add_remove_elements/.
    #
    # Step 2: Click the "Add Element" button.
    #
    #     Expected Result: A "Delete" button appears on the page.
    #
    # Step 3: Click the newly created "Delete" button.
    #
    #     Expected Result: The "Delete" button disappears, leaving 0 delete buttons on the page.

    print("Running test automation 4 - Heroku Add/Remove Element")
    driver = setup("https://the-internet.herokuapp.com/add_remove_elements/")
    addelement = driver.find_element(By.XPATH, "//button[contains(.,'Add Element')]")
    addelement.click()
    wait = WebDriverWait(driver, 10)
    delete_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(.,'Delete')]")))
    assert delete_btn
    time.sleep(1)
    delete_btn.click()
    remaining_buttons = driver.find_elements(By.XPATH, "//button[contains(.,'Delete')]")
    assert len(remaining_buttons)== 0
    print("Test ADD/Remove Element PASSED")
    driver.quit()

def test_automation_5():
    # Step 1: Navigate to https://the-internet.herokuapp.com/checkboxes.
    # Step 2: Check the state of the first checkbox. If it is unchecked, click it to check it.
    #     Expected Result: The first checkbox is now successfully checked.
    # Step 3: Check the state of the second checkbox. If it is checked, click it to uncheck it.
    #     Expected Result: The second checkbox is now successfully unchecked.

    print("Running test automation 5 - Checkboxes")
    driver = setup("https://the-internet.herokuapp.com/checkboxes")
    checkbox_1 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]")
    state = checkbox_1.is_selected()
    if not state:
        print("checkbox 1 not selected")
        checkbox_1.click()
    state = checkbox_1.is_selected()
    if state == True:
        print("Checkbox 1 is checked!!")
    checkbox_2 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")
    state_2 = checkbox_2.is_selected()
    if state_2 == True:
        print("Checkbox 2 is checked!!")
        checkbox_2.click()
    state_2 = checkbox_2.is_selected()
    if not state_2:
        print("Checkbox 2 not checked")
    print("Test automation 5 - checkboxes PASSED")
    driver.quit()

def test_automation_6():
    # Step 1: Navigate to https://the-internet.herokuapp.com/hovers.
    # Step 2: Hover the mouse cursor over the first user avatar image.
    #     Expected Result: Additional text elements appear showing "name: user1".
    #                      Verify that the View profile link for user1 is displayed.

    print("Running test automation 6 - Hover testing")
    driver = setup("https://the-internet.herokuapp.com/hovers")
    avatar_1 = driver.find_element(By.XPATH, "(//img[@alt='User Avatar'])[1]")
    avatar_1 = ActionChains(driver).move_to_element(avatar_1).perform()
    avatar_1_hover = driver.find_element(By.XPATH, "//h5[contains(.,'name: user1')]")
    assert avatar_1_hover.text == "name: user1", "Hover text not user1"
    avatar_1_link = driver.find_element(By.XPATH, "//a[@href='/users/1']")
    assert avatar_1_link.is_displayed(), "Avatar Link not displayed"
    print("Test automation 6 - hover PASSED")
    driver.quit()

def test_automation_7():
    # Step 1: Navigate to https://the-internet.herokuapp.com/dropdown.
    # Step 2: Click on the dropdown element to expand the options.
    # Step 3: Click on and select "Option 1".
    #     Expected Result: "Option 1" is marked as selected in the dropdown list.

    print("Running test automation 7 - Dropdow")
    driver = setup("https://the-internet.herokuapp.com/dropdown")
    dropdown = driver.find_element(By.XPATH, "//select[@id='dropdown']")
    dropdown.click()
    dropdown_option_1 = driver.find_element(By.XPATH, "//option[contains(text(), 'Option 1')]")
    dropdown_option_1.click()
    assert dropdown_option_1.is_selected() == True
    print("Test dropdown by text PASSED")
    driver.quit()

