from csv import DictReader
from re import sub

def get_user_questions():
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
                if value is not "":
                    # create an id/name by adding form name and a lowercased underscored string
                    id = row["form_name"] + "_" + sub(" ","_",value.lower())
                    list_entries.append({"id":id, "value":value})
                    id_list.append(id)
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