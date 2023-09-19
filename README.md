# inundation_survey
for interviews about flood depths and durations during field works related to Hydrology

# General Details
Project Name:         Inundation Survey
Project Maintainer:   Ned Santiago
Project Start: 		    230919
Release Ver1.0.0:     -

## Objectives
### Version 1.0.0
Client
- [ ] Survey results can be stored locally
- [ ] Stored survey results can be sent at a later time
- [ ] Remembers details to reduce number of inputs of user

Server
- [ ] Checks validity of each form received
- [ ] Store received data into database

# Features
- Progressive Web App
- Record GPS coordinates

# Technologies:
- Bootstrap for website
- Django for server
- JSON

# Implementation Details
## Server
database{
	db_id			            INTEGER
	db_datetime	          REAL
	survey_id		          INTEGER
	typhoon			          TEXT
	subject_address		    TEXT
	depth			            REAL
	duration		          REAL
	image			            BINARY
	long			            REAL
	lat 			            REAL
	respondent_name		    TEXT
	respondent_age		    INTEGER
	respondent_residency	TEXT (employee or resident)
	surveyor_name		      TEXT
	survey_datetime		    TEXT
	project_name		      TEXT
	remarks			          TEXT
}
methods{
	check_validity()
}


## Client
database{
	survey_id		          INT
	typhoon			          STRING
	subject_address		    STRING
	depth			            FLOAT
	duration		          FLOAT
	image			            BINARY
	long			            FLOAT
	lat 			            FLOAT
	respondent_name		    STRING
	respondent_age		    INT
	respondent_residency	STRING (employee or resident)
	surveyor_name		      STRING
	survey_datetime		    STRING
	project_name		      STRING
	remarks			          STRING
}
methods{
	send_data()
	store_locally()
}
template{

auto records:
lat and long
survey datetime auto record
surveyor name auto record

subject address
respondent age
respondent name
respondent residency
project name remembers previous

typhoon name
flood depth
flood duration

image or picture

remarks

store button

at a dropdown menu,
update server button
}
