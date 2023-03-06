def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"fistname": "Facundo", "lastname": "García"}

    super_list = [
        {"fistname": "Facundo", "lastname": "García"},
        {"fistname": "Miguel", "lastname": "Torres"},
        {"fistname": "Pepe", "lastname": "Rodelo"},
        {"fistname": "Tatiana", "lastname": "Rodriguez"},
        {"fistname": "Jose", "lastname": "García"},
    ]

    super_dic = {
        "natural_nums": [1, 2, 3, 4, 5, 6],
        "integer_nums": [-2, -1, 0, 1, 2, 3, 4, 5],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dic.items():
        print(key, "-", value)


if __name__ == "__main__":
    run()