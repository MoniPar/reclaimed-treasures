/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Gets the Stripe public key and secret from the template
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
// Sets up Stripe using the public key
var stripe = Stripe(stripePublicKey);
// Creates an instance of Stripe elements
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            fontStyle: 'italic'
        }
    },
    invalid: {
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
// Creates and mounts the card element
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handles validation errors on card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fa-solid fa-xmark" aria-hidden="true"></i>
            </span>
            <span>${event.error.message}</span>`;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handles form submission
var form = document.getElementById('payment-form');
form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    // Disables the card element and the submit button
    card.update({ 'disabled': true});
    $('#submit-btn').attr('disabled', true);
    // Fades out the form and triggers the loading overlay
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    // Gets the boolean value of the checkbox
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';
    // Posts the data to the view, waits for a response with the done method
    $.post(url, postData).done(function () {
        // Calls the confirm card payment method
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.eircode.value),
                    state: $.trim(form.county.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                <span class="icon" role="alert">
                    <i class="fa-solid fa-xmark" aria-hidden="true"></i>
                </span>
                <span>${result.error.message}</span>`;
                // Displays error
                $(errorDiv).html(html);
                // Shows the form and hides the overlay 
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                // Enables the card element and the submit button
                card.update({ 'disabled': false});
                $('#submit-btn').attr('disabled', false);
            } else {
                // Submits form if status comes back as succeeded
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit()
                }
            }
        });
    }).fail(function () {
        // just reloads the page, the error will be in django messages
        location.reload();
    })
});
