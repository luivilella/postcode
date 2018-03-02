import os
from setuptools import setup


def file_path(fname):
    return os.path.join(os.path.dirname(__file__), fname)


with open(file_path('requirements.txt')) as f:
    required = f.read().splitlines()


with open(file_path('README.md')) as f:
    readme = f.read()


setup(
    name="postcode",
    version="0.0.1",
    author="Luis Vilella",
    author_email="luivilella+postcode@gmail.com",
    description="Project to create validators for postcode.",
    keywords="postcode",
    url="https://github.com/luivilella/postcode",
    packages=['postcode', 'tests'],
    long_description=readme,
    install_reqs=required
)
