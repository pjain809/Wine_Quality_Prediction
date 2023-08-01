from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "E2E-ML-Project-with-MLFlow"
AUTHOR_USER_NAME = "Paras Jain"
AUTHOR_MAIL = "Paras.Jain@eclerx.com"
GITHUB_USER_NAME = "pjain809"
SRC_REPO = "ML_PROJECT"

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_MAIL,
    description="Small Python Package for ML App",
    long_description=long_description,
    url=f"https://github.com/{GITHUB_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{GITHUB_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
)
