from distutils.core import setup
setup(
  name = 'rnasieve',
  packages = ['rnasieve'],
  version = '0.1',
  license='MIT',
  description = 'A library for the statistical deconvolution of RNA bulk samples with single-cell references.',
  author = 'Justin Hong',
  author_email = 'justinhong@berkeley.edu',
  url = 'https://github.com/jjhong922/rnasieve',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['rna', 'deconvolution', 'statistics', 'single-cell', 'proportion', 'bulk'],
  install_requires=[
          'numpy',
          'cvxpy',
          'scipy',
          'pandas',
          'altair',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Computational Biologists',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
