from re import sub
from backend.data_managers import DataRetriever, HtmlContextCreator

def generate_id_labels_options(row):
    # list of dictionariies that may replace the options
    list_entries = []

    # iterate over a comma seperated list in options column
    for value in row["options"].split(","):
        # if there is a value in the options
        if value:
            # create the id/name (radio only uses this as id)
            # by appending a lower-cased, underscored "value" to the "db_name"
            id = row["db_name"] + "_" + sub(" ","_",value.lower())
            list_entries.append({"id":id, "value":value})
        # else it is assumed not to have any options
        else:
            id = row["db_name"]
            list_entries.append({"id":id, "value":""})
    
    # create stuff
    row["options"] = list_entries

    return row

def generate_id_labels_repeat_labels(row):

    # list of dictionariies that may replace the storm_name
    list_entries = []

    # iterate over a comma seperated list in storm_name column
    for value in row["storm_name"].split(","):
        # create an id name based on the value
        id = sub(" ","_",value.lower())
        # create the dictionary
        list_entries.append({"id":id, "value":value})

    
    # create stuff
    row["storm_name"] = list_entries

    return row

def create_questions_context():
    """This method will take the questions setting file from the static backend directory"""
    path_user_questions = r"survey_website\survey_app\backend\static\backend\questions_inundation_survey.csv"
    
    raw_questions_data = DataRetriever(
        path_to_database=path_user_questions
        ).get_raw_data()

    questions_data = HtmlContextCreator(
        raw_data=raw_questions_data, 
        per_row_processor=generate_id_labels_options
        ).get_context()

    return questions_data

def create_questions_repeat_labels_context():
    """This method will create a context for the repeating questiosn (e.g. description_subject: "Storm Name", 
    list_subject: ["Storm Event 1", "Storm Event 2", "Storm Event 3"]). To explain, sometimes the same question
    depending on the situation. For example, What is the flood depth? can be asked again depending on the storm
    in question. This method will list the data to be iterated"""

    # declare the path to the iterable labels file
    path_repeat_labels = r"survey_website\survey_app\backend\static\backend\questions_repeat_labels.csv"

    # open using the DataRetriever
    raw_questions_repeat_labels = DataRetriever(
        path_to_database=path_repeat_labels
        ).get_raw_data()
    
    print(f"raw_questions_repeat_labels: {raw_questions_repeat_labels}")

    repeat_labels_data = HtmlContextCreator(
        raw_data=raw_questions_repeat_labels, 
        per_row_processor=generate_id_labels_repeat_labels
        ).get_context()
    
    print(f"adjusted_repeat_labels: {repeat_labels_data}")

    return repeat_labels_data