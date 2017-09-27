from setuptools import setup

setup(
    name = "fixtags",
    packages = ["fixtags"],
    install_requires = ["mutagen"],
    entry_points = {
        "console_scripts": ['fixtags = fixtags.fixtags:main']
        },
    version = "0.1",
    description = "A Python program that corrects the track tags on the specified file",
    author = "Steven Smith",
    author_email = "stevensmith.ome@gmail.com",
    license = "MIT",
    url = "https://blha303.github.io/fixtags/",
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "Topic :: Multimedia :: Sound/Audio"
        ]
    )
