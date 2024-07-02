from setuptools import setup, find_packages

# Function to read the requirements.txt file
def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name='your_project_name',
    version='0.1',
    packages=find_packages(),
    install_requires=read_requirements(),
    # Additional metadata
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of your project',
    url='https://github.com/yourusername/yourproject',  # Replace with your project's URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Choose your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify your minimum Python version if needed
)