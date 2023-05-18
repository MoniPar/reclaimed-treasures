// Gets the Stripe public key and secret from the template
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
// Sets up Stripe using the public key
var stripe = Stripe(stripe_public_key);
// Creates an instance of Stripe elements
var elements = stripe.elements();
// Creates and mounts the card element
var card = elements.create('card', { style: style });
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
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
card.mount('#card-element');