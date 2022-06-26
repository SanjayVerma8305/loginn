keyid="rzp_test_neF5iC0Gdo9ISb"
keySecret="Eu64PUICXXgpboNDzL2vkaem"


import razorpay

client = razorpay.Client(auth=(keyid, keySecret))



data={
    'amount':100*100,
    'currency':'INR',
    'receipt':'code12',
    'notes':{
        'name':'sanjay',
        'Payment_for':'Angular'
    }
}

order=client.order.create(data=data)
print(order)

# {'id': 'order_JmDe5WBfovwajz', 'entity': 'order', 'amount': 10000, 'amount_paid': 0, 'amount_due': 10000, 'currency': 'INR', 'receipt': 'code12', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': {'name': 'sanjay', 'Payment_for': 'Angular'}, 'created_at': 1656267427}

data_dict={ 'razorpay_payment_id': "pay_JmDrHFZIEqibx9", 'razorpay_order_id': "order_JmDnaDODScSY3Z", 'razorpay_signature': "dd0d095ba84260247f833873a06d218519e18f5224c41c53fc39277fe166fd19"}

var=client.utility.verify_payment_signature(data_dict)
print(var)