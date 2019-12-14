from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

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
