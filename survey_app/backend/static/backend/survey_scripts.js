// Attempting to create validity checker base class
class numberValidityChecker {
    /*This class is a validity checker. It serves as a base class
    for other validity checkers. Must be instantiated with upper
    and lower limits. By default, this class will take
    a string of letters, check if it is numeric then compare it
    against a specified upper and lower limit*/

    // constructor of properties
    constructor(lowerLimit, upperLimit) {
        this.lowerLimit = lowerLimit;
        this.upperLimit = upperLimit;
    }

    // Checker for whether the number is numeric (no alphabet
    // or could be float)
    isNumeric(str){
        // check if input was a string
        if (typeof str != "string"){
            // return false because only strings are considered
            return false;
        }
        // return true if not None and is a float
        return !isNaN(str) && !isNaN(parseFloat(str))
    }

    // The main validity checker function
    isValid(id) {
        /*This function takes the id label, gets the value in the
        element, then runs the validity check through that value.*/

        // get the element
        let element = document.getElementById(id)
        
        // check if element exists
        if (!element) {
            console.error(`ValidityCheckeer: Element with id ${id} not found.`)
            return false
        }

        // get the value in the element
        let value = element.value

        // if the string is NOT a numeric
        if (!(this.isNumeric(value))) {
            console.log(`ValidityChecker: string value in Element, ${id}, is not numeric`)
            // return false
            return false
        }

        console.log(`ValidityChecker: string with value ${value} is numeric`)

        // check if the value should between 0 and 180
        if ((value <= this.upperLimit) && (value >= this.lowerLimit)){
            // passes: then return True
            console.log(`ValidityChecker,${id}: ${value} is between ${this.lowerLimit} and ${this.upperLimit}`)
            return true;
        }
        // else
        else{
            // fails: longitude exceeded the limits 
            console.log(`ValidityChecker,${id}: string value failed, ${value} is NOT between ${this.lowerLimit} and ${this.upperLimit}`)
            return false;
        }
    }
}

function checkAll(event){
    /*This function summarizes all the client-side form checks*/

    // prevent form submission
    event.preventDefault();

    var isValid = true;
    let message = '<strong>Hold On!</strong>, please review the following:<br><ul>';

    // check logitude validity
    let long_valitidy = new numberValidityChecker(0, 180);
    // if longitude is not valid
    if (!(long_valitidy.isValid("id_long"))) {
        // flag as invalid
        isValid = false
        // modify the message
        message = message.concat("<li>Longitude</li>")
    }

    let lat_validity = new numberValidityChecker(0,90);
    if (!(lat_validity.isValid("id_lat"))) {
        // flag as invalid
        isValid = false
        // modify the message
        message = message.concat("<li>Latitutde</li>")
    }
    
    let age_validity = new numberValidityChecker(0,125);
    if (!(age_validity.isValid("id_respondent_age"))) {
        // flag as invalid
        isValid = false
        // modify the message
        message = message.concat("<li>Respondent Age</li>")
    }

    // close the unordered list in the message
    message = message.concat("</ul>")

    console.log(`Resulting Validity of all items is: ${isValid}`)
    
    // if all are valid (flag remains true)
    if (isValid) {
        console.log("Validity check passed, submitting form..")
        document.getElementById("survey-form-view").submit();
    }
    // else, invalid result
    else {
        // show the error alert
        console.log("Validity check failed, displaying error mesage..")
        test_id = "id_long"
        showAlert(message, "warning")
    }
}

// trigger for Bootstrap Alert
function showAlert(message, alertType) {
    /*This function creates the Boot Strap Alert*/

    // create alert element
    var alertElement = document.createElement('div');
    alertElement.classList.add('alert', 'alert-' + alertType, 'alert-dismissable', 'fade', 'show');
    if (alertElement) {
        console.log(`Successfully created alertElement with claslist add with innerHTML: ${alertElement.innerHTML}`)
    }

    // add close button and message
    alertElement.innerHTML = `
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
        </button>
        ${message}
    `
    if (alertElement) {
        console.log(`Successfully changed innerHTML: ${alertElement.innerHTML}`)
    }

    // append the alert to container in html
    document.getElementById('alert-container').appendChild(alertElement);

    // close after some time
    setTimeout(function () {
        alertElement.remove();
    }, 10000)
}

// when window loads, run the userlocation function
window.onload = getUserLocation

// record user's longitude and latitude
function getUserLocation() {
    /*This function records the user's location and places the recorded
    values as default longitude and latitude.*/

    navigator.geolocation.getCurrentPosition(defaultLocation)

    function defaultLocation(loc) {
        lat = loc.coords.latitude
        long = loc.coords.longitude

        document.getElementById("id_lat").value = lat;
        document.getElementById("id_long").value = long;
    }


}