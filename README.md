# Example Python package

## How to use

Can be used as GitHub template repository,
see [GitHub documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

You will need to find and replace occurences of

- `python_package` -> `your_package_name`
- `RasmussenLab` -> `GitHub_user_name` (or `organization`)

with the name of your package and GitHub user name (or organization).

## Development environment

Install package so that new code is picked up in a restared python interpreter:

```
pip install -e ".[dev]"
```

## Basic usage

```python
from python_package import hello_world
print (python_package.__version__)
print(hello_world(4))
```

## Readthedocs

The documentation can be build using readthedocs automatically. See
[project on Readthedocs](https://readthedocs.org/projects/rasmussenlab-python-package/) for the project. A new project needs
to be registered.

- make sure to enable build from PRs in the settings (advanded settings)
- checkout configuration file: [`.readthedocs.yaml`](.readthedocs.yaml)
