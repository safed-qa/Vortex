import pytest


def pytest_configure(config):
    config.option.allure_report_dir = 'allure-results'
