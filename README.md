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
