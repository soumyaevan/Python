*** Settings ***
Library     rbfWEB

*** Test Cases ***
Sample Test
    Open Browser  url  browser=firefox  alias=None  remote_url=False  desired_capabilities=None  ff_profile_dir=None
    Set Browser Implicit Wait  30
    
    