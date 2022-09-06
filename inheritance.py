# Inheritance Example
import logging
logging.basicConfig(filename='inheritance.log', level=logging.DEBUG, format= '%(asctime)s %(name)s %(levelname)s %(message)s')

class student_details:

    def student_name(self):
        """ Function takes student name """
        try:
            self.student1 = input(" please enter student name")
            logging.info('Student name is {}'.format(self.student1))
        except Exception as e:
            logging.info(e)


class internship(student_details):

    def student_email(self):
         """This function will take student email id"""
         try:
             st_email = input(" please enter email id")
             logging.info('Email id for {} is {}'.format(self.student1, st_email))
         except Exception as e:
             logging.info(e)


i = internship()
i.student_name()
i.student_email()