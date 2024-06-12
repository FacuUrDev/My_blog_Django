# DjangoBlog

Welcome to DjangoBlog, a simple yet powerful blogging platform built with Django. This project allows you to create, edit, and manage blog posts with ease, leveraging the robust features of Django and its admin interface.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or higher
- Django 2.2 or higher

### Installation

Follow these steps to get your development environment running:

1. Clone the repository to your local machine: 

    ```bash
    git clone: https://github.com/FacuUrDev/My_blog_Django.git

2. Navigate to the project directory:
    
        ```bash
        cd DjangoBlog
        ```

3. Install the required dependencies:
    
        ```bash
        pip install -r requirements.txt
        ```

4. Run the migrations to create the database schema:
    
        ```bash
        python manage.py migrate
        ```

5. Create a superuser to access the Django admin:
        
            ```bash
            python manage.py createsuperuser
            ```

6. Start the development server:
            
                ```bash
                python manage.py runserver
                ```

7. Open your browser and go to `http://127.0.0.1:8000/` to view the application.

### Using Django Admin

To manage blog posts, access the Django admin by navigating to `/admin` on your local server. Log in using the superuser credentials you created earlier.

## Contributing

We welcome contributions to DjangoBlog! Please feel free to contribute by submitting pull requests to add features, fix bugs, or improve the documentation.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.