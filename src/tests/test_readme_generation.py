import os
import pytest
import shutil
from pyaoc.readme_generation import generate_readme

def test_readme_generation_year_out_of_range():
    shutil.copy("README.md", "save_README.md")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_readme(2010)
    assert pytest_wrapped_e.type == SystemExit
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_readme(-1)
    assert pytest_wrapped_e.type == SystemExit
    shutil.copy("save_README.md", "README.md")
    os.unlink("save_README.md")

def test_readme_generation_year_not_int():
    shutil.copy("README.md", "save_README.md")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        generate_readme("a")
    assert pytest_wrapped_e.type == SystemExit
    shutil.copy("save_README.md", "README.md")
    os.unlink("save_README.md")

def test_readme_generation_with_no_days():
    shutil.copy("README.md", "save_README.md")
    assert generate_readme() == None
    shutil.copy("save_README.md", "README.md")
    os.unlink("save_README.md")

def test_readme_generation_with_days():
    shutil.copy("README.md", "save_README.md")
    for i in range(1, 26):
        dir_name = f"day{i:02d}"
        os.mkdir(dir_name)
        os.mkdir(os.path.join(dir_name, "inputs"))
        with open(os.path.join(dir_name, "inputs", "input.txt"), "w") as f:
            pass
        with open(os.path.join(dir_name, "part1.py"), "w") as f:
            f.write("def solution(text): return 0")
        with open(os.path.join(dir_name, "part2.py"), "w") as f:
            f.write("def solution(text): return 0")
        os.mkdir(os.path.join(dir_name, "benchmark"))
        with open(os.path.join(dir_name, "benchmark", "benchmark.txt"), "w") as f:
            pass

    assert generate_readme() == None
    shutil.copy("save_README.md", "README.md")
    os.unlink("save_README.md")

    for i in range(1, 26):
        dir_name = f"day{i:02d}"
        shutil.rmtree(dir_name)