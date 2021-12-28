import setuptools

setuptools.setup(
    name="this-is-alpen-package-master",
    version="0.0.1",
    author="Anton",
    author_email="lotrus@yandex.ru",
    description="Testing how packages work",
    url="git@github.com:Alpensin/package-hello-world.git",
    project_urls={
        "Just Google": "https://www.google.com/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=[
        "certifi==2021.10.8",
        "charset-normalizer==2.0.9",
        "click==8.0.3",
        "gTTS==2.2.3",
        "idna==3.3",
        "playsound==1.3.0",
        "pyttsx3==2.90",
        "requests==2.26.0",
        "six==1.16.0",
        "text-to-voice==0.0.1",
        "urllib3==1.26.7",
    ],
    entry_points={
    'console_scripts': [
        'run-this=hello_world:main',
    ],
},
)