import undetected_chromedriver as uc
from undetected_chromedriver import ChromeOptions
from typing import List


class HiddenSelenium:
    """Give this library a proper name and document it."""

    def create_undetected_chromedriver(
        self, port: int = 9222, exe_path: str = None, extension_paths: List[str] = None
    ):
        if extension_paths is not None:
            options = ChromeOptions()
            for path in extension_paths:
                options.add_extension(path)
        else:
            options = None
        driver = uc.Chrome(options=options, port=port, browser_executable_path=exe_path)
        return driver, driver.capabilities["goog:chromeOptions"]["debuggerAddress"]
