from importlib.metadata import version

import inferax as ix


def test_version():
    assert version('inferax') == ix.__version__
