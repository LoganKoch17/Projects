def get_personal_data() -> dict:
    """
    :return: Returns a dictionary of personal information.
    """
    personal_data = {"name": "Jim", "a_role": "teacher"}
    return personal_data


def main() -> int:
    default_dict = dict()
    print(default_dict)
    initalized_dict =  dict([('name','Jim'), ('a_role','joker')])
    print(initalized_dict)
    simple_init_dict = dict(name='Jim', a_role='teacher')
    print(simple_init_dict)
    simple_init_dict['a_role'] = 'joker'
    print(simple_init_dict)
    my_comprehension = {x: x**2 for x in range(5)}
    print(my_comprehension)

    s = "little,".translate({ord(i)})


    return 0

if __name__ == '__main__':
    main()