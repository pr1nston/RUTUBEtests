import re
from playwright.sync_api import  Page, expect

import pytest

@pytest.mark.order(4)

def test_re_comment(page: Page):
    page.goto("https://rutube.ru/video/7bb7ea68b8d3bab80670250e49fe4a9c/")
    page.get_by_role("button", name="Закрыть").click()
    page.get_by_role("button", name="Вход и регистрация").click()
    page.locator("iframe[title=\"Multipass\"]").content_frame.get_by_role("textbox", name="Введите телефон").fill(
        "prinstondota2@gmail.com")
    page.locator("iframe[title=\"Multipass\"]").content_frame.get_by_role("button", name="Продолжить").click()
    page.locator("iframe[title=\"Multipass\"]").content_frame.locator("#login-password").fill("Prinston5698!@")
    page.locator("iframe[title=\"Multipass\"]").content_frame.get_by_role("button", name="Войти", exact=True).click()
    page.get_by_label("Привет! хорошее видео").get_by_role("button").filter(has_text=re.compile(r"^$")).click()
    page.get_by_role("button", name="Изменить").click()
    page.get_by_text("Привет! хорошее видео").fill("Привет! хорошее видео!!!")
    page.get_by_role("button", name="Сохранить").click()
    expect(page.get_by_label("Привет! хорошее видео").get_by_role("link")).to_contain_text(
        "МоикотыЧихиМатрос-тестовыйканал111111111")
    expect(page.get_by_label("Привет! хорошее видео")).to_contain_text("Привет! хорошее видео!!!")