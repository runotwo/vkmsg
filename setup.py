import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vkmsg",
    version="0.1",
    author="runotwo",
    description="Simple but yet functional library for building VK bots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/runotwo/vkmsg",
    packages=setuptools.find_packages(exclude=['tests*', 'examples*']),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests'],
    python_requires='>=3.6',
)
