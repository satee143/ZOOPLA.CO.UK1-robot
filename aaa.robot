*** Settings ***
Library    BuiltIn  

*** Variables ***
${i}=    '1'



*** Test Cases ***
MY TEST CASE
    
    ${j}=    Convert To String    1
    Log To Console    ${i}
    Log To Console    ${j}        