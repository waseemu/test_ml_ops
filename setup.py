from setuptools import setup,find_packages

def get_requirements(file_path):
    requirements = []
    with open(file_path,'r') as f:
        requirements = f.readlines()
        requirements=[req.replace('\n','') for req in requirements]
    return requirements


setup(
    name="Data Science Project",
    version='0.0.1',
    author="Waseemullah",
    author_email="waseemu@cloud.neduet.edu.pk",
    #packages=['numpy','pandas'],
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt')
)