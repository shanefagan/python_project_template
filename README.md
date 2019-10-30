# project_template

A basic project template to get some of the boring stuff out of the way. This assumes you are only going to use docker/docker-compose to ship your code. If you want to publish your module to pypi you will have to work on the setup.py file a bit to get it working. I made a minimal version just to be functional as a package just in case and to keep the code clean. Once you get up and running you should have a running instance of the most recent version of python, your code running in a container by itself and you can start adding other services to your docker-compose.yml file to build your service.

## Suggested Usage

* Start by renaming project_name to your actual project name
* Go to setup.py and change project_name in there too to match your project name
* Use Pycharm's docker-compose interperator feature if you can https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html alternatively you can do `docker-compose build` `docker-compose up` but Pycharm is almost worth it for the interperator feature (I don't work for them but it's just cool)
* Your main code goes in bin/app.py and any reusable code goes in the folder that was called project_name (now the name of your project). 
* When you need to add a library add it with pipenv install package_name your project package is included by default with this template
* Whenever you run pipenv update it will generate a new VERSION file for you. It is designed for people doing daily builds who don't care too much about version numbering. If you don't want that remove it from setup.py and make your own VERSION file.
* There is a sample for github actions to build the docker containers and push them to a repository in .github/workflows/main.yml.example with some explanation of how to use it included
* The fun with this approach is when you use the docker container directly without the docker-compose part, you can use the libraries you create directly in the repl for exporing or you could set up a docker compose file just for testing your code only if you want to test your code and the dependencies. 

When you want to run your code you can run with Pycharm's run feature, just right click and click run when you change app.pp. If you change something in the library then you will have to do a `docker-compose build` to update it in the docker container. 

## Not in the template but helpful

* Sphinx is the normal documentation format
* http://www.sphinx-doc.org/en/master/
* Docstrings like below are really nice in Sphinx
* Use type hints because they are really helpful
* Useful commands for Sphinx:
  * `pipenv run sphinx-apidoc -o source/module_name module_name`
  * `pipenv run sphinx-quickstart`
  * `pipenv run make html`
* Configuration is in the conf.py file and to edit the docs change the .rst files

```python 
def some_method(method_param_name: str = ''):
   '''Short description of your method.

   Longer description of the method.

   :param method_parm_name: some description of the text
   '''
```

## Pre-commit hooks

I added a small example of pre-commit hooks. The way they work is they are repeating things before doing certain git
actions. The docs are available https://pre-commit.com/

* In the .pre-commit-config.yaml file it has all the configs
* To install the hook so it actually runs run `pipenv run pre-commit install`
* To configure the hooks to play nice you should use whatever configuration file they use.
For Black I added some sample settings to `pyproject.toml` which should be a start. 