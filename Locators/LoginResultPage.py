from selenium.webdriver.common.by import By

class LoginResultPageLocators(object):
  LABEL_MESSAGE = (By.XPATH, '//*[@id="login_button_container"]/div/form/h3')
  RESULT_URL = 'inventory.html'
  HEADER_TITLE = (By.ID,'inventory_filter_container')