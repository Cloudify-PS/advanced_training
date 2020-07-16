from setuptools import setup

setup(
    name='cloudify-solution-plugin',
    version='0.1',
    description='Solution plugin for traning',
    author='Michael Shnizer',
    author_email='michael@cloudify.co',
    license='LICENSE',
    packages=['solution'],
    zip_safe=False,
    install_requires=[
        'cloudify-common>=5.0',
    ],
    test_requires=[
        "cloudify-common>=5.0"
        "nose"
    ]
)
