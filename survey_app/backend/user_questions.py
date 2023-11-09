from csv import DictReader
from re import sub
from backend.data_managers import DataRetriever, HtmlContextCreator

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