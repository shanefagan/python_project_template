import datetime

from setuptools import setup

version = datetime.datetime.now().strftime("%Y%m%d")
with open("VERSION", "w") as version_file:
    version_file.write(version)

setup(name="Project Name", version=version, packages=["project_name"], scripts=["bin/app.py"])
