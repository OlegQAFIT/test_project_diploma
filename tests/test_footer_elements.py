import allure

from elements import FooterElement


@allure.feature('Footer Links')
@allure.severity('critical')
@allure.story('Checking social media links')
def test_soc_links_instagram(driver):
    """
    Checking social media links instagram
    """
    soc_media = FooterElement(driver)
    soc_media.open()
    soc_media.click_on_instagram()
    soc_media.switch_to_window_by_index(1)
    soc_media.assert_instagram()


@allure.feature('Footer Links')
@allure.severity('critical')
@allure.story('Checking social media links')
def test_soc_links_linkedin(driver):
    """
    Checking social media links linkedin
    """
    soc_media = FooterElement(driver)
    soc_media.open()
    soc_media.click_on_linkedin()
    soc_media.switch_to_window_by_index(1)
    soc_media.assert_linkedin()


@allure.feature('Footer Links')
@allure.severity('critical')
@allure.story('Checking phone numbers and email')
def test_current_number_alert(driver):
    """
    Checking the unique number and alert
    """
    checking_number = FooterElement(driver)
    checking_number.open()
    checking_number.assert_phone_numbers_email()


@allure.feature('Footer Links')
@allure.severity('critical')
@allure.story('Checking the employee page')
def test_checking_the_employee_page(driver):
    """
    Checking the opening in the footer of the page for employees
    """
    open_page_for_employees = FooterElement(driver)
    open_page_for_employees.open()
    open_page_for_employees.click_on_employees_page()
    open_page_for_employees.assert_text_in_page_employees()


@allure.feature('Footer Links')
@allure.severity('critical')
@allure.story('Checking the partner page')
def test_checking_for_partners_page(driver):
    """
    Checking the opening in the footer of the page for partners
    """
    open_page_for_partners = FooterElement(driver)
    open_page_for_partners.open()
    open_page_for_partners.click_on_partners_page()
    open_page_for_partners.assert_text_in_page_partners()


@allure.feature('Footer Links')
@allure.severity('critical')
@allure.story('Checking the correct phone number')
def test_checking_the_correct_phone_number(driver):
    """
    We check on the contact page, the correct phone number
    """
    check_phone = FooterElement(driver)
    check_phone.open()
    check_phone.click_on_contacts_page()
    check_phone.assert_phone()


@allure.feature('Footer Links')
@allure.severity('critical')
@allure.story('Checking an existing document')
def test_checking_an_existing_document(driver):
    """
    We check in the documentation tab that there is a document with the name -"Индивидуальные лицензии"
    """
    found_text = FooterElement(driver)
    found_text.open()
    found_text.click_on_agreements_page()
    found_text.assert_dok("Индивидуальные лицензии")


@allure.feature('Footer Links')
@allure.severity('critical')
@allure.story('Checking legal documents page')
def test_checking_legal_documents_page(driver):
    """
    Checking the opening of a page with documents for legal entities
    """
    check_legal_documents = FooterElement(driver)
    check_legal_documents.open()
    check_legal_documents.click_on_legal_documents_page()
    check_legal_documents.assert_text_in_page_documents()

@allure.feature("Company Page")
@allure.severity("normal")
@allure.story("Checking the opening of a page for companies")
def test_checking_legal_company_page(driver):
    """
    Checking the opening of a page for company's
    """
    check_company_page = FooterElement(driver)
    check_company_page.open()
    check_company_page.click_on_company_page()
    check_company_page.assert_companies_page()

@allure.feature('Footer Links')
@allure.severity('critical')
@allure.story('Checking objects page')
def test_with_objects_page(driver):
    """
    Checking the opening of a page with objects
    """
    check_objects_page = FooterElement(driver)
    check_objects_page.open()
    check_objects_page.click_on_objects_page()
    check_objects_page.assert_element()


@allure.feature('Footer Links')
@allure.severity('critical')
@allure.story('Checking blog page')
def test_with_blog_page(driver):
    """
    Checking the search for a button in the footer and when clicked, goes to the blog tab
    """
    check_blog_page = FooterElement(driver)
    check_blog_page.open()
    check_blog_page.click_on_blog_page()
    check_blog_page.assert_element_blog()
