import logging
import os

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'polymorphism.log'), level=logging.INFO, format=logging_str,
                    filemode="a")

# import student class from variables module
from varaibles import student
st = student()


class internship:

    def __init__(self):
        self.name = 'sudh'

    def student_info(self):
        try:
            logging.info(f'internship student name is {self.name}')
        except Exception as e:
            logging.info(e)

int1 = internship()

def test(a):
    a.student_info()


test(int1)
test(st)

