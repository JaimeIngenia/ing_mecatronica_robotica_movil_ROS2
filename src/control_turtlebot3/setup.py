from setuptools import setup

package_name = 'control_turtlebot3'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jaime',
    maintainer_email='jaime@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "nodo_publicador =  control_turtlebot3.ejercicio1:main",
            "nodo_publicador2 = control_turtlebot3.ejercicio2:main",
            "nodo_publicador3 = control_turtlebot3.ejercicio3:main"
        ],
    },
)
