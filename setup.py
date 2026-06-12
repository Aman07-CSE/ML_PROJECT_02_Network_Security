'''
This Setup.py file is essential part of packaging and
distributing python projects. It is used by setuptools
(or distutils in older python versions) to define configuration 
of the project ,such as its metadata, dependency, and more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt",'r') as file:
            # read lines of/from the file
            lines=file.readlines()
            #process the each line
            for line in lines:
                requirement=line.strip()
                # ignoring the empty lines and -e. 
                if requirement and requirement  != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file is not found")

    return requirement_lst
    
setup(
    name="Network_Security",
    version="0.0.1",
    author="Aman",
    author_email="amanco____@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)