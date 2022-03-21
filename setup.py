import setuptools

setuptools.setup(
    name="fit2pd",
    version="0.0.1",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'fitparse>=1.2.0',
        'pandas>=1.1.5'
    ])
