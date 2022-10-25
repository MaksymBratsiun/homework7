from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='Clean folder and sort',
    url='https://github.com/MaksymBratsiun/homework7',
    author='Maksym Bratsiun',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']}
)
