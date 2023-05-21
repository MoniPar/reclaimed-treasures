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
            color: '#aab7c4'
        }
    },
    invalid: {
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
// Creates and mounts the card element
var card = elements.create('card', { style: style });
card.mount('#card-element');

// Handles validation errors on card element
card.addEventListener('change', function(event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fa-solid fa-xmark" aria-hidden="true"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);

    } else {
        errorDiv.textContent = '';
    }
});

// Handles form submission
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(event) {
    event.preventDefault();
    // Disables the card element and the submit button
    card.update({'disabled': true});
    $('#submit-btn').attr('disabled', true);
    // Fade out the form and trigger the loading overlay
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    // Calls the confirm card payment method
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                    <i class="fa-solid fa-xmark" aria-hidden="true"></i>
                </span>
                <span>${result.error.message}</span>
            `;
            $(errorDiv).html(html);
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            // Enables the card element and the submit button
            card.update({ 'disabled': false });
            $('#submit-btn').attr('disabled', false);
        } else {
            // Submits form if status comes back as succeeded
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});