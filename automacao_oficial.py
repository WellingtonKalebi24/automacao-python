from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.esocial.gov.br/portal/")
    time.sleep(3)
    page.locator('xpath=//*[@id="login-acoes"]/div[2]/p/button').click()
    time.sleep(3)
  