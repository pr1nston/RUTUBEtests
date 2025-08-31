import re
from playwright.sync_api import Page, expect


import pytest

@pytest.mark.order(5)

def test_delete_comment(page: Page):
    page.goto("https://rutube.ru/video/7bb7ea68b8d3bab80670250e49fe4a9c/")
    page.get_by_role("button", name="Закрыть").first.click()
    page.get_by_role("button", name="Вход и регистрация").click()
    page.locator("iframe[title=\"Multipass\"]").content_frame.get_by_role("textbox", name="Введите телефон").fill(
        "prinstondota2@gmail.com")
    page.locator("iframe[title=\"Multipass\"]").content_frame.get_by_role("button", name="Продолжить").click()
    page.locator("iframe[title=\"Multipass\"]").content_frame.locator("#login-password").fill("Prinston5698!@")
    page.locator("iframe[title=\"Multipass\"]").content_frame.get_by_role("button", name="Войти", exact=True).click()
    page.get_by_label("Привет! хорошее видео!!!").get_by_role("button").filter(has_text=re.compile(r"^$")).click()
    page.get_by_role("button", name="Удалить").click()
    page.get_by_role("button", name="Удалить").click()
