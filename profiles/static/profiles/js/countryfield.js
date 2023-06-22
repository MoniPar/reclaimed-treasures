// Gets the value of the country field and stores it in a variable
let countrySelected = $('#id_default_country').val();
// First option = empty string so can be used as boolean
if(!countrySelected) {
    $('#id_default_country').css('font-style', 'italic');
}

// Captures change event
$('#id_default_country').change(function () {
    // gets value everytime box changes
    countrySelected = $(this).val();
    // determines the proper colour
    if(!countrySelected) {
        // grey if it is not selected
        $(this).css('font-style', 'italic');
    } else {
        // black if it is
        $(this).css('font-style', 'normal');
    }
});