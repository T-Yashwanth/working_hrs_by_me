my_project/
│
├── src/
│   └── working_hrs_by_me/
│       ├── __init__.py   #wrote logging hear
│       ├── calculator.py
│       └── config
│            ├──__init__.py
│            ├──config_loader.py #has code
│            └──excel_writer.py
│
├── setup.py #has code
├── requirements.txt 
├── README.md
├──work_hr_me\ #python virtual env directory
└──data
    └── config.yaml   #contain data


step 1: 
    wrote yaml loader

Step 2: 
    have to write the excel_writer so that we have to fill the excel with all the dates, start time and end time, have to neglate the custome times and avoid the absent dates.
step 3: 
    have to write the caliculator logic for the data in excel and it should be written in the excel along with the total hours at the end.