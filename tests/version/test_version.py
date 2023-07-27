import os
import pytest

from src.flask_meter import version

def test_read_version_file_ok():
    fake_version = '0.99.0'
    path = os.path.join(os.getcwd(), '.version')
    with open(path, 'w') as f:
        f.write(fake_version)

    result = version.read_version_file()

    assert fake_version == result

    os.remove(path)

    assert '' == version.read_version_file()