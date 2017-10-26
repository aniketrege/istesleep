from setuptools import setup, find_packages

setup(author='Aniket Rege',
      description='A non contact sleep hygiene monitor in an IoT setup',
      name='istesleep',
      packages=find_packages(),
      install_requires=[
      'pyserial>=3.4',
      'numpy>=1.13.3',
      'smbus-cffi>=0.5.1',
      'pytz>=2017.2'      
      ],
      url='https://github.com/aniketrege/istesleep.git',
      version='0.1-alpha'
)