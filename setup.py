from setuptools import find_packages, setup


if __name__ == '__main__':
    setup(
        name='pseudo_lidar',
        version='0.1.1',
        description='Human Parser from cozymantis/human-parser-comfyui-node',
        long_description='This repo is a fork from cozymantis/human-parser-comfyui-node',
        # long_description_content_type='text/markdown',
        author='Akmal Mukhsimov',
        author_email='aka.mukhsimov@gmail.com',
        keywords='computer vision, human part segmentation',
        url='https://github.com/amukhsimov/human-parser-comfyui-node',
        packages=['psmnet', 'psmnet.models'],
        # package_data={'schp.modules': ['src/*', 'src/utils/*']},
        # include_package_data=True,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
        ],
        license='Apache License 2.0',
        install_requires=[
            'torch==2.3.0',
            # 'opencv-python==4.8.0.76',
            # 'Ninja==1.11.1.1',
            # 'numpy==1.25.2'
        ]
        # extras_require={
        #     'eth_xgaze': parse_requirements('requirements.txt'),
        #     'tests': parse_requirements('requirements/tests.txt'),
        #     'build': parse_requirements('requirements/build.txt'),
        #     'optional': parse_requirements('requirements/optional.txt'),
        # },
        # ext_modules=[],
        # cmdclass={'build_ext': BuildExtension},
        # zip_safe=False
    )