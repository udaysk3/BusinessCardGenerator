# BusinessCardGenerator


# Business Card Generator

Business Card Generator is a web application built with Django that allows users to design and customize their own business cards. Users can create visually appealing business cards by choosing from a variety of templates, customizing the design elements, and adding their contact information.

## Features

- User registration and authentication system.
- User-friendly interface for designing business cards.
- Multiple customizable templates to choose from.
- Ability to add and edit contact information.
- Share  cards directly from the website.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/udaysk3/BusinessCardGenerator.git
   ```

2. Navigate to the project directory:

   ```shell
   cd BusinessCardGenerator
   ```

3. Create a virtual environment:

   ```shell
   python -m venv env
   ```

4. Activate the virtual environment:

   - For Windows:

     ```shell
     .\env\Scripts\activate
     ```

   - For macOS/Linux:

     ```shell
     source env/bin/activate
     ```

5. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Perform database migrations:

   ```shell
   python manage.py migrate
   ```

7. Start the development server:

   ```shell
   python manage.py runserver
   ```

8. Open your browser and visit [http://localhost:8000](http://localhost:8000) to access the application.

## Configuration

- The default configuration uses SQLite as the database backend. If you wish to use a different database, update the `DATABASES` setting in the `settings.py` file.

- Additional configuration options, such as email settings and static file handling, can be found in the `settings.py` file.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Open a pull request, explaining the purpose and changes made.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Django](https://www.djangoproject.com/) - The web framework used for building this application.
- [Bootstrap](https://getbootstrap.com/) - The CSS framework used for styling the user interface.
- [Font Awesome](https://fontawesome.com/) - The library providing icons used in the project.
- [Pillow](https://python-pillow.org/) - The Python imaging library used for image processing.
- [jQuery](https://jquery.com/) - The JavaScript library used for client-side interactions.
- [Google Fonts](https://fonts.google.com/) - The collection of open-source fonts used in the application.
```

Feel free to customize this README file based on your specific project requirements and add any additional sections or information that may be relevant.
