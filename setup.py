from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

version='0.1.0'

setup(
    name='click-bash4.2-completion',
    author = 'Egor Abramov',
    author_email = 'coreegor@gmail.com',
    version=version,
    description="Bash 4.2 completion support for Click 8",
    py_modules=['click_bash42_completion'],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    download_url=f'https://github.com/coreegor/click-bash4.2-completion/archive/refs/tags/{version}.tar.gz',
    install_requires=[
        'click>=8.0.0,<9'
    ],
    python_requires='>=3.6',
    project_urls={
        'Source': 'https://github.com/coreegor/click-bash4.2-completion',
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]

)
