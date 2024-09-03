from working_hrs_by_me.config.config_loader import loader
from working_hrs_by_me.config.excel_writer import WritingExcel
from working_hrs_by_me.calculator import Calculator

from pathlib import Path
from working_hrs_by_me import logger
import os

filename = "config.yaml"

if __name__ == "__main__":
    try:
        logger.info("********************************************")
        Cal = Calculator()
        DataFrame = Cal.df_creater(filename)

        excel = WritingExcel()
        excel.DataFrameToExcel(DataFrame)
        logger.info("********************************************\n\n\n\n")
    except Exception as e:
        logger.exception(e)
        raise e