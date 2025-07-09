import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rutube.ru/categories/")
    page.get_by_label("Облегченная панель навигации").locator("a").filter(has_text="Каталог").click()
    expect(page.locator("main a").filter(has_text="День семьи")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Сезон контента")).to_be_visible()
    expect(page.locator("main a").filter(has_text="RUTUBE x PREMIER")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Авто")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Анимация")).to_be_visible()
    expect(page.locator("a").filter(has_text="Аниме")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Блогеры")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Видеоигры")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Детям")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Еда")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Интервью")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Культура")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Лайфхаки")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Музыка")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Новости и СМИ")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Обучение")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Подкасты")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Путешествия")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Радио")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Сельское хозяйство")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Сериалы")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Спорт")).to_be_visible()
    expect(page.locator("main a").filter(has_text="ТВ онлайн")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Телешоу")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Трансляции")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Фильмы")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Фонды помощи")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Футбол")).to_be_visible()
    expect(page.locator("main a").filter(has_text="Юмор")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)