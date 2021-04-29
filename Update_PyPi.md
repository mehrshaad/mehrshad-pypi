# Update PyPi package

## Clone current version from GitHub
```
git clone https://github.com/mehrshaad/mehrshad-pypi
```
Update the project locally

## Test in development
Assuming you’re in the root of your project directory, then run:
```
pip install -e .
```

## Create source distribution
Minimally, you should create a Source Distribution:
```
python setup.py sdist
```

## Create 'wheel'
You should also create a wheel for your project. 
A wheel is a built package that can be installed without needing to go through the “build” process. 
Installing wheels is substantially faster for the end user than installing from a source distribution.
Universal Wheels are wheels that are pure Python and support Python 2 and 3. 
This is a wheel that can be installed anywhere by pip.
```
python setup.py bdist_wheel
```
Only use the `--universal` setting, if:
* Your project runs on Python 2 and 3 with no changes.
* Your project does not have any `C` extensions.

## Install 'twine'
```
pip install twine
```

## Upload distribution to Pypi
```
twine upload dist/*
```
You can see if your package has successfully uploaded by navigating
to the URL https://pypi.org/project/mehrshad/ where `mehrshad` is the name of your project that you uploaded. 
It may take a minute or two for your project to appear on the site.

## Reference
* [Working in “Development Mode”](https://packaging.python.org/tutorials/distributing-packages/#working-in-development-mode)
* [Uploading your Project to PyPI](https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi)