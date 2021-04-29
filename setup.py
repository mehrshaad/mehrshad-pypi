from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mehrshad',
    packages=['mehrshad'],
    version='0.3-beta',
    description='A Python 3 module that contains all of my collections to let you code easier!',
    long_description=long_description,
    long_description_content_type='text/markdown'
    author='Mehrshad Dadashzadeh',
    author_email='mehrdadashzadeh1379@gmail.com',
    url='https://github.com/mehrshaad/mehrshad-pypi',
    license='MIT',
    download_url='https://github.com/mehrshaad/mehrshad-pypi/archive/refs/tags/v0.2-beta.tar.gz',
    keywords=['mehrshad', 'json', 'excel', 'pygame'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
)
