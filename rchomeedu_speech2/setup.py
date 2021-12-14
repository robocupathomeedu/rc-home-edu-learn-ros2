from setuptools import setup
import os
from glob import glob

package_name = 'rchomeedu_speech2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jupiter',
    maintainer_email='i@jeffreytan.org',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'speech_synthesis = rchomeedu_speech2.speech_synthesis:main',
            'speech_recognition = rchomeedu_speech2.speech_recognition:main',
            'question_answer = rchomeedu_speech2.question_answer:main',
        ],
    },
)
