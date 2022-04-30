## Learn Python

Code exercises and examples

### Setup


#### virtualenv

```
# Create virtualenv
$ python3.9 -m venv venv

# Switch to venv
$ source venv/bin/activate

# Install pip-tools
$ pip install pip-tools

# Add requirements in requirements.in
# Generate requirements.txt (will already part of project)
$ pip-compile requirements/requirements.in

# You can use inheritance in requirements.in files, eg. check dev-requirements.in file
$ pip-compile requirements/dev-requirements.in

# Install packages in the environment
$ pip-sync requirements/dev-requirements.txt


```

#### VSCode
Make sure there is a .vscode folder with settings.json file
This has set `black` and `flake8` formatters and linting tools for python
