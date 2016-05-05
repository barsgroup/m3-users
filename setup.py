# coding: utf-8
from pip.download import PipSession
from pip.req.req_file import parse_requirements
from setuptools import setup, find_packages


def _get_requirements(file_name):
    pip_session = PipSession()
    requirements = parse_requirements(file_name, session=pip_session)

    return tuple(str(requirement.req) for requirement in requirements)


setup(name='m3-users',
      version='2.1.0',
      url='https://bitbucket.org/barsgroup/m3_users',
      license='MIT',
      author='BARS Group',
      author_email='bars@bars-open.ru',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      description=u'Пользователи и роли',
      install_requires=_get_requirements('REQUIREMENTS'),
      include_package_data=True,
      classifiers=[
          'Intended Audience :: Developers',
          'Environment :: Web Environment',
          'Natural Language :: Russian',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'License :: OSI Approved :: MIT License',
          'Development Status :: 5 - Production/Stable',
      ],
)