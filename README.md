# project_template

A basic project template to get some of the boring stuff out of the way. This assumes you are only going to use docker/docker-compose to ship your code. If you want to publish your module to pypi you will have to work on the setup.py file a bit to get it working. I made a minimal version just to be functional as a package just in case and to keep the code clean. Once you get up and running you should have a running instance of the most recent version of python, your code running in a container by itself and you can start adding other services to your docker-compose.yml file to build your service.

## Suggested Usage

1. Start by renaming project_name to your actual project name
2. Go to setup.py and change project_name in there too to match your project name
3. Use Pycharm's docker-compose interperator feature https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html
4. When you need to add a library add it with pipenv install package_name your project package is included by default with this template
5. Whenever you run pipenv update it will generate a new VERSION file for you. It is designed for people doing daily builds who don't care too much about version numbering. If you don't want that remove it from setup.py and make your own VERSION file.
6. There is a sample for github actions to build the docker containers and push them to a repository in .github/workflows/main.yml.example with some explanation of how to use it included
When you want to run your code you can run with Pycharm's run feature, just right click and click run when you change app.pp. If you change something in the library then you will have to do a `docker-compose build` to update it in the docker container. 
