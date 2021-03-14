from setuptools import setup
#from biketrauma import __version__ as current_version

setup(
  name='bike_3trauma',
  version= '0.0.1',
  description='Visualization of a bicycle accident db',
  url='https://github.com/KamalAyoubi/packaging_tutorial',
  author='K.Ayoubi',
  author_email='xxxxxxxxxx@xxxxxxxxxxxxx.xxx',
  license='MIT',
  packages=['bike_3trauma','bike_3trauma.io', 'bike_3trauma.preprocess', 'bike_3trauma.vis'],
  zip_safe=False
)