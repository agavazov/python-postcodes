from setuptools import setup, find_packages
import unittest


# Define test suite settings
def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


# Open README file and set it as long_description
with open("README.md", "r") as f:
    long_description = f.read()

# Configure python setup() settings
setup(
    name="postcode-task",
    version="0.1",
    description="Get postcodes lon/lat and sort them by direction or filter them by radius",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Alexander Gavazov",
    author_email="alex@atlantify.com",
    url="https://github.com/agavazov",
    install_requires=[
        "Flask"
    ],
    test_suite='setup.my_test_suite',
    packages=find_packages(),
    scripts=[
        "foo/bar",
        "asd/fgh",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
