import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rutube.ru/channel/53315268/")
    expect(page.get_by_label("секция навигации").locator("ul")).to_contain_text("Главная")
    expect(page.get_by_label("секция навигации").locator("ul")).to_contain_text("Видео")
    expect(page.get_by_label("секция навигации").locator("ul")).to_contain_text("Shorts")
    expect(page.get_by_label("секция навигации").locator("ul")).to_contain_text("Плейлисты")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
