import sys


def error_message_details(error,error_details:sys):
    _,_,exc_tb=error_details.exc.info()
    file_name=exc_tb.tb_frame.f_code.co_file

    error_message="error occured in python script name [{0}] line number [{1}] error massage [{2}]".format(
        file_name, exc_tb.tb_lineno,str(error)

    )

    return error_message


class CustomException(Exception):

    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_details=error_details)

    def __str__(self):
        return self.error_message

    
'''
if __name__=="__main__":
    logging.info("Logging has started")
    try:
        a=1/0
    except Exception as e:
        logging.info('Dicision by zero') 
        raise CustomException(e,sys)
'''