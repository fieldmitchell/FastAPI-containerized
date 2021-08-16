import os
import setuptools

setuptools.setup(
    name='PACKAGE NAME',
    version=os.environ.get('PACKAGE_VERSION', '1.0.0'),
    packages=setuptools.find_packages(),
    python_requires='>=3.7'
)
