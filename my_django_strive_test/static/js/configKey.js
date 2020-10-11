var stripe
fetch("/config/")
    .then(result => result.json())
    .then(data => stripe = Stripe(data.publicKey))