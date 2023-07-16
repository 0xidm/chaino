from setuptools import setup, find_packages

setup(
    version='0.1.0',
    name='chaino',
    description="chaino",
    packages=[
        'chaino',
    ],
    scripts=[],
    include_package_data=True,
    keywords='',
    author='0xidm',
    author_email='0xidm@protonmail.com',
    url='https://linktr.ee/0xidm',
    install_requires=[
        "pandas",
        "numpy",
        "web3==5.28.0",
        "python-dotenv",
        "click",
        "multicall",
        "pytest",
        "rich",
        "pdbpp",
    ],
    license='MIT',
    zip_safe=True,
)
