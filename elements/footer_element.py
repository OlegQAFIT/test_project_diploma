import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait

from helpers.base import BasePage


class FooterElement(BasePage):
    contact_number = '//*[@href="tel:+375-44-525-38-92"]'
    contact_email = '//*[@href="mailto:contact@allsports.by"]'
    instagram_locator = '//main/div/div/footer/div[2]/a[1]'
    linkedin_locator = '//main/div/div/footer/div[2]/a[2]'
    button_employee = '//ul[@class="links"]/li[1]/a'
    button_for_partners = '//ul[@class="links"]/li[3]/a'
    button_contacts = '//ul[@class="links"]/li[5]/a'
    button_documents_for_legal_entities = '//ul[@class="links"]/li[7]/a'
    button_company = '//ul[@class="links"]/li[2]/a'
    button_objects = '//ul[@class="links"]/li[4]/a'
    button_blog = '//ul[@class="links"]/li[6]/a'
    user_agreements_locator = '//ul[@class="links"]/li[8]/a'
    subscription_types = '//h1[text()="Типы подписки"]'
    found_elements_delete = '//button[@class="reset" and @title="Очистить фильтр"]'
    partner = "//h3[text()='Что Allsports дает вашему фитнес-клубу?']"
    element_in_blog_page = '//div[h1[text()="Оллспортс Статьи"]]/article'
    act_result = '//div/div/main/section[1]/p[7]/a'
    locator_companies_page = '//h1[@class="top_title"]'
    documents_for_legal_entities = "//h2[text()='Документы для юридических лиц']"
    expected_result = '+375 (44) 502-36-13'
    file = "Индивидуальные лицензии"
    phone = +375 - 44 - 525 - 38 - 92
    expected_alert_text = "Открыть приложение 'Выбор приложения'"

    def __init__(self, driver):
        self.driver = driver
        self.main_window_handle = None

    @allure.step("Open the website")
    def open(self):
        self.driver.get('https://www.allsports.fit/by/')

    @allure.step("Click on Instagram link")
    def click_on_instagram(self):
        self.click_on(self.instagram_locator)

    @allure.step("Click on Docs link")
    def click_on_docs(self):
        self.click_on(self.user_agreements_locator)

    @allure.step("Click on LinkedIn link")
    def click_on_linkedin(self):
        self.click_on(self.linkedin_locator)

    @allure.step("Click on Employees page")
    def click_on_employees_page(self):
        self.click_on(self.button_employee)

    @allure.step("Click on Partners page")
    def click_on_partners_page(self):
        self.click_on(self.button_for_partners)

    @allure.step("Click on Contacts page")
    def click_on_contacts_page(self):
        self.click_on(self.button_contacts)

    @allure.step("Click on Agreements page")
    def click_on_agreements_page(self):
        self.click_on(self.user_agreements_locator)

    @allure.step("Click on Legal Documents page")
    def click_on_legal_documents_page(self):
        self.click_on(self.button_documents_for_legal_entities)

    @allure.step("Click on Company page")
    def click_on_company_page(self):
        self.click_on(self.button_company)

    @allure.step("Click on Objects page")
    def click_on_objects_page(self):
        self.click_on(self.button_objects)

    @allure.step("Click on Blog page")
    def click_on_blog_page(self):
        self.click_on(self.button_blog)

    @allure.step("Assert dok")
    def assert_dok(self, file):
        if file in self.driver.page_source:
            print(f"Текст '{file}' найден на странице.")
        else:
            print(f"Текст '{file}' не найден на странице.")

    @allure.step("Assert Instagram")
    def assert_instagram(self):
        self.wait_for_visible(self.instagram_locator)
        current_url = self.get_current_url()
        print("Текущий URL (instagram):", current_url)
        assert self.get_current_url() == 'https://www.instagram.com/allsports.fit/'

    @allure.step("Assert LinkedIn")
    def assert_linkedin(self):
        self.wait_for_visible(self.linkedin_locator)
        current_url = self.get_current_url()
        print("Текущий URL (LinkedIn):", current_url)
        assert current_url == 'https://www.linkedin.com/company/allsportsby'

    @allure.step("Assert phone numbers and email")
    def assert_phone_numbers_email(self):
        self.assert_element_text_equal(self.contact_number, '+375 (44) 525-38-92')
        self.assert_element_text_equal(self.contact_email, 'contact@allsports.by')

    @allure.step("Assert text in Employees page")
    def assert_text_in_page_employees(self):
        self.assert_element_text_equal(self.subscription_types, 'Типы подписки')

    @allure.step("Assert text in Partners page")
    def assert_text_in_page_partners(self):
        self.assert_element_text_equal(self.partner, 'Что Allsports дает вашему фитнес-клубу?')

    @allure.step("Assert phone")
    def assert_phone(self):
        self.assert_text_in_element(self.act_result, self.expected_result)

    @allure.step("Assert text in Legal Documents page")
    def assert_text_in_page_documents(self):
        self.assert_element_text_equal(self.documents_for_legal_entities, 'Документы для юридических лиц')

    @allure.step("Assert element")
    def assert_element(self):
        self.wait_for_element_is_displayed(self.found_elements_delete)

    @allure.step("Assert element in Blog page")
    def assert_element_blog(self):
        self.wait_for_element_is_displayed(self.element_in_blog_page)

    @allure.step("Check the companies page")
    def assert_companies_page(self):
        self.wait_for_element_is_displayed(self.locator_companies_page)
