from csc131 import dictionaries
''''''

def main():
    print("Main")

def something_else():
    d = (dictionaries.get_personal_data())
    print(d)
    for key in sorted(d.keys()):
        print("%s: %s" % (key, d[key]))

if __name__ == '__main__':
    something_else()
    main()
