from setuptools import setup
import os

package_name = 'isaac_ros_system'

# List all files in the 'launch' directory
launch_files = [os.path.join('launch', file) for file in os.listdir('launch') if file.endswith('.launch.py')]

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Install all launch files
        (os.path.join('share', package_name, 'launch'), launch_files),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mohamed Abdelkader',
    maintainer_email='mohamedashraf123@gmail.com',
    description='ROS2 package for launching components of the ISAAC ROS packages',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Add your nodes here
        ],
    },
)
