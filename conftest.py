import pytest
from selenium import webdriver
from page_objects.home_page import HomePageScooter
from page_objects.order_page import OrderFormPage
from data import base_url


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(base_url)
    yield driver
    driver.quit()


@pytest.fixture
def home_page(driver):
    home_page = HomePageScooter(driver)
    home_page.close_cookie()
    return home_page


@pytest.fixture
def order_page(driver):
    order_page = OrderFormPage(driver)
    return order_page