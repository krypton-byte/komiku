from setuptools import setup, find_packages
from os import path
base_dir = path.abspath(path.dirname(__file__))
setup(
  name = 'komiku',        
  packages = ['komiku'],
  include_package_data=True,
  version = '0.0.1',    
  license='MIT',     
  description = 'komiku', 
  author = 'Krypton Byte',                  
  author_email = 'galaxyvplus6434@gmail.com',     
  url = 'https://github.com/krypton-byte/komiku',   
  download_url = 'https://github.com/krypton-byte/komiku/archive/0.0.1.tar.gz',    
  keywords = ['manga', 'pdf', 'downloader', 'komik', 'komiku'], 
  install_requires=[           
          'pillow',
          'requests',
          'bs4'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)