import importlib_metadata

import inferax


def test_version():
    assert importlib_metadata.version('inferax') == inferax.__version__
