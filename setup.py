from setuptools import setup, find_packages

setup(
        name = 'motor',
        version = '0.1dev',
        description = 'Abstract class for controlling Dynamixel motors',
        classifiers = [
            'Development Status :: 3 - Alpha',
            'License :: OSI Approves :: MIT License',
            'Programming Language :: Python :: 3.6',
            'Topic :: Text Processing :: Hardware Interface',
            ],
        keywords = 'dynamixel control',
        url = 'https://github.com/SRMTH/motor.git',
        author = 'Piyush Jaipuriyar',
        author_email = 'piyushjaipuriyar@gmail.com',
        license = 'MIT',
        packages = find_packages(),
        install_requires = [
            'dynamixel_sdk',
            ]
        )
