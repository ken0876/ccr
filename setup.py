from setuptools import find_packages, setup

setup(
    name='csv-comment-replacer',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'inquirer'
    ],
    entry_points={
        'console_scripts': [
            'csv = src.main:run',
        ],
    },
)