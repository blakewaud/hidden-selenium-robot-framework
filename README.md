# Hidden Selenium Robot Framework

This robot is an example of using the `undetected_chromedriver` library to help utilize web automation on sites using certain anti-automation countermeasures. It will likely *not* work for websites with CAPTCHA, but should work against sites that do things like check user agent settings.

## Use

Import the `HiddenSelenium` library and use the `Create undetected chromedriver` keyword, which returns a `driver` object and `DebuggerAddress` string. You can then use the `Attach chrome browser` keyword with the debug address in the `ChromeOptions` object by splitting the port off the string and using that.
