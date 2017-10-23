from distutils.core import setup

setup(
    name='rentright', version='1.0', author='lhennessy',
    author_email='loganjhennessy@gmail.com',
    packages=[
        'rentright',
        'rentright.bin', 
        'rentright.model', 
        'rentright.scraper', 
        'rentright.scrubber', 
        'rentright.utils',
    ],
    install_requies=[
        'bs4',
        'fake_useragent',
        'pymongo',
    ],
    url='https://github.com/loganjhennessy/rent-right'
)