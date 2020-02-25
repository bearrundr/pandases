from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

extras_require = {
    "pandas": ["pandas"],
}

setup(
    name='pandases',
    version='0.1.0',
    author='bearrundr',
    author_email='bearrundr@hotmail.com',
    packages=['pandases', 'pandases.operators'],
    url='http://pypi.python.org/pypi/pandases/',
    license='MIT',
    description='A Pandas manuplication of  Elasticsearch client .',
    install_requires=required,
    extras_require=extras_require,
    test_suite='nose.collector',
    tests_require=['nose', 'mock'],
)
