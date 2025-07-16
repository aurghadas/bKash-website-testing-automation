# 🌐 bKash Website Testing Automation
This program is built using Python and uses Playwright as the testing framework. It automates the testing of different features on the bKash Developer Portal. The tests cover core functionalities like navigating pages, interacting with UI components, and verifying key sections of the website.

The test suite is designed to display success and failure messages in the terminal for each tested feature as a whole. Each test outputs:  
✅ A final summary message for each specific feature at the end of its execution.  
❌ Failure details for any assertion that does not pass.  


## 🚀 Features Tested
The following features of the bKash Developer website are automated:<br><br>
🏠 Home Page Navigation<br>
💬 Minimize Chat Widget<br>
📣 Campaigns Section<br>
📰 Blog Section<br>
📱 bKash App Page<br>
🧮 Charge Calculator<br>
📞 Customer Care Page<br>
ℹ️ About Section


Each feature includes explicit assertions that verify page navigation, UI element presence, and interactions.  

## 🛠️ Built With
Python 3.x – Programming language  
Playwright – Modern end-to-end web testing framework  
pytest – For organizing and running tests  
Modular Python scripts for reusable test logic and clean code  

## How to run the code?
1. Go to 'pytest' directory <br>
2. execute 'pytest bkash-web-test.py' on terminal <br>
3. Hit 'ENTER'  <br>

## 📂 Project Structure

```text
bKash-website-testing-automation/
│
├── inputs/                   Input data files (if any)
├── logs/                     Log files generated during test runs
├── pytest/                   Main test scripts directory
│   ├── bkash-web-test.py     Main test runner script
│   ├── urls.py               Stores all target URLs
│
├── screenshots/              Screenshots captured during failed tests
├── tests/                    Additional test files or test data
├── commands.txt              Useful command references
├── pytest.ini                Pytest configuration file
└── README.md                 Project documentation





