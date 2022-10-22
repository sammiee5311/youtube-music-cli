from setuptools import find_packages, setup

requires = [
    "python-vlc",
    "google-api-python-client",
    "youtube-dl==2020.12.2",
    "python-dotenv",
    "pafy",
    "click",
]

dev_requires = [
    "black",
    "pytest",
    "pytest-cov",
    "tox",
]

if __name__ == "__main__":
    setup(
        name="youtube-music-cli",
        version="0.1.0",
        description="youtube music cli.",
        author="sammiee5311",
        packages=find_packages(exclude=("tests")),
        install_requires=requires,
        extras_require={"dev": dev_requires},
        license="MIT",
    )
