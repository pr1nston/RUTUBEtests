import os
import pytest
from playwright.sync_api import sync_playwright

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
def close_all_popups(page):
    """Закрывает все всплывающие окна с кнопкой 'Закрыть' на странице."""
    try:
        close_buttons = page.get_by_role("button", name="Закрыть")
        count = close_buttons.count()
        for i in range(count):
            try:
                close_buttons.nth(i).click()
            except:
                # Иногда кнопка может исчезнуть между подсчётом и кликом
                continue
    except:
        # Если кнопок нет, просто продолжаем
        pass


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
