from pathlib import Path
from setuptools import setup, find_packages

here = Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='bili-spyder',
    version='0.2.0',
    description="Calculating the signature of the Bilibili's heartbeat requests",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='acgnhiki',
    author_email='acgnhiki@outlook.com',
    keywords='bilibili, live, heartbeat, sign, spyder',
    url='https://github.com/acgnhiki/bili-spyder',
    project_urls={
        'Source Code': 'https://github.com/acgnhiki/bili-spyder/',
        'Bug Tracker': 'https://github.com/acgnhiki/bili-spyder/issues',
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    python_requires='>=3.6',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    install_requires=['wasmtime>=0.19.0'],
)
