try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'gwrobolib',
	'version': '0.1',
    'description': 'Robotics library to control a robot with a Raspberry Pi connected to an Arduino via serial',
    'author': 'Nam Tran',
    'url': 'https://github.com/GW-Robotics/gwrobolib',
    'download_url': 'https://github.com/GW-Robotics/gwrobolib/releases',
    'author_email': 'nam_tran@gwu.edu',
    'install_requires': ['nose'],
	'dependency_links' = ['http://github.com/GW-Robotics/nanpy/tarball/master#egg=Nanpy'],
	'license': 'MIT'
    'packages': ['gwrobolib'],
    'scripts': []
}

setup(**config)
