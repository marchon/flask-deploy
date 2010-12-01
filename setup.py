"""
Flask-Dozer
-------------

"""
from setuptools import setup


setup(
    name='Flask-Deploy',
    version='0.1',
    url='http://imlucas.com/',
    license='BSD',
    author='Lucas Hrabovsky',
    author_email='hrabovsky.lucas@gmail.com',
    description='Canned dxeploytment workflow with fabric.',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'Fabric'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)