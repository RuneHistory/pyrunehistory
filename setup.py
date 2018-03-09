from setuptools import setup, find_packages

github = 'https://github.com/jmwri/pyrunehistory'
version = '0.0.1'

setup(
    name='pyrunehistory',
    packages=find_packages(),
    version=version,
    license='MIT',
    python_requires='>=3.6, <4',
    description='RuneHistory API client',
    author='Jim Wright',
    author_email='jmwri93@gmail.com',
    url=github,
    download_url='{github}/archive/{version}.tar.gz'.format(
        github=github, version=version
    ),
    keywords=['runehistory', 'api', 'client'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'typing',
        'requests>=2.18,<3',
    ],
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-watch', 'tox',
                 'python-dateutil>=2.6.1,<3']
    },
    test_suite='tests',
)
