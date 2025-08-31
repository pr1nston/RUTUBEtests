import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    # Запускаем браузер и создаем контекст с записью видео
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir="test-results/videos")
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        page = item.funcargs.get("browser")
        if page:
            os.makedirs("test-results/screenshots", exist_ok=True)
            page.screenshot(path=f"test-results/screenshots/{item.name}.png")


def pytest_configure(config):
    # Делаем order глобальным на всю сессию
    config.addinivalue_line("markers", "order(n): set order of tests")






# Хук для снятия скриншота при падении теста
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        page = item.funcargs.get("browser")
        if page:
            os.makedirs("test-results/screenshots", exist_ok=True)
            page.screenshot(path=f"test-results/screenshots/{item.name}.png")
