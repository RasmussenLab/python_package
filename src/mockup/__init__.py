# The __init__.py file is loaded when the package is loaded.
# It is used to indicate that the directory in which it resides is a Python package


from importlib import metadata

__version__ = metadata.version("rasmussenlab-mockup")

from .mockup import add_one, Circle

# The __all__ variable is a list of variables which are imported
# when a user does "from example import *"
__all__ = ["add_one", "Circle"]
