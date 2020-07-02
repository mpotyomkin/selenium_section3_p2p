import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default=None,
                     help="Choose language to run tests against, "
                     + "e.g. ru,en-us, es")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    assert user_language in [None, 'ru', 'es', 'fr', 'en-gb'], "--language должен быть 'ru', 'es', 'fr' или 'en-gb'"
    
    if user_language is None:
        user_language = 'ru'
    print(f'\nsetting language to {user_language}')

    assert browser_name in [None, 'chrome', 'firefox'], "--browser_name должен быть chrome or firefox"
    
    browser = None
    if browser_name == "chrome" or browser_name is None:
        print("start chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', 
            {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("start firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        
    yield browser

    print("\nquit browser..")
    browser.quit()