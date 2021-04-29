from distutils.core import setup

setup(
    name='mehrshad',
    packages=['mehrshad'],
    version='0.2-beta',
    description='A Python 3 module that contains all of my collections to let you code easier!',
    author='Mehrshad Dadashzadeh',
    author_email='mehrdadashzadeh1379@gmail.com',
    url='https://github.com/mehrshaad/mehrshad-pypi',
    license='MIT',
    download_url='https://github.com/mehrshaad/mehrshad-pypi/archive/refs/tags/v0.1-beta.tar.gz',
    keywords=['mehrshad', 'json', 'excel', 'pygame'],
    install_requires=['tqdm', 'win10toast',
                      'py-notifier', 'pathlib', 'openpyxl', 'pygame'],
    classifiers=classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Operating System :: Linux',
        'Programming Language :: Python :: 3',
    ],
)
