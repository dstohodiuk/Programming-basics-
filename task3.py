first_dict = {"first key": "TFC LNTU",
              "Second key": 17,
              "Trird key": {"First key": 21,
                            "Second key": 'Denys',
                            "Trird key": True,
                            "Fourh key": False,
                            "Fifth key": (1, 2, 3, 4, 5)},
              "Fourh key": "Stohodiuk"}

print(first_dict)

second_dict = {"first key": type("TFC LNTU"),
               "Second key": type(17),
               "Trird key": {"First key": type(21),
                             "Second key": type('Denys'),
                             "Trird key": type(True),
                             "Fourh key": type(False),
                             "Fifth key": type((1, 2, 3, 4, 5))},
               "Fourh key": type("Stohodiuk")}

print(second_dict)
