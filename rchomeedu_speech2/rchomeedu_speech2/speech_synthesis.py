import rclpy    
import rclpy.node    
from std_msgs.msg import String    
    
from gtts import gTTS
import os

class SpeechSynthesis(rclpy.node.Node):        
    def __init__(self):        
        super().__init__("speech_synthesis")

        self.logger = self.get_logger()    
        self.logger.info("Begin speech synthesis. Waiting for the text input...")

        self.answer_sub = self.create_subscription(String, "answer_text", self.answer_subscribe, 10)
        
    def answer_subscribe(self, msg):
        self.logger.info("Subscribed text: '{}'".format(msg.data))
        tts = gTTS(msg.data)
        tts.save("voice.mp3")
        
        os.system("mpg321 voice.mp3")
        self.logger.info("Completed. Waiting for the next text input...")
        os.remove("voice.mp3")
    
def main():        
    rclpy.init()        
        
    speech_synthesis = SpeechSynthesis()
    
    try:
        rclpy.spin(speech_synthesis)
    except:
        speech_synthesis.destroy_node()

    rclpy.shutdown()