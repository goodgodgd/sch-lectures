
data = {'name': ['tom', 'lee'],
        'age': [3, 4],
        'gender': ['male', 'female'],
        'country': ['usa', 'china']}
newdata = {'name': 'jane', 'age': 6, 'gender': 'female'}
print(newdata)
try:
    assert 'country' in newdata, "'country' is not in newdata"
except AssertionError as ae:
    print(ae)
