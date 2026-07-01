import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode"
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use: chrome (default)"
    )


@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture: Launches Chrome WebDriver, navigates to the OrangeHRM login page,
    and tears down after each test.
    """
    headless = request.config.getoption("--headless")

    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.implicitly_wait(5)
    drv.get(BASE_URL)

    yield drv

    drv.quit()
