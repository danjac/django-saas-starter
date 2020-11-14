This is an opinionated Django cookie cutter template. For a more configurable cookiecutter, see https://github.com/pydanny/cookiecutter-django.

Features

* Heroku, AWS/S3 and Mailgun in production
* Docker for local development
* Turbolinks/StimulusJS for JS
* Tailwind/PostCSS for CSS
* Celery
* Redis
* PostgreSQL

Getting Started

You should have the following installed on your development machine:

* Docker and docker-compose
* Cookiecutter (pip install cookiecutter)
* pre-commit hooks (pip install pre-commit)
* prettier (npm install -g prettier)
* eslint (npm install -g eslint)

Now build the project:

    cookiecutter [github url]

Change to your project directory and copy the file .env.example to .env. Set the SECRET_KEY. You can change the AWS settings when you need to deploy to production.

Build your docker environment:

    docker-compose build

Open users/models.py and add any custom fields you might want at the start.

Next run migrations:

    ./scripts/manage makemigrations

    ./scripts/manage migrate

You can now start the application:

    docker-compose up -d

To ensure all dependencies are up to date, you can use pip-tools (pip install piptools):

    pip-compile requirements.in -o requirements.txt

And for frontend dependencies:

    ./scripts/yarn update

Deployment

Ensure you have the correct AWS settings in your .env file. BASE_URL should point to your CDN.

The following buildpacks are assumed:

Set up Heroku and Git as per the instructions. You need to set up Heroku to deploy a Docker image:

To deploy just run:

    ./scripts/deploy

References

* Turbolinks:
* StimulusJS:
* Tailwind:
* Docker:
* Heroku:



