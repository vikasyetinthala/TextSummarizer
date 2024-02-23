from setuptools import setup, find_packages

with open("README.md",'r',encoding='utf-8') as f:
    long_description=f.read() 


__version__="0.0.0"

REPO_NAME="textsummarizer"
AUTHOR_USER_NAME="vikasyetinthala"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="vikasyetintala07@gmail.com"


setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer package",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"":"src"},
    packages=find_packages(where='src')
)