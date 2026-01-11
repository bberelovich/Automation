# 🐾 JPetStore E2E Automation Project

An End-to-End automation testing framework for the JPetStore demo site.
Built with **Python**, **Playwright**, and **Pytest**, implementing the **Page Object Model (POM)** design pattern.

## 📌 Project Features
* **Page Object Model (POM):** Clean separation between test logic and page selectors.
* **Data-Driven:** Configuration (search queries, budget, limits) loaded from an external JSON file.
* **Robust Locators:** Handles dynamic tables and relative URLs automatically.
* **Reporting:** Integrated with Allure Report for rich visualization.
* **Smart Waiting:** Utilizes Playwright's auto-wait and custom synchronization for stability.

---

## 🚀 Prerequisites

Before you begin, ensure you have the following installed on your machine:
1.  **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
2.  **Allure Command Line** (Optional, for viewing reports):
    * *Mac:* `brew install allure`
    * *Windows:* `scoop install allure` (or download from [Allure Releases](https://github.com/allure-framework/allure2/releases))

---

## 🛠️ Installation & Setup

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone <YOUR_GITHUB_REPO_URL>
cd <YOUR_PROJECT_FOLDER_NAME>

2. Create a Virtual Environment
It is recommended to run the project in a virtual environment.

Windows:

Bash

python -m venv venv
venv\Scripts\activate
Mac / Linux:

Bash

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
Install the required Python packages from requirements.txt:

Bash

pip install -r requirements.txt

4. Install Playwright Browsers
This command downloads the necessary browser binaries (Chromium, Firefox, WebKit):

Bash

playwright install
⚙️ Configuration
You can modify the test parameters in the config.json file located in the root directory:

JSON

{
  "search_query": "fish",      // Item to search for
  "max_price": 20.0,           // Maximum price filter
  "items_to_select": 3,        // Number of items to add to cart
  "budget_per_item": 25.0      // Budget limit validation per item
}


▶️ Running the Tests
Run Tests (Standard)
To run the tests and see the output in the terminal:

Bash

pytest -s -v
Run Tests with Allure Reporting

To generate the raw results for the report:

Bash

pytest --alluredir=allure-results

📊 Viewing Reports

After running the tests with Allure enabled, use the following command to serve and view the report in your browser:

Bash

allure serve allure-results
