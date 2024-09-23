from setuptools import setup, find_packages

setup(
    name="own_sqlite_orm",
    version="0.2.1",
    author="LoloCG",
    author_email="",
    description="Personal SQLite ORM for light weight applications.",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/LoloCG/PersonalPythonPackage",
    packages=find_packages(include=['own_sqlite_orm', 'own_sqlite_orm.*']),
    # packages=find_packages(), 
    # packages=['Databases.own_sqlite_orm'], 
    install_requires=[], # SQLite is built-in, so no base dependencies
    extras_require={
        'sqlite': [],
        'sqlite_pandas': ['pandas'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)



