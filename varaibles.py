import logging
import os

# logging.basicConfig(filename='method.log', level= logging.INFO, format=' %(asctime)s %(level)s %(message)s')
logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'variables.log'), level=logging.INFO, format=logging_str,
                    filemode="a")

class student:

    def __init__(self):
        self.name = "sahil"
        self._email = "sahil@gmail.com"
        self.__password = "sahil123"

    def student_info(self):
        """This function is getting student information using public, protected and private variables"""
        try:
            logging.info(f" Name of the student is {self.name}")
            logging.info(f" email of the student is {self._email}")
            logging.info(f" password is  {self._student__password}")
        except Exception as e:
            logging.info(e)

st = student()
st.student_info()




