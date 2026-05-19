from setuptools import setup,find_packages

setup(
    name="crop_yield_prediction_system",
    version='1.1.1',
    author="Himadri Gowami",
    author_email="himadrigoswami191118@gmail.com",
    description="Crop yield Prediction Machine Learning System",
    license="MIT",

    package_dir={'':'src'},
    packages=find_packages(where='src'),
    
    include_package_data=True,
    python_requires=">=3.8"
)