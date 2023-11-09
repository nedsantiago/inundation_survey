from csv import DictReader
from re import search
from os.path import isfile

class DataRetriever():
    """This object retrieves a list of dictionaries from a database file. This class supports 
    .db and .csv files"""

    def __init__(self, path_to_database:str):
        """The initialization must include the path to the settings. On initialization, the class
        will validate the provided paths"""

        # check the file extension (sql database or csv)
        self._file_extension = search("[^.\n]{1,}$", path_to_database).group(0)
        self._path_to_database = path_to_database
        
        # initialize a None value to the result
        self._raw_data = None

        # check if the file exists
        assert isfile(self._path_to_database), f"File Does Not Exist.\nFile Name: {self._path_to_database}"
        # check if the file extension is supported (.csv, .db)
        assert self._file_extension in ["csv", "db"], f"Unexpected File Extension: {self._file_extension}"

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
            raise(AssertionError(f"Unexpected file extension {self._file_extension}"))
        
        # return the result
        return self._raw_data

    # process for reading sql database
    def _read_sql_db(self, path, sql_cmd):
        """This is the method for reading sql database file into a list dictionary
        for later processing"""

        # not yet implemented
        raise(AssertionError("Not yet implemented"))

    # process for reading csv database
    def _read_csv(self, path):
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
        assert type(self._data) is list, f"raw data must be a list, but data is {type(self._data)}"
        for row in self._data:
            assert type(row) is dict, "raw data rows must be dictionaries"
        
    def get_context(self):
        # apply the processor into each row 
        # (change the values based on whats defined in processor)
        for row in self._data:
            self._result.append(self._processor(row))
        
        # return the result
        return self._result