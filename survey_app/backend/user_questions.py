from csv import DictReader
from re import sub
from backend.data_managers import DataRetriever, HtmlContextCreator

def generate_questions(row):
    # list of dictionariies that may replace the options
    list_entries = []

    # iterate over a comma seperated list in options column
    for value in row["options"].split(","):
        # if there is a value in the options
        if value:
            # create the id/name (radio only uses this as id)
            # by appending a lower-cased, underscored "value" to the "form_name"
            id = row["form_name"] + "_" + sub(" ","_",value.lower())
            list_entries.append({"id":id, "value":value})
        # else it is assumed not to have any options
        else:
            id = row["form_name"]
            list_entries.append({"id":id, "value":""})
    
    # create stuff
    row["options"] = list_entries

    return row

def create_questions_context():
    """This method will take the questions setting file from the static backend directory"""
    path_user_questions = r"survey_app\backend\static\backend\questions_inundation_survey.csv"
    
    raw_questions_data = DataRetriever(path_to_database=path_user_questions).get_raw_data()

    questions_data = HtmlContextCreator(
        raw_data=raw_questions_data, 
        per_row_processor=generate_questions
        ).get_context()

    return questions_data

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