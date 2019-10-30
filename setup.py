import datetime

from setuptools import setup

# Generate a VERSION file when the package is imported into pipenv
# changes daily, mainly designed for my laziness when it comes to
# versioning software
version = datetime.datetime.now().strftime("%Y%m%d")
with open("VERSION", "w") as version_file:
    version_file.write(version)

setup(name="Project Name", version=version, packages=["project_name"], scripts=["bin/app.py"])
