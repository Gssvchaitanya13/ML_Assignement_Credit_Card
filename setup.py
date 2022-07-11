from setuptools import setup
PROJECT_NAME="credit_card_prediction"
AUTHOR="gssv"
VERSION="0.0.1"
PACKAGES=["credit_card"]
DESCRIPTION="This is Credit Card Project"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list():
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()
setup(
    name=PROJECT_NAME,
    author=AUTHOR,
    version=VERSION,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()

)