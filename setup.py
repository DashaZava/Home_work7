from setuptools import setup, find_packages


setup(name='clean_folder',
      version='0.0.1',
      # packages=['cleen_folder'],
      packages=find_packages(),
      author='Daria_Zava',
      author_email='dasha_kirik49@ukr.net',
      description="clean folder from trash",
      entry_points={
          'console_scripts': ['clean-folder = clean_folder.clean:main',
                              'fill-fils = clean_folder_files_generator:file_generator']

      },
      install_requires=[
          'numpy',
          'Pillow',
      ],
      )
