from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='fgrequests',
    version='0.0.4',
    description='Fastest async group request package for Python',
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    url='https://github.com/faridlu/fgrequests',
    author='Farid Chowdhury',
    author_email='faridstudylu@gmail.com',
    keywords='Fastest async group requests python multiple threading',
    py_modules=['fgrequests'],
    install_requires=[
        'requests',
        'futures',
    ],
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    extra_require = {
        'dev': [
            'pytest>=3.7',
        ],
    }  
)
