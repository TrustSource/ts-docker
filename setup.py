from setuptools import setup

setup(
    name='ts-docker',

    packages=['ts_docker'],

    version='1.1.0',

    description='A Docker scanner for TrustSource (https://app.trustsource.io) to manage open source code compliance',

    author='EACG GmbH',

    license='ASL-2.0',

    url='https://github.com/TrustSource/ts-docker.git',

    download_url='',

    keywords=['scanning', 'dependencies', 'modules', 'TrustSource', 'Docker'],

    classifiers=[],

    install_requires=[
        'click',
        'wasabi',
        'docker',
        'ts-python-client==1.2.0',
        'ts-spdx-import @ git+https://github.com/TrustSource/ts-spdx-upload.git@1.1.0#egg=ts-spdx-import'
    ],

    scripts=['ts-docker'],

    entry_points={
        'console_scripts': ['ts-docker=ts_docker.cli:main'],
    },
)