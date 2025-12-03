import allure
from selene import have, by


@allure.title("Заполнение формы DemoQA")
def test_practice_form(setup_browser):
    browser = setup_browser

    with allure.step("Открываем страницу"):
        browser.get("https://demoqa.com/automation-practice-form")

    with allure.step("Заполняем имя и фамилию"):
        browser.find_element("#lastName").send_keys("Doe")
        browser.find_element("#firstName").send_keys("John")

    with allure.step("Вводим email"):
        browser.find_element('#userEmail').send_keys('john.doe@example.com')

    with allure.step("Выбираем пол"):
        browser.all('[for^=gender-radio]').element_by(have.text('Male')).click()
    
    with allure.step("Вводим номер телефона"):
        browser.find_element('#userNumber').send_keys('1234567890')

    with allure.step("Выбираем дату рождения"):
        browser.find_element('#dateOfBirthInput').click()
        browser.find_element('.react-datepicker__month-select').click()
        browser.find_element('.react-datepicker__month-select option[value="0"]').click()
        browser.find_element('.react-datepicker__year-select').click()
        browser.find_element('.react-datepicker__year-select option[value="1990"]').click()
        browser.find_element('[aria-label="Choose Tuesday, January 23rd, 1990"]').click()
    
    with allure.step("Выбираем предмет"):
        browser.find_element("#subjectsInput").send_keys("Maths")
        browser.find_element("#subjectsInput").press_enter()
    
    with allure.step("Выбираем хобби"):
        browser.find_element('[for=hobbies-checkbox-1]').click()
        browser.find_element("#hobbiesWrapper").find_element(by.text("Sports")).click()

    with allure.step("Заполняем адрес"):
        browser.find_element("#currentAddress").send_keys("Some street 1")

    with allure.step("Выбираем штат и город"):
        browser.find_element("#state").click()
        browser.find_element("#stateCity-wrapper").find_element(by.text("NCR")).click()
        browser.find_element("#city").click()
        browser.find_element("#stateCity-wrapper").find_element(by.text("Delhi")).click()

    with allure.step("Отправляем форму"):
        browser.find_element("#submit").click()

    with allure.step("Проверяем успешную отправку формы"):
        browser.find_element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
