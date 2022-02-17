import setuptools

REQUIRED_PACKAGES = [
    'flask==2.0',
    "pyyaml==6.0",
    "imgkit==1.2",
    "Flask_WeasyPrint==0.6",
]

setuptools.setup(
    name='dos2-build',
    version='0.0.1',
    description='Divinity original Sin 2 Build Cards',
    maintainer='Romain Marret',
    maintainer_email='romain.marret@gmail.com',
    url='https://github.com/rmarret/dos2-build.git',
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages(),
)
