# Sustainable Streets Norwalk - Wagtail Site


## Development

First time configuration:

1. Install pre-commit, https://pre-commit.com/
2. Run `pre-commit install`
3. Install poetry, 
4. Change into the `wagtail_site/` directory and run `poetry install --no-root`

Running the application locally, from within `wagtail_site/`, using the same
dockerfile used to deploy production.

1. Copy the `template.env` file to a new file named `.env` and update per the instructions within the file.
2. Build the container with: `podman build -t ssn-wagtail:latest .`
3. Run the container with: `podman run -it --env-file .env -p 8000:8000 ssn-wagtail`
