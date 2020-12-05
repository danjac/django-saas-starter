This is an opinionated Django cookiecutter template. It is useful for quick MVPs, prototypes and side projects that may grow over time if they gain traction, so solid foundations based on tried-and-tested solutions and best practices are important.

For a more configurable and complete starter template, https://github.com/pydanny/cookiecutter-django is strongly recommended.

It is assumed that you have basic familiarity with Django, Heroku and AWS.

## Features

* Docker for local development
* Turbolinks/StimulusJS for JS
* Tailwind/PostCSS for CSS
* Celery
* Redis
* PostgreSQL
* Sentry for performance/error monitoring
* Heroku for deployment
* AWS/S3 for production static/media assets
* Mailgun for production emails
* Mailhog for local dev emails
* Custom user model

## Getting Started

You should have the following installed on your development machine:

* Docker and docker-compose
* Cookiecutter (pip install cookiecutter)
* pre-commit hooks (pip install pre-commit)
* prettier (npm install -g prettier)
* eslint (npm install -g eslint)
* Heroku CLI (see https://devcenter.heroku.com/articles/heroku-cli)

Now build the project:

    cookiecutter https://github.com/danjac/django-saas-starter

Build your docker environment:

    docker-compose build

A custom user model is provided. Open *users/models.py* and add any custom fields you might want at the start.

Next run migrations:

    ./scripts/manage makemigrations users

    ./scripts/manage migrate

You can run any other Django management commands locally with *./scripts/manage*.

To run unit tests with pytest:

    ./scripts/runtests  [ARGS]

You can now start the application:

    docker-compose up -d

To ensure all dependencies are up to date, you can use pip-tools (pip install piptools):

    pip-compile requirements.in -o requirements.txt

And for frontend dependencies:

    ./scripts/yarn upgrade

Remember to do *docker-compose build* after updating backend or frontend dependencies.

Before your first Git commit, set up pre-commit hooks:

    pre-commit install

## Authentication

Django-allauth is used for authentication. This package has its own set of templates that should be overridden if you want to have Tailwind-styled login and sign up pages. You can do this by copying the templates below to the *templates/account* folder in your project and modifying them as needed:

https://github.com/pennersr/django-allauth/tree/master/allauth/templates

Example configuration is provided for social logins e.g. Google or Facebook. See the all-auth docs for more details.

## Tailwind

You can add custom classes in the file *static/css/app.css* using the *@apply* directive. Compilation should be on-the-fly using PostCSS. See the Tailwind docs for more details.

## Turbolinks/Stimulusjs

Turbolinks and Stimulusjs have been integrated to provide sufficient frontend interactivity without the complexity and overhead of an SPA architecture. A few simple controllers are included to get started with. A small middleware class is provided to handle redirects, as detailed in the Turbolinks documentation.

## Deployment

Ensure you have the correct AWS settings in your generated *.env* file. We use a single bucket for both static and (user uploaded) media, with separate folders for each, so you just need to set up a single bucket for your deployment.

PostgreSQL and Redis buildpacks are required.

Set up Heroku, S3, Cloudfront and Git as per the instructions. You need to set up Heroku to deploy a Docker image:

    heroku git:remote -a APP_NAME

    heroku stack:set container

For more details see:

https://devcenter.heroku.com/articles/git

https://www.heroku.com/deploy-with-docker


You will need to set the following Heroku environment variables:

- **ADMINS**: comma separated in form _my full name <name@mysite.com>,other name <othername@mysite.com>_
- **ADMIN_URL**: should be something other than "admin/". Must end in forward slash.
- **ALLOWED_HOSTS**: enter your domains, separated by comma e.g. *mysite.com, myothersite.com*. If you are using wildcard domain with subdomains for each community you just need the wildcard domain without the "*".
- **AWS_STORAGE_BUCKET_NAME**: see your S3 settings
- **AWS_ACCESS_KEY_ID**: see your S3 settings
- **AWS_S3_CUSTOM_DOMAIN**: your cloudfront domain e.g. *xyz123abcdefg.cloudfront.net*
- **DATABASE_URL**: provided by Heroku PostgreSQL buildpack
- **DISABLE_COLLECTSTATIC**: set to "1"
- **DJANGO_SETTINGS_MODULE**: should always be *myproject.config.settings.heroku*
- **MAILGUN_API_KEY**: see your Mailgun settings
- **MAILGUN_SENDER_DOMAIN**: see your Mailgun settings
- **REDIS_URL**: provided by Heroku Redis buildpack
- **SECRET_KEY**: Django secret key. Use e.g. https://miniwebtool.com/django-secret-key-generator/ to create new key.

To deploy just run:

    ./scripts/deploy

This is a very barebones deployment that just pushes assets to S3 and deploys your application to Heroku. You may wish to expand this to use a CI/CD pipeline such as Github Actions or Travis, or Ansible or Terraform for provisioning servers, manage staging environments etc.

If you want to include Sentry for production performance and error monitoring, just uncomment the import in the settings module *config/settings/heroku.py* and set **SENTRY_URL** (as provided by your Sentry account) in your Heroku environment.

## References

* Turbolinks: https://github.com/turbolinks/turbolinks
* StimulusJS: https://stimulusjs.org/
* Tailwind: https://tailwindcss.com/

## License

This project is covered by GNU Affero General Public License (AGPL).
