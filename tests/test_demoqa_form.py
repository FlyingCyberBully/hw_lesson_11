from selene import browser, have


def test_complete_practice_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Doe')
    browser.element('#userEmail').type('john.doe@example.com')

    browser.all('[for^=gender-radio]').element_by(have.text('Male')).click()

    browser.element('#userNumber').type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select [value="1990"]').click()
    browser.element('.react-datepicker__month-select [value="0"]').click()
    browser.element('.react-datepicker__day--005').click()

    browser.element('#subjectsInput').type('Math').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()

    browser.element('#uploadPicture').send_keys('/Users/dmitrij/Desktop/photo.png')

    browser.element('#currentAddress').type('Some address')

    browser.element('#state').click()
    browser.all('#state div').element_by(have.text('NCR')).click()

    browser.element('#city').click()
    browser.all('#city div').element_by(have.text('Delhi')).click()

    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(
        have.text('Thanks for submitting the form')
    )
