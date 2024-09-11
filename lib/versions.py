def python_version():
    import sys
    return sys.version_info

def requests_version():
    import requests
    return requests.__version__

def pytest_version():
    import pytest
    return pytest.__version__
