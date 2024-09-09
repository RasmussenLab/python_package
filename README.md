# Example Python package

## How to use

Can be used as GitHub template repository,
see [GitHub documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

You will need to find and replace occurences of `mockup` with the name of your package. This still might
need further testing:

```bash
# currently these are (v24.03)

pyproject.toml:
  5  description = "A small example package"
  6: name = "rasmussenlab-mockup"
  7  # This means: Load the version from the package itself.

README.md:
   7  
   8: You will need to find and replace occurences of `mockup` with the name of your package. This still might
   9  need further testing.

  22  
  23: Install vom [TestPyPI](https://test.pypi.org/project/rasmussenlab-mockup):
  24  
  25  ```
  26: pip install -i https://test.pypi.org/simple/ rasmussenlab-mockup
  27  ```
  28  
  29: > The package on PyPI is call `rasmussenlab-mockup` and not `mockup` as the package name is already taken. The import is still `import mockup`.
  30  

docs\conf.py:
   18  
   19: project = "mockup"
   20  copyright = "2024, Jakob Nybo Nissen, Henry Webel"
   21  author = "Jakob Nybo Nissen, Henry Webel"
   22: PACKAGE_VERSION = metadata.version("rasmussenlab-mockup")
   23  version = PACKAGE_VERSION

  119      PROJECT_ROOT = Path(__file__).parent.parent
  120:     PACKAGE_ROOT = PROJECT_ROOT / "src" / "mockup"
  121  

docs\index.rst:
   1: .. mockup documentation master file, created by
   2     sphinx-quickstart on Mon Aug 28 14:09:15 2023.

   5  
   6: The mockup package
   7  ==================================
   8  
   9: Mockup is a Python package with some simple example code.
  10: To get started, explore the :class:`mockup.Circle` class.
  11  

docs\README.md:
  27  # apidoc
  28: sphinx-apidoc --force --implicit-namespaces --module-first -o reference ../src/mockup
  29  # build docs

docs\tutorial\tutorial.ipynb:
   6     "source": [
   7:     "# Mockup tutorial"
   8     ]

  15     "source": [
  16:     "from mockup import mockup"
  17     ]

  24     "source": [
  25:     "mockup.add_one(-11)"
  26     ]

  33     "source": [
  34:     "list(mockup.flatten_ints([[9, 11], [12], [4, 5]]))"
  35     ]

  42     "source": [
  43:     "c2 = mockup.Circle.from_circumference(100)\n",
  44      "round(c2.radius, 3)"

src\mockup\__init__.py:
  6  
  7: __version__ = metadata.version("rasmussenlab-mockup")
  8  
  9: from .mockup import add_one, Circle
  10  

tests\test_circle.py:
  1  import unittest
  2: from mockup.mockup import Circle
  3  
```

And additionally the author names:

```bash
pyproject.toml:
  1  [project]
  2: authors = [
  3    {name = "Jakob Nybo Nissen", email = "jakobnybonissen@gmail.com"},

README.md:
  37     20  copyright = "2024, Jakob Nybo Nissen, Henry Webel"
  38:    21  author = "Jakob Nybo Nissen, Henry Webel"
  39     22: PACKAGE_VERSION = metadata.version("rasmussenlab-mockup")

  96  
  97: And additionally the author names:
  98  

docs\conf.py:
  20  copyright = "2024, Jakob Nybo Nissen, Henry Webel"
  21: author = "Jakob Nybo Nissen, Henry Webel"
  22  PACKAGE_VERSION = metadata.version("rasmussenlab-mockup")
```

> Potentially a cookiecutter could be based on this template repository.

## Development environment

Install package so that new code is picked up in a restared python interpreter:

```
pip install -e ".[dev]"
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
