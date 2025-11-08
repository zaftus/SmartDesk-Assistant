import os
from smartdesk.automation import Automation

def test_organize_folder(tmp_path):
    # Create dummy files
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.pdf"
    file1.write_text("Hello")
    file2.write_text("PDF content")

    Automation.organize_folder(tmp_path)
    # Check folders created
    assert (tmp_path / "txt" / "file1.txt").exists()
    assert (tmp_path / "pdf" / "file2.pdf").exists()
