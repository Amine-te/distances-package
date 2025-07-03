from setuptools import setup, find_packages

setup(
    name="distancepy",
    version="0.1.0",
    author="Amine FARIS",
    author_email="farisamine13@example.com",
    description="A comprehensive distance metrics library implemented from scratch",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "openpyxl>=3.0.0",  # For Excel file support
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)