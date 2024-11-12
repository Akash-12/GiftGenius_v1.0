# E-Gift Commerce Portal

This is the E-Gift Commerce Portal built using Django and Tailwind CSS.

## Table of Contents

- [Project Setup](#project-setup)
  - [For macOS/Linux](#for-macoslinux)
  - [For Windows](#for-windows)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)

---

## Project Setup

### Prerequisites

- Python 3.8 or higher
- Git
- Virtualenv (optional, but recommended)
- Node.js (for Tailwind CSS)

### For macOS/Linux

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd e-giftcard-portal
    ```

2. **Create a Virtual Environment**:
    (Optional, but recommended)
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install Node.js (if not installed)**:
    Follow [this guide](https://nodejs.org/en/download/) to install Node.js.

5. **Install Tailwind CSS**:
    Install Tailwind CSS as a PostCSS plugin by running:
    ```bash
    npm install -D tailwindcss@latest postcss@latest autoprefixer@latest
    ```

6. **Run the Migrations**:
    ```bash
    python manage.py migrate
    ```

### For Windows

1. **Clone the Repository**:
    Open Command Prompt or Git Bash:
    ```bash
    git clone <repository-url>
    cd e-giftcard-portal
    ```

2. **Create a Virtual Environment**:
    (Optional, but recommended)
    ```bash
    python -m venv env
    env\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install Node.js (if not installed)**:
    Follow [this guide](https://nodejs.org/en/download/) to install Node.js.

5. **Install Tailwind CSS**:
    Install Tailwind CSS as a PostCSS plugin by running:
    ```bash
    npm install -D tailwindcss@latest postcss@latest autoprefixer@latest
    ```

6. **Run the Migrations**:
    ```bash
    python manage.py migrate
    ```

---

## Running the Application

Once the setup is complete, you can start the Django development server:

```bash
python manage.py runserver


The application will be accessible at http://127.0.0.1:8000/.
