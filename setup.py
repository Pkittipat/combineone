import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="combineeone",
    version="0.0.2",
    author="pkittipat",
    author_email="kittipat.phongsak@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pkittipat/combineone",
    # download_url="https://github.com/Pkittipat/combineone/releases/tag/0.0.3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
