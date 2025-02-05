from setuptools import setup, find_namespace_packages

setup(name = 'clean_folder',
      version = '0.1.0',
      description = 'Clean Folder Program',
      author = 'Paul Musquaro',
      author_email = 'paulren9200@ukr.net',
      packages = find_namespace_packages(),
      entry_points = {'console_scripts': ['clean_folder = clean_folder.clean:main']}
      )