from setuptools import setup, find_packages
import os.path

install_requires = [
    'PyYAML',
    'charmhelpers>=0.5.0'
]

tests_require = [
    'coverage',
    'nose',
    'pep8',
]

HERE = os.path.dirname(__file__)
with open(os.path.join(HERE, 'VERSION')) as f:
    VERSION = f.read().strip()

setup(
    name='charms.benchmark',
    version=VERSION,
    author='Adam Israel',
    author_email='adam@adamisrael.com',
    description='Library to aid in the creation of benchmark actions in Juju',
    install_requires=install_requires,
    url="https://github.com/juju-solutions/charms.benchmark",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'benchmark-start = charms.benchmark.cli.start:main',
            'benchmark-finish = charms.benchmark.cli.finish:main',
            'benchmark-actions = charms.benchmark.cli.actions:main',
            'benchmark-composite = charms.benchmark.cli.composite:main',
            # An alias for benchmark-composite
            'benchmark-result = charms.benchmark.cli.composite:main',
            'benchmark-meta = charms.benchmark.cli.meta:main',
            'benchmark-data = charms.benchmark.cli.data:main',
            'benchmark-raw = charms.benchmark.cli.raw:main',
        ]
    }
)
