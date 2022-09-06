import logging
import os

# logging.basicConfig(filename='method.log', level= logging.INFO, format=' %(asctime)s %(level)s %(message)s')
logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")

class student1:

    def __init__(self):
        self.student_name = "sahil"

    def student(self):
        try:
            logging.info(f'The name of the student is {self.student_name}')
        except Exception as e:
            logging.info(e)

        print(self.student_name)

st1 = student1()
st1.student()

class student2(student1):

    def __init__(self):
        self.student_name = 'aaru'

    def student(self):
        try:
            logging.info(f'The name of the student is {self.student_name}')
        except Exception as e:
            logging.error(e)

st2 = student2()
# we are trying to overide student function of parent class by student function of student class
st2.student()