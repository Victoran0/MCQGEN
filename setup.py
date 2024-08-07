from setuptools import find_packages, setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Victor Oluwadare',
    author_email='victorano69@mail.com',
    install_requires=["openai", "langchain",
                      "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)

# We install this setup with the command: python setup.py install
# Then the mcqgenerator and wvery folder in our project directory with the __init__.py file becomes a package folder
