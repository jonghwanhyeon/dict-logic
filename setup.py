from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as input_file:
    long_description = input_file.read()

setup(
    name='dict-logic',
    version='1.0.1',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jonghwanhyeon/dict-logic',
    author='Jonghwan Hyeon',
    author_email='hyeon0145@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords='dict logic',
    packages=find_packages(),
)
