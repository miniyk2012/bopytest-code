"""Some tests that use temp data files."""
import json


def test_brian_in_portland(author_file_json):
    """A test that uses a data file."""
    with author_file_json.open() as f:
        authors = json.load(f)
    assert authors['Brian']['City'] == 'Portland'

