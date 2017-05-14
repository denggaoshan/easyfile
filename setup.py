from distutils.core import setup  

PACKAGE = "easyfile"
NAME = "easyfile"
DESCRIPTION = "Make python files operation easier!"
AUTHOR = "denggaoshan"
AUTHOR_EMAIL = "gaoshan.deng@foxmail.com"
URL = "https://github.com/denggaoshan/easyfile"

VERSION = "0.1.0"


def read(filenanme):
    with open(filenanme,'r') as f:
        return f.read()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read("README.md"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=["easyfile"],
)