from playwright.sync_api import Page, expect
import pytest

@pytest.mark.order(2)
def test_login_mail(page: Page):
    page.goto('https://rutube.ru')
    page.get_by_role("button", name="Вход и регистрация").click()
    page.locator("iframe[title=\"Multipass\"]").content_frame.get_by_role("textbox", name="Введите телефон").fill(
        "prinstondota2@gmail.com")
    page.locator("iframe[title=\"Multipass\"]").content_frame.get_by_role("button", name="Продолжить").click()
    page.locator("iframe[title=\"Multipass\"]").content_frame.locator("#login-password").fill("Prinston5698!@")
    page.locator("iframe[title=\"Multipass\"]").content_frame.get_by_role("button", name="Войти", exact=True).click()
