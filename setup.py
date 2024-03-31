# find and install the available packages used in the project
from setuptools import find_packages,setup
# to mention the List as a return type of a function
from typing import List

# require to append the string at the end of the list of requirements read from requirements.txt
HYPEN_E_DOT='-e .'

# read requirements from requirements.txt
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

# project metadata
setup(
name='GenericProjectStructure_ML',
version='0.0.1',
author='Subhankar',
author_email='subhankar.130495@gmail.com',
packages=find_packages(),

# we can list down the requirements as follows
# install_requires=['pandas', 'numpy']

# we can mention the required packages in 'requirements.txt' file and then import it
install_requires=get_requirements('requirements.txt')
)