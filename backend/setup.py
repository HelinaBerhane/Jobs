from setuptools import find_packages, setup

setup(
    name="jobs_api",
    version="0.1.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "jobs_api = api.__main__:cli",
        ],
    },
)
