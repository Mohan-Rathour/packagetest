from setuptools import setup

setup(name='pack',
      version='0.1',
      description='Package test',
      url='ssh://git@git.pbs.org:7999/~msingh/packagetest.git',
      author='Mohan Rathour',
      author_email='mohanpratap.singh@excelindia.com',
      license='MIT',
      packages=['packagetest'],
      zip_safe=False)