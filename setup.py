from setuptools import find_packages, setup

setup(
    name='query_logger',
    author="Mattia Procopio",
    author_email="promat85@gmail.com",
    version='0.1.0',
    description="Utility for logging queries while running on `DEBUG = False`",
    license='BSD License',
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
