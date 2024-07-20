from setuptools import setup, find_packages

setup(
    name='ArtexSTT',
    version='0.0.1',
    author='Artex AI',
    description='A python speech to text library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JunaidParkar/Python-STT',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'selenium==4.22.0',
        'webdriver_manager==4.0.1',
        'mtranslate==1.8',
        'pathlib==1.0.1'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Boost Software License 1.0 (BSL-1.0)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    project_urls={
        'Documentation': 'https://github.com/JunaidParkar/Python-STT',
        'Source': 'https://github.com/JunaidParkar/Python-STT',
        'Tracker': 'https://github.com/JunaidParkar/Python-STT',
    },
)