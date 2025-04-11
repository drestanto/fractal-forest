from setuptools import setup, find_packages

setup(
    name="fractal-forest",  # Name of the package
    version="0.1.0",  # Initial version
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[],  # List of dependencies (empty for now, add as needed)
    author="Drestanto Muhammad Dyasputro",
    author_email="dyas@live.com",
    description="A library for managing hierarchical numerical data structures",  # Short description
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",  # Format of the long description
    url="https://github.com/drestanto/fractal-forest",  # Link to your project’s repository
    license="MIT",  # Choose your license (MIT in this case)
    classifiers=[  # Classifiers help users find your project
        "Programming Language :: Python :: 3",  # Python 3 compatibility
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",  # Works on any OS
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
