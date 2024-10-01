first = {"first key": "TFC LNTU",
         "Second key": 17,
         "Trird key": {"One": 21,
                       "Two": 'Denys',
                       "three": True,
                       "four": False,
                       "five": (1, 2, 3, 4, 5)},
         "Fourh key": "Stohodiuk"}

print(first)

second_dict = {}

for keys, checks in first.items():
    if type(checks) == dict:

        for keys1, checks1 in checks.items():
            second_dict[keys1] = type(checks1)

    else:
        second_dict[keys] = type(checks)

print(second_dict)
