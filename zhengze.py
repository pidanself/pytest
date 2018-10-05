import re
def is_valid_email(addr):
    re_email=re.compile(r'^[a-zA-Z0-9.]+@[a-zA-Z0-9]+.com$')
    if re_email.match(addr):
        return True
    else:
        return False

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')