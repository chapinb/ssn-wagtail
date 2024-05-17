# Sustainable Streets Norwalk - Wagtail Site


## Development

First time configuration:

1. Install pre-commit, https://pre-commit.com/
2. Run `pre-commit install`
3. Install poetry, 
4. Change into the `wagtail_site/` directory and run `poetry install --no-root`

Running the application locally, from within `wagtail_site/`, using the same
dockerfile used to deploy production and a PostgreSQL DB.

1. Copy the `template.env` file to a new file named `.env` and update per the instructions within the file.
2. Build the container with: `podman-compose build`
3. Run the container with: `podman-compose up -d`

Running tests locally:

1. Start the DB, `podman-compose up db -d`
2. Update your .env file to point to `localhost` for the DB host and similar settings to match the docker-compose.yml settings
3. Run the tests outside of docker: `poetry run pytest`
