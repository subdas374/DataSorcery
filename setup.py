"""setup.py is a script used in Python projects to define how the project should be installed and distributed. 
It is commonly used in projects that follow the Python packaging standards and use the setuptools library. 
The setup.py file typically contains metadata about the project, such as its name, version, author, description, and dependencies, among other things."""

from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT ='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirement
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name="DataSorcery",
    version="0.0.1",
    author="Subrata",
    author_email="subdas374@gmail.com",
    packages=find_packages(),
    requires=get_requirements("requirements.txt")
)