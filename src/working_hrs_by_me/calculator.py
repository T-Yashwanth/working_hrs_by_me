from working_hrs_by_me.config.config_loader import loader
from working_hrs_by_me import logger
from datetime import datetime, timedelta
import pandas as pd

class Calculator:
    def df_creater(self, file_name):
        try:
            # Load YAML data
            yaml_data = loader().yaml_load(file_name)
            start_date = yaml_data["start_date"]
            end_date = yaml_data["end_date"]
            self.schedule = yaml_data["schedule"]
            self.lunch_duration = timedelta(minutes=yaml_data.get("lunch_duration", 0))  # Lunch duration in minutes
            self.leaves = yaml_data.get("leaves", [])
            self.custom_hours = yaml_data.get("custom_hours", {})
                    
            # Create date range
            date_range = pd.date_range(start=start_date, end=end_date)
            
            logger.info(">>>>> Creating the Data Frame <<<<<")
            # Initialize DataFrame
            df = pd.DataFrame({
                "Date": date_range,
                "Day": date_range.day_name(),
                "Start Time": "",
                "End Time": "",
                "Total Time": ""
            })           
            # Apply get_times to each row
            df[['Start Time', 'End Time']] = df.apply(lambda row: pd.Series(self.get_times(row)), axis=1)        
            logger.info(">>>>> Calculating the Total Hours for each day <<<<<")
            # Calculate total time
            df['Total Time'] = df.apply(lambda row: self.calculate_total_time(row['Start Time'], row['End Time']), axis=1)
            # Remove default index
            logger.info(">>>>> Calculating the Total Hours <<<<<")
            Total_hours = df['Total Time'].sum()
            df = pd.concat([df, pd.DataFrame({'Total Time': [Total_hours]})], ignore_index=True)
            #df.set_index('Date', inplace=True)
            logger.info(df)
            return df
        
        except Exception as e:
            logger.exception(e)
            raise e

    def get_times(self, row):
        try:
            date_str = row['Date'].strftime('%Y-%m-%d')
            
            # Check if the date is a leave
            if date_str in self.leaves:
                logger.info(f">>>>> Leave on {date_str} <<<<<")
                return "12:00 AM", "12:00 AM"
            
            # Check for custom hours
            if self.custom_hours and date_str in self.custom_hours:
                custom = self.custom_hours[date_str]
                logger.info(f">>>>> Custom Hours on {date_str} start time {custom['start_time']} end time {custom['end_time']} <<<<<")
                return custom['start_time'], custom['end_time']
            
            # Use standard schedule
            day = row['Day'].lower()
            if day in self.schedule:
                return self.schedule[day]['start_time'], self.schedule[day]['end_time']
            else:
                logger.warning(f">>>>> Day not found in Shedule {day} <<<<<")           
                # Default times if day not found in schedule
                return "12:00 AM", "12:00 AM"
            
        except Exception as e:
            logger.exception(e)
            raise e

    def calculate_total_time(self, start_time_str, end_time_str):
        # Convert to datetime objects
        start_time = datetime.strptime(start_time_str, '%I:%M %p')
        end_time = datetime.strptime(end_time_str, '%I:%M %p')
        
        # Calculate the difference
        if end_time < start_time:
            # Handle cases where the end time is past midnight
            end_time += timedelta(days=1)
        
        total_hours = (end_time - start_time).seconds / 3600.0  # convert to hours
        
        # Subtract lunch duration if total hours exceed 6 hours
        if total_hours > 6.0:
            
            total_hours -= self.lunch_duration.seconds / 3600.0
        
        return float(f"{total_hours:.2f}")
