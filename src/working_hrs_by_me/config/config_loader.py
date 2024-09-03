from working_hrs_by_me import logger
import yaml, os


class loader:

    def yaml_load(self, file_name):
        try:
            # Get the directory of the current script
            base_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', '..', '..'))
            #constructing the full path
            file_path = os.path.join(base_directory, "data", file_name)
            logger.info(">>>>> Loading the Yaml file <<<<<")
            with open(file_path, 'r') as file:
                config = yaml.safe_load(file)
            logger.info(">>>>> Loading Completed <<<<<")
            return config
        
        except Exception as e:
            logger.exception(e)
            raise e