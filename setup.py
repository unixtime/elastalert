# -*- coding: utf-8 -*-
import os

from setuptools import find_packages
from setuptools import setup


base_dir = os.path.dirname(__file__)
setup(
    name='elastalert',
    version='0.2.4',
    description='Runs custom filters on Elasticsearch and alerts on matches',
    author='Quentin Long',
    author_email='qlo@yelp.com',
    setup_requires='setuptools',
    license='Copyright 2014 Yelp',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': ['elastalert-create-index=elastalert.create_index:main',
                            'elastalert-test-rule=elastalert.test_rule:main',
                            'elastalert-rule-from-kibana=elastalert.rule_from_kibana:main',
                            'elastalert=elastalert.elastalert:main']},
    packages=find_packages(),
    package_data={'elastalert': ['schema.yaml', 'es_mappings/**/*.json']},
    install_requires=[
        'apscheduler>=3.6.3',
        'aws-requests-auth>=0.4.3',
        'blist>=1.3.6',
        'boto3>=1.14.47',
        'configparser>=5.0.0',
        'croniter>=0.3.34',
        'elasticsearch==7.6.0',
        'envparse>=0.2.0',
        'exotel>=0.1.5',
        'jira>=2.0.0',
        'jsonschema>=3.2.0',
        'mock>=4.0.2',
        'prison>=0.1.3',
        'PyStaticConfiguration>=0.10.5',
        'python-dateutil>=2.8.1',
        'PyYAML>=5.3.1',
        'requests>=2.24.0',
        'stomp.py>=6.1.0',
        'texttable>=1.6.2',
        'twilio>=6.45.0',
        'python-magic>=0.4.18',
        'cffi>=1.14.2'
    ]
)
