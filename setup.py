from setuptools import setup, find_packages

setup(
    name = "django-french-ping-calculator",
    version = "1.0",
    url = 'http://github.com/',
    license = 'WTFPL',
    description = "Calculateur de point pour le tennis de tabl",
    author = 'Ulakanakulot',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)
