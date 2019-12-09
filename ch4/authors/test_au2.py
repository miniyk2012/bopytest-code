"""Some tests that use temp data files."""
import json

def test_all_have_cities(author_file_json):
    """Same file is used for both tests."""
    print(type(author_file_json))  # py._path.local.LocalPath
    with author_file_json.open() as f:
        authors = json.load(f)
    for a in authors:
        assert len(authors[a]['City']) > 0

def test_all_have_cities2(author_file_json):
    """Same file is used for both tests."""
    with author_file_json.open() as f:
        authors = json.load(f)
    for a in authors:
        assert len(authors[a]['City']) > 0