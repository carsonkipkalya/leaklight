from pathlib import Path


def test_app_file_exists():
    app_file = Path("src/leaklight/app.py")
    assert app_file.is_file()


def test_app_contains_leaklight_title():
    app_file = Path("src/leaklight/app.py")
    content = app_file.read_text(encoding="utf-8")
    assert 'st.title("Leaklight")' in content
