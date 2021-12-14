from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rchomeedu_speech2',
            executable='speech_synthesis',
            name='speech_synthesis'
        ),
        Node(
            package='rchomeedu_speech2',
            executable='speech_recognition',
            name='speech_recognition'
        ),
        Node(
            package='rchomeedu_speech2',
            executable='question_answer',
            name='question_answer'
        )
    ])
