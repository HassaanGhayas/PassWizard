# Password Strength Checker & Generator

## Overview

This project is a **Password Strength Checker** and **Password Generator** built with **Python** and **Streamlit**. It allows users to:

1. **Check the strength** of their password by evaluating its length, character diversity, and the inclusion of digits and special characters.
2. **Generate a random secure password** based on user-defined length (between 8 and 32 characters).

## Features

### Password Strength Checker

* Evaluates the strength of a password based on three criteria:

  1. **Length**: The password must be at least 8 characters long.
  2. **Character Variety**: The password must include both **uppercase** and **lowercase** letters.
  3. **Inclusion of Numbers and Special Characters**: The password must contain **at least one digit** and **one special character**.
* Provides real-time feedback and suggestions for improving password security.

### Password Generator

* Generates a **secure random password**.
* Allows users to specify the desired length of the password (from 8 to 32 characters).
* The generated password includes a mix of uppercase, lowercase, digits, and special characters for maximum security.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/HassaanGhayas/PassWizard.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd PassWizard
   ```

3. **Create a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**:

   * On Windows:

     ```bash
     venv\Scripts\activate
     ```
   * On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. **Install the required dependencies**:

   ```bash
   pip install streamlit
   ```

6. **Run the app**:

   ```bash
   streamlit run app.py
   ```

The app will open in your default web browser.

## Usage

1. **Password Strength Checker**:

   * Enter a password in the input field.
   * Click **"Check Strength"** to evaluate the password.
   * A score (out of 6) will be displayed with suggestions on how to improve the password's strength.

2. **Password Generator**:

   * Use the **slider** to choose the length of your password (between 8 and 32 characters).
   * Click **"Generate Password"** to generate a secure password.
   * The generated password will be displayed in a **code block**, which you can easily copy and use.
