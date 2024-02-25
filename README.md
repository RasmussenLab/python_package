# Example Python package

## Development environment

Install package so that new code is picked up in a restared python interpreter:

```
pip install -e .
```

## TestPyPI

Install vom [TestPyPI](https://test.pypi.org/project/rasmussenlab-mockup):

```
pip install -i https://test.pypi.org/simple/ rasmussenlab-mockup
```

> The package on PyPI is call `rasmussenlab-mockup` and not `mockup` as the package name is already taken. The import is still `import mockup`.

## Readthedocs

The documentation is build using readthedocs automatically. See 
[project on Readthedocs](https://readthedocs.org/projects/rasmussenlab-python-package/).

- make sure to enable build from PRs in the settings (advanded settings)
- checkout configuration file: [`.readthedocs.yaml`](.readthedocs.yaml)