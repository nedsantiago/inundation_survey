from csv import DictReader
from re import sub, search
from os.path import isfile, exists

def create_questions_context():
    """This method will take the questions setting file from the static backend directory"""
    path_user_questions = r"survey_app\backend\static\backend\questions_inundation_survey.csv"
    
    # open the csv file as utf-8-sig file
    with open(path_user_questions, mode= 'r', encoding='utf-8-sig') as file:
        dictreader = DictReader(file)
        list_dict = []
        # initialize an id list, this may be useful for the server later on
        id_list = []
        # create a list of dictionaries
        # iterate over the csv file
        for row in dictreader:
            # create a list out of the data in options
            row["options"] = row["options"].split(",")
            list_entries = []
            # iterate over that sublist
            for value in row["options"]:
                # if there is a value in the options
                if value:
                    # create the id/name (radio only uses this as id)
                    # by appending a lower-cased, underscored "value" to the "form_name"
                    id = row["form_name"] + "_" + sub(" ","_",value.lower())
                    list_entries.append({"id":id, "value":value})
                    id_list.append(id)
                # else it is assumed not to have any options
                else:
                    id = row["form_name"]
                    list_entries.append({"id":id, "value":""})
                    id_list.append(id)
            # create new dictionary value for the id new id list
            row["options"] = list_entries
            # append the entire dictionary
            list_dict.append(row)

    # return the list of dictionaries
    return list_dict

class DataRetriever():
    """This object retrieves a list of dictionaries from a database file. This class supports 
    .db and .csv files"""

    def __init__(self, path_to_database:str):
        """The initialization must include the path to the settings. On initialization, the class
        will validate the provided paths"""

        # check the file extension (sql database or csv)
        self._file_extension = search("[^.\n]{1,}$", path_to_database)
        self._path_to_database = path_to_database
        
        # initialize a None value to the result
        self._raw_data = None

        # check if the file exists
        assert isfile(self._path_to_database), print(f"File Does Not Exist.\nFile Name: {self._path_to_database}")
        # check if the file extension is supported (.csv, .db)
        assert self._file_extension in ["csv", "db"], "Unexpected File Extension"

    def get_raw_data(self):
        """get_raw_data() is a method that requests the data from the database declared during initialization"""
        
        # if csv file
        if self._file_extension == "csv":
            self._raw_data = self._read_csv(self._path_to_database)
        # else if sql database
        elif self._file_extension == "db":
            self._raw_data = self._read_sql_db(self._path_to_database)
        # else it is not a supported file extension
        else:
            raise(AssertionError("Unexpected file extension"))
        
        # return the result
        return self._raw_data

    # process for reading sql database
    def _read_sql_db(path, sql_cmd):
        """This is the method for reading sql database file into a list dictionary
        for later processing"""

        # not yet implemented
        raise(AssertionError("Not yet implemented"))

    # process for reading csv database
    def _read_csv(path):
        """This is the method for reading csv files into a list dictionary for later
        processing"""

        # initialize raw settings list of dictionaries
        list_dict = []

        with open(path, mode='r', encoding='utf-8-sig') as file:
            # create the dictreader object
            dictreader = DictReader(file)

            # iterate over the csv file
            for row in dictreader:
                # copy the details in the dictreader into list of dictionaries
                # copying rows because copying the list itself may copy the pointers
                # instead of the values
                list_dict.append(row.copy())
            
        # return the list of dictionaries
        return list_dict

class HtmlContextCreator():
    """This class creates a new list of dictionaries for HTML contexts. It takes data
    from the DataRetriver as list of dictionaries and will return a list of dictionary
    upon request. This is mainly used to hold the different per-row processors."""
    
    def __init__(self, raw_data, per_row_processor):
        """Initialization checks data validity. It also stores the per-row processor"""

        self._processor = per_row_processor
        self._data = raw_data
        self._result = []

        assert callable(self._processor), "per-row processor needs to be a function"
        assert type(self._data) == "list", "raw data must be a list"
        for row in self._data:
            assert type(row) == "dict", "raw data rows must be dictionaries"
        
    def get_context(self):
        # apply the processor into each row 
        # (change the values based on whats defined in processor)
        for row in self._data:
            self._result.append(self._processor(row))
        
        # return the result
        return self._result

def create_settings_context():
    """This method will create a context for the settings (e.g. description_subject: "Storm Name", 
    list_subject: ["Storm Event 1", "Storm Event 2", "Storm Event 3"])"""

    # declare the path to the settings.csv file

    # open the csv file as utf-8-sig

    # read the file onto a dictreader object

    # iterate through the dictreader object

    # create a dictionary with parameters as key and a list of values as value
    
    # return the new list_dict

    pass