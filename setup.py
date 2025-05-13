import setuptools
import distutils.core

setuptools.setup(
    name='kde-wallpaper-cli',
    version="1.0.1",
    author='@readwithai',
    long_description_content_type='text/markdown',
    author_email='talwrii@gmail.com',
    description='Set the wallpaper for KDE',
    license='MIT',
    keywords='KDE,wallpaper',
    url='',
    packages=["kde_wallpaper_cli"],
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': ['kde-wallpaper=kde_wallpaper_cli.main:main']
    }
)
