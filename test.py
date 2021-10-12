from selenium import webdriver
import pytest
import time
import conftest

def test_zero(browser):
    time.sleep(1)
    assert True