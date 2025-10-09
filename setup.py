'''
This is file is an essential part of packaging and distributing python projects . it is used by setuptools to define the configuration of your project, such its metadata , dependencies and more 
'''

from setuptools import find_packages, setup 

## find package tool sab folder me jayega and scan karega __init__.py aur jisme hoga vo parent folder ek package ki tarah treat hoga 


from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of the requiremnts 
    '''
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            ## read lines from the file 
            lines = file.readlines()
            ## Process each line 
            for line in lines:
                requirement = line.strip()
                ## Ignore the empty line and -e. 
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    
    except FileNotFoundError:
        print("Requirements.txt file not found")

    return requirement_list


print(get_requirements())


setup(
    name="NetworkSecurity",
    version = "0.0.1",
    author="Shubh Patel",
    author_email="shubhnpatel@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
