import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = []
# with open("requirements.txt") as f:
#     requirements = f.read().splitlines()

setuptools.setup(
    name="fantasy-names",
    version="1.0.0",
    author="Jens Reidel",
    author_email="jens.reidel@gmail.com",
    description="Generates fantasy item names",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kenvyra/fantasy-names",
    packages=setuptools.find_packages(),
    license="AGPLv3+",
    install_requires=requirements,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
