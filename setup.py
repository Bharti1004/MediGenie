#here we are setting our local package
#we use bcoz initially it dont contain gen AI ..So we have to install it using -e . package

from setuptools import find_packages, setup
setup(
    name='Generative AI Project',
    version='0.0.0',
    author='Bharti Jain',
    author_email='bhartijain033@gmail.com',
    packages=find_packages(),  # it find the _init_.py , when it finds it consider it local
    install_requires=[]
)

#we may check that gen AI has now included in pip list