import allure
from selene import be, have
from selene.core import command


@allure.title('Успешное заполнение формы регистрации студента')
def test_fill_out_and_submit_form(setup_browser):
    browser = setup_browser

    with allure.step('Открыть форму регистрации'):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step('Заполнить форму регистрации'):
        browser.element('#firstName').should(be.blank).type('Петр')
        browser.element('#lastName').should(be.blank).type('Иванов')
        browser.element('#userEmail').should(be.blank).type('iivanov@gmail.com')
        browser.element('input[value="Male"] + label').perform(command.js.scroll_into_view).click()
        browser.element('#userNumber').should(be.blank).type('89000000000')

        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select option[value="1985"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select option[value="8"]').click()
        browser.element('.react-datepicker__day--015').click()

        browser.element('#subjectsInput').type('ma').press_enter()
        browser.element('#subjectsInput').type('phy').press_enter()
        browser.element('#subjectsInput').type('eng').press_enter()

        browser.element('//label[text()="Reading"]').click()
        browser.element('//label[text()="Music"]').click()

        browser.element('#currentAddress').type('Москва, ул. Фрунзе, 12')

        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.element('//div[@id="state"]//div[text()="Haryana"]').click()
        browser.element('#city').click()
        browser.element('//div[@id="city"]//div[text()="Panipat"]').click()

        browser.element('#submit').click()

    with allure.step('Проверить результат сохранения формы'):
        browser.element('.modal-content').should(be.visible)
        browser.element("#example-modal-sizes-title-lg").should(have.text(
            'Thanks for submitting the form'
        ))
