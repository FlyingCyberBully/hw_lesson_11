import allure
from allure_commons.types import Severity
from selene import browser, have


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Dmitriy")
@allure.feature("DemoQA")
@allure.story("Заполнение формы DemoQA")
@allure.link("https://demoqa.com/automation-practice-form", name="DemoQA Form")
def test_complete_practice_form(setup_browser):
    browser=setup_browser

    with allure.step("Открываем страницу"):
        browser.open('/automation-practice-form')

    with allure.step("Заполняем имя и фамилию"):
        browser.element('#firstName').type('John')
        browser.element('#lastName').type('Doe')

    with allure.step("Вводим email"):
        browser.element('#userEmail').type('john.doe@example.com')

    with allure.step("Выбираем пол"):
        browser.all('[for^=gender-radio]').element_by(have.text('Male')).click()

    with allure.step("Вводим номер телефона"):
        browser.element('#userNumber').type('1234567890')

    with allure.step("Выбираем дату рождения"):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select [value="1990"]').click()
        browser.element('.react-datepicker__month-select [value="0"]').click()
        browser.element('.react-datepicker__day--005').click()

    with allure.step("Выбираем предмет"):
        browser.element('#subjectsInput').type('Math').press_enter()

    with allure.step("Выбираем хобби"):
        browser.element('[for=hobbies-checkbox-1]').click()

    with allure.step("Заполняем адрес"):
        browser.element('#currentAddress').type('Some address')

    with allure.step("Выбираем штат и город"):
        browser.element('#state').click()
        browser.all('#state div').element_by(have.text('NCR')).click()
        browser.element('#city').click()
        browser.all('#city div').element_by(have.text('Delhi')).click()

    with allure.step("Отправляем форму"):
        browser.element('#submit').click()

    with allure.step("Проверяем успешную отправку формы"):
        browser.element('#example-modal-sizes-title-lg').should(
            have.text('Thanks for submitting the form')
        )
