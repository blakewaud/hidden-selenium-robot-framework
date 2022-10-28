*** Settings ***
Documentation       Template robot main suite.

Library             RPA.Browser.Selenium
Library             String
Library             HiddenSelenium


*** Tasks ***
Minimal task
    ${driver}    ${debugger_address}=    Create undetected chromedriver
    ${split_address}=    Split string    ${debugger_address}    :
    Attach chrome browser    ${split_address}[1]
    Go to    www.google.com
    Sleep    1m
