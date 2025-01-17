from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='kripa_sindhu_resume',
  version='0.0.3',
  description='A very own private resume',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Kripa Sindhu',
  author_email='sindhukripa007@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='currency_convertor', 
  packages=find_packages(),
  install_requires=[''] 
)