# Pranish Shrestha | Portfolio

A personal portfolio website built with **Django**, **Tailwind CSS**, and **Flowbite**.

## Features

- **Responsive Design**: Fully responsive UI/UX using Tailwind CSS.
- **Dark Mode**: Sleek dark theme enabled by default.
- **Dynamic Content**:
    - **Skills**: Animated progress bars.
    - **Achievements**: Grid layout for hackathons and certifications.
    - **Projects**: Showcase of GitHub repositories.
- **Interactive**: Hover effects, scroll-to-top button, and CV download.
- **Resume Download**: Direct link to download my curriculum vitae.

## Tech Stack

- **Backend**: Django 5.x (Python 3.x)
- **Frontend**: HTML5, Tailwind CSS (via CDN), Flowbite (via CDN)
- **Database**: SQLite (Default)

## Setup & Running

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/pranishs999/Portfolio.git
    cd Portfolio
    ```

2.  **Create and Activate Virtual Environment**:
    ```bash
    python -m venv .venv
    # Windows
    .\.venv\Scripts\activate
    # Linux/Mac
    source .venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install django
    ```

4.  **Run Migrations**:
    ```bash
    python manage.py migrate
    ```

5.  **Start Server**:
    ```bash
    python manage.py runserver
    ```

6.  Visit `http://127.0.0.1:8000` in your browser.

## Customization

- **Content**: Update `templates/home.html` with your own details.
- **Resume**: Replace `static/resume.pdf` with your own file.
- **Profile Image**: Replace `static/images/profile.png` with your own photo.

---
© 2024 Pranish Shrestha. Built with Django.