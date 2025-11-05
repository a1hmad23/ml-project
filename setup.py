from setuptools import find_packages, setup

HYPHEN_E_DOT='-e .' #added to requirements.txt to trigger setup.py
def get_requirements(file_path:str) -> list[str]:
    '''
    returns the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Ahmad',
    author_email='ahmad2001khan@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)