from setuptools import setup

setup(
    name='clean_folder',
    version='1',
    description='Clean folder program by Python',
    author='yulyan407',
    author_email='yu_lyan@ukr.net',
    url='https://github.com/yulyan407/GoIT_HomeWork_7',
    license='MIT',
    packages=['clean_folder'],
    include_package_data=True,
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)
