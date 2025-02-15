from importlib.metadata import version

import inferax


def test_version():
    assert version('inferax') == inferax.__version__
