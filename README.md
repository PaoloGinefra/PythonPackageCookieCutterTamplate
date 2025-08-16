# My CookieCutter python package template

This is a template for my go-to Python package starter.

Integrations:

- Pytest
- Poetry
- Git/Github
- MIT license

To generate the template you can run:

```bash
pip install pipx
pipx install cookiecutter
cookiecutter gh:PaoloGinefra/PythonPackageCookieCutterTamplate
```

If you pass a `remoteOrigin`, it will automatically setup a remote repository with the given url. If "None" is passed it will just setup a git repository without a remote origin.

Once you generated the template you can install the generated package with:

```bash
cd [packageName]
pip install -e .
```

## Poetry

Poetry is a great way to manage dependencies. You can install it with

```bash
pipx install poetry
```

Once you have poetry set up, you can create a venv and install the dependencies with:

```bash
poetry config virtualenvs.in-project true #This will create the virtual environment in the project folder

poetry install
```

After that you can dependencies with:

```bash
poetry add [your dep]
```
