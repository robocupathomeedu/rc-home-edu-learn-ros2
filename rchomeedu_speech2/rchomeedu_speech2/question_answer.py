import rclpy
import rclpy.node
from std_msgs.msg import String

import Levenshtein

class QuestionAnswer(rclpy.node.Node):    
    def __init__(self):    
        super().__init__("question_answer")
    
        self.logger = self.get_logger()
        self.logger.info("Begin question and answer")

        self.questions = {
            "Bring me a bottle from the kitchen":"OK, I will go to the kitchen",
            "Fetch me a book from the study room":"Alright, I will go to the study room"
        }

        self.text_sub = self.create_subscription(String, "recognized_text", self.question_answer, 10)
        self.answer_pub = self.create_publisher(String, "answer_text", 10)
    
    def question_answer(self, msg):
        self.logger.info("Subscribed text: '{}'".format(msg.data))

        answer = ""
        ratio = 0.0
        t_ratio = 0.0

        for key, value in self.questions.items():
            t_ratio = Levenshtein.ratio(msg.data, key)
            #self.logger.info("Ratio: {} | Compared '{}' and '{}'".format(round(t_ratio, 3), key, msg.data))

            if t_ratio > ratio:
                ratio = t_ratio
                answer = value
                self.logger.info("Ratio: {} | Compared '{}' and '{}'".format(round(t_ratio, 3), key, answer))

        if ratio > 0.8:
            msg = String()
            msg.data = answer
            self.answer_pub.publish(msg)
            self.logger.info("Published answer: '{}'".format(msg.data))
    
def main():    
    rclpy.init()    
    
    question_answer = QuestionAnswer()

    try:
        rclpy.spin(question_answer)
    except:
        question_answer.destroy_node()

    rclpy.shutdown()