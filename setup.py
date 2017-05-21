from setuptools import setup, find_packages

setup(
        name='data_analysis',
        version='0.0.1',
        url='www.github.com/TripleR007/data-analysis',
        license='BSD',
        author='Randy Ross',
        packages=find_packages(),
        install_requires=['PyQt5', 'pandas', 'sqlalchemy', 'nltk', 'numpy', 'jupyter', 'PyQtChart', 'lda', 'matplotlib', 'scipy', 'tweepy'],
        entry_points={},
        extras_require={'dev': ['flake8',]},
        )
