import sys

import pytest
import maya.standalone


maya.standalone.initialize(name="python")


pytest.main(sys.argv[1:])
