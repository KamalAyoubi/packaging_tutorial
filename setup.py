from setuptools import setup
from biketrauma import __version__ as current_version

setup(
  name='biketrauma',
  version=current_version,
  description='Visualization of a bicycle accident db',
  url='https://github.com/KamalAyoubi/packaging_tutorial',
  author='K.Ayoubi',
  author_email='xxxxxxxxxx@xxxxxxxxxxxxx.xxx',
  license='MIT',
  packages=['biketrauma','biketrauma.io', 'biketrauma.preprocess', 'biketrauma.vis'],
  zip_safe=False
)