from playwright.sync_api import Page

class base_page:
    #создание конструктора класса
    def __init__(self, page: Page):
        #присвоение в атрибут для паблик доступа
        self.page = page 
    #открытие страницы и проверка на 200
    def open(self, url: str):
        responce = self.page.goto(url)
        assert responce and responce.ok, f"Page fail to load: {url}" 
    #взаимодейстиве с элементами на странице
    def click_button(self, locator: str):
        #функция возвращает объект локатор
        self.page.locator(locator).click()
    #функция заполнения поля по локатору
    def fill_fld(self, locator: str, value: str):
        self.page.locator(locator).fill(value)
    
