# Multiple Inheritance Example
import logging
logging.basicConfig(filename='multiple_inheritance.log', level=logging.DEBUG, format= '%(asctime)s %(name)s %(levelname)s %(message)s')

class student_details:

    def student_name(self):
        """ Function takes student name """
        try:
            self.student1 = input(" please enter student name")
            logging.info('Student name is '.format(self.student1))
        except Exception as e:
            logging.info(e)


class internship():

    def student_email(self):
         """This function will take student email id"""
         try:
             self.st_email = input(" please enter email id")
             logging.info('Email id is {}'.format(self.st_email))
         except Exception as e:
             logging.info(e)

class job(student_details,internship):

    def job_application(self):
        """ Student who applied for job """
        try:
            logging.info(" student name is {} email id is {} ".format(self.student1, self.st_email))
        except Exception as e:
            logging.info(e)


j = job()
j.student_name()
j.student_email()
j.job_application()