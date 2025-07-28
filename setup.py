from setuptools import setup, find_packages

setup(
    name='django-settings',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.2',
    ],
    author='Antwi Kwarteng',
    description='A class based settings for django.',
)
