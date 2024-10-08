from setuptools import setup

setup(
    name='ts-docker',

    packages=['ts_docker'],

    version='1.2.0',

    description='A Docker scanner for TrustSource (https://app.trustsource.io) to manage open source code compliance',

    author='EACG GmbH',

    license='Apache-2.0',

    url='https://github.com/TrustSource/ts-docker.git',

    download_url='',

    keywords=['scanning', 'dependencies', 'modules', 'TrustSource', 'Docker'],

    classifiers=[],

    install_requires=[
        'click',
        'wasabi',
        'docker',
        'ts-python-client==1.3.0',
        'ts-spdx-import @ git+https://github.com/TrustSource/ts-spdx-upload.git@1.2.0#egg=ts-spdx-import'
        'setuptools'
    ],

    scripts=['ts-docker'],

    entry_points={
        'console_scripts': ['ts-docker=ts_docker.cli:main'],
    },
)
"""
provides a setup routine to install ts-docker cli
"""
