from distutils.core import setup  

PACKAGE = "easyfile"
NAME = "easyfile"
DESCRIPTION = "Make python files operation easier!"
AUTHOR = "denggaoshan"
AUTHOR_EMAIL = "gaoshan.deng@foxmail.com"


VERSION = "0.1.0"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    #long_description=read("README.rst"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    #url=URL,
    packages=["easyfile"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    zip_safe=False,
)