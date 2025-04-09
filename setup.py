import setuptools
setuptools.setup(
    name="bp_percentile",
    version="0.1.0",
    author="VitalLab",
    author_email="vital@snu.ac.kr",
    description="Blood Pressure Percentile Calculation",
    long_description="Model Context Server for Blood Pressure Percentile Calculation",
    long_description_content_type="text/markdown",
    url="https://github.com/vitaldb/bp_percentile",
    install_requires=['mcp','scipy'],
    packages=['bp_percentile'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)