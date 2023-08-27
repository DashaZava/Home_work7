from setuptools import setup

setup(
    name='clean_folder',
    version='0.1',
    description='Clean folder program by Python',
    author='DashaZava',
    author_email='Dashss_kirik49@ukr.net',
    url='https://github.com/DashaZava/Home_work7',
    license='MIT',
    packages=['clean_folder'],
    include_package_data=True,
    entry_points={'console_scripts': [
        'clean-folder = clean_folder.clean:main']}
)
