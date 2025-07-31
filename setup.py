from setuptools import setup, find_packages

setup(
    name='django-settings',
    version='0.2.14',
    packages=find_packages(include=["django_settings", "django_settings.*"]),
    include_package_data=True,
    install_requires=[
        'Django>=3.2',
    ],
    author='Antwi Kwarteng',
    description='A type-safe class based settings for django.',
)
