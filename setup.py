from setuptools import setup, find_packages

setup(
    name='hireme-clg',
    version='0.1',
    packages=[],   
    py_modules=['clg'],   
    package_dir={"": "src"},
    install_requires=[
        'python-docx',
        'docx2pdf'
    ],
    entry_points={
        'console_scripts': [
            'HireMe = clg:main' 
        ]
    }
)
