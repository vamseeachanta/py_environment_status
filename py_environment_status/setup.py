from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Python Environment Package Status'
LONG_DESCRIPTION = 'Python Environment Package Status helps in determining the package versions used ' \
                   'and relative version/timeline to the latest/stable versions'

requirements = [
]

# Setting up
setup(
    name="py_enviornment_status",
    version=VERSION,
    author="Vamsee Achanta",
    author_email="<vamsee.achanta@aceengineer.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)