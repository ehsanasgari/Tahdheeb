from setuptools import setup, find_packages

setup(
    name='Tahdheeb',
    version='0.1.1',
    author='Ehsaneddin Asgari and Yassine Elkheir',
    author_email='easgari@hbku.edu.qa/yelkheir@hbku.edu.qa',
    description='An Arabic Preprocessing Toolkit for Pretraining of LLM',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ehsanasgari/Tahdheeb',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
