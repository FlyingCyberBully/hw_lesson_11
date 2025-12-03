import allure
from selene import have, by


@allure.title("Заполнение формы DemoQA")
def test_practice_form(setup_browser):
    browser = setup_browser

    with allure.step("Открываем страницу"):
        browser.get("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Заполняем имя и фамилию"):
        browser.element("#firstName").set_value("John")
        browser.element("#lastName").set_value("Doe")

    with allure.step("Вводим email"):
        browser.element('#userEmail').set_value('john.doe@example.com')

    with allure.step("Выбираем пол"):
        browser.all('[for^=gender-radio]').element_by(have.text('Male')).click()
    
    with allure.step("Вводим номер телефона"):
        browser.element('#userNumber').set_value('1234567890')

    with allure.step("Выбираем дату рождения"):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select option[value="0"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select option[value="1990"]').click()
        browser.element('[aria-label="Choose Tuesday, January 23rd, 1990"]').click()
    
    with allure.step("Выбираем предмет"):
        browser.element("#subjectsInput").send_keys("Maths")
        browser.element("#subjectsInput").press_enter()
    
    with allure.step("Выбираем хобби"):
        browser.element('[for=hobbies-checkbox-1]').click()
        browser.element("#hobbiesWrapper").element(by.text("Sports")).click()

    with allure.step("Заполняем адрес"):
        browser.element("#currentAddress").set_value("Some street 1")

    with allure.step("Выбираем штат и город"):
        browser.element("#state").click()
        browser.element("#stateCity-wrapper").element(by.text("NCR")).click()
        browser.element("#city").click()
        browser.element("#stateCity-wrapper").element(by.text("Delhi")).click()

    with allure.step("Отправляем форму"):
        browser.element("#submit").click()

    with allure.step("Проверяем успешную отправку формы"):
        browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
