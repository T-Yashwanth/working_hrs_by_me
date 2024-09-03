from working_hrs_by_me.calculator import Calculator
from working_hrs_by_me import logger
from openpyxl import Workbook
import pandas as pd

class WritingExcel:
    def DataFrameToExcel(self, data):
        try:
            logger.info(">>>>> writing the data to the excel <<<<<")    
            data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%Y-%m-%d')
            data.to_excel('output.xlsx')
            logger.info(">>>>> Completed writing to Excel <<<<<")
        except Exception as e:
            logger.exception(e)
            raise e