import os
import pytest
from playwright.sync_api import sync_playwright, Page  # <-- Page нужно импортировать
from playwright.sync_api import TimeoutError

# Фикстура для Browser
@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

# Фикстура для Page, каждый тест в отдельном контексте с видео
@pytest.fixture(scope="function")
def page(browser_instance):
    context = browser_instance.new_context(record_video_dir="test-results/videos")
    page = context.new_page()
    yield page
    context.close()

# В conftest.py или отдельном utils.py
def close_all_popups(page: Page):
    """Закрывает все всплывающие окна с кнопкой 'Закрыть' на странице."""
    for _ in range(5):  # повторяем несколько раз, чтобы точно закрыть все
        try:
            buttons = page.locator('button', has_text='Закрыть')
            count = buttons.count()
            if count == 0:
                break
            for i in range(count):
                try:
                    buttons.nth(i).click(timeout=2000)
                except TimeoutError:
                    continue
        except:
            break

@pytest.fixture(autouse=True)
def close_popups_before_test(page: Page):
    close_all_popups(page)
    yield


# Скриншоты при падении теста
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("test-results/screenshots", exist_ok=True)
            page.screenshot(path=f"test-results/screenshots/{item.name}.png")

# Глобальный order для тестов
def pytest_configure(config):
    config.addinivalue_line("markers", "order(n): set order of tests")
