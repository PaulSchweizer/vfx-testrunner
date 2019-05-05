# VFX Testrunner

Simple pytest wrapper for unittests that depend on common vfx applications like maya, nuke, houdini.

**Linux:**
```
vfx-testrunner ./tests --capture no --interpreter maya
```

**Windows:**
```
python vfx-testrunner ./tests --capture no --interpreter maya
```

For more details consult the help, -p/--pytest-help will show the pytest help.

```
vfx-testrunner --help

usage: vfx-testrunner [file_or_dir] [pytest options] [interpreter]

optional arguments:
  -h, --help            show this help message and exit
  --pytest-help, -p     Show the pytest help
  --interpreter {python,nuke,maya,houdini}, -i {python,nuke,maya,houdini}
                        The python interpreter to use.

```

# Using Pytest in a vfx studio

In VFX studios, pytest and other test libraries like mock or pytest-cov might not be available out of the box, especially inside the applications (e.g. maya, houdini, nuke).

The simple, albeit a bit hacky solution would be the following:

1. Create a virtualenv and pip install all required libraries. I recommed pytest, pytest-cov and mock.
2. Inside the created virtualenv will be the site-packages folder holding all the installed libraries and their dependencies.
3. Edit the `{interpreter}_test.py` files from thevfx-testrunner to prepend the path to that site-packages folder prior to importing pytest.

```python
import os
import sys

sys.path.insert(0, "/path/to/the/venv/Lib/site-packages"))

import pytest

pytest.main(sys.argv[1:])
```

4. This looks a bit hacky and might fail in certain situations due to library clashes but it will be enough to get your started in situations where you do not have control over the python environment at your studio (as is the usual case).

# Add support for more applications

If you want to add support for more interpreters like a different python version or another dcc application, you can simply add the appropriate command to [vfx-testrunner](vfx-testrunner):

```python
INTERPRETERS = {
    "python": "python",
    "maya": "mayapy",
    "nuke": "nuke -t",
    "houdini": "hython",
    "INTERPRETER_NAME": "COMMAND"
}
```

and supply a `{INTERPRETER_NAME}_test.py` in the root of this module with the appropriate code necessary to run the tests like in [python_test.py](python_test.py):

```python
import sys
import pytest

pytest.main(sys.argv[1:])
```

**Please feel free to contribute and add your improvements to this repo!**
