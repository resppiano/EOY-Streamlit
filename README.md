# Employee Review Question Generator

## Description
This Streamlit-based web application generates personalized employee review questions, collects responses, and produces summaries and comprehensive reports for annual performance reviews.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Local Usage](#local-usage)
4. [Deploying to Streamlit Community Cloud](#deploying-to-streamlit-community-cloud)
5. [Application Workflow](#application-workflow)
6. [Customization](#customization)
7. [Troubleshooting](#troubleshooting)
8. [Contributing](#contributing)
9. [License](#license)

## Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Git

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd employee-review-generator
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Local Usage

1. Ensure you're in the project directory and your virtual environment is activated.

2. Run the Streamlit app:
   ```
   streamlit run streamlit_app.py
   ```

3. Your default web browser should open automatically with the application. If not, open a browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

## Deploying to Streamlit Community Cloud

1. Ensure your main Python file is named `streamlit_app.py`.

2. Create a GitHub repository and push your code:
   ```
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/your-username/your-repo-name.git
   git push -u origin main
   ```

3. Go to [Streamlit Community Cloud](https://share.streamlit.io/) and sign in with your GitHub account.

4. Click on "New app" and select your repository, branch, and main file (`streamlit_app.py`).

5. Click "Deploy".

6. To make your app private:
   - Go to your app's settings
   - Under "Sharing", select "Private app"
   - Invite specific people by email or create a shareable link with a password

## Application Workflow

1. **Enter Employee Information:**
   - Fill in all the fields in the "Employee Information" section.
   - Fields include Job Title, Department, Years of Service, Key Responsibilities, Goals Set This Year, Major Projects, Key Achievements, Areas for Improvement, and Training Completed.

2. **Generate Questions:**
   - After filling in all fields, click the "Generate Questions" button.
   - The application will create 10 tailored review questions based on the provided information.

3. **Answer Questions:**
   - Review the generated questions.
   - Provide answers in the text areas below each question.

4. **Generate Summary and Report:**
   - After answering the questions, click the "Generate Summary and Report" button.
   - The application will produce a summary and a comprehensive report based on the employee information and answers provided.

5. **Review Output:**
   - The summary and comprehensive report will be displayed on the page.
   - You can copy this text for use in official review documents or further analysis.

## Customization

You can customize the application by modifying the following parts of the `streamlit_app.py` file:

- `generate_local_questions`: Edit or add to the question pool.
- `generate_summary_and_report`: Modify the structure and content of the summary and report.

## Troubleshooting

- If you encounter any issues, check the Streamlit output in the terminal for error messages.
- Ensure all required fields are filled before generating questions or the summary.
- If deploying to Streamlit Community Cloud, make sure your `requirements.txt` file is up to date with all necessary dependencies.

## Contributing

Contributions to improve the application are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear, descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request with a clear description of your changes.


---

For any additional questions or support, please [contact gregjones5947@gmail.com.]