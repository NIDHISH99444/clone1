from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC38aded79d42ce30264556942167073e8"
auth_token = "9feaa90730412064b9936b27ee0660b9"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+919944429911",
    from_="+15402741542",
    body="you have messed up with a wrong person !!!! i will hack your accounts now !!! Just kidding :P Nidhish Singhal")