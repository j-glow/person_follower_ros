from setuptools import find_packages, setup
from glob import glob
import os

package_name = "nodes"
nn_models = glob(os.path.join("models","*.pt"))
launch_files = glob(os.path.join("launch","*.launch.py"))

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        ("share/" + package_name + "/models", nn_models),
        ("share/" + package_name + "/launch", launch_files)
    ],
    install_requires=["setuptools", "interfaces"],
    zip_safe=True,
    maintainer="j.glowacki",
    maintainer_email="jakubglowacki3@gmail.com",
    description="Package containing ROS-based nodes with logic regarding the engineering thesis project.",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "detector = nodes.detector:main",
            "moving_target = nodes.moving_target:main",
            "dummy_nav = nodes.dummy_nav:main"
        ],
    },
)
