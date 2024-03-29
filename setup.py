import re
from setuptools import setup, find_packages
import os

VERSION_RE = r"__version__\s*=\s*[\'\"]([0-9]+\.[0-9]+\.[0-9]+[0-9a-z]*)[\'\"]"

DESCRIPTION = "Administrative API for the QEng quest engine"


def get_version() -> str:
    version_file = os.path.abspath(os.path.join(__file__, "..", "qeng", "version.py"))
    with open(version_file, "r") as f:
        version_file_text = "".join(f)
    version = re.findall(VERSION_RE, version_file_text)[0]
    return version


setup(
    name="qeng_admin_api",
    version=get_version(),
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    author="phaust94",
    author_email="phaust94@gmail.com",
    packages=find_packages(),
    project_urls={
        "Homepage": "https://github.com/Phaust94/qeng_admin_api",
    }
)