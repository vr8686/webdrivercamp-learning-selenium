MISMATCHES = []


def compare_data(dict1, dict2):
    print(f'Comparing data')
    keys_to_compare = ['item1 - title', 'item2 - title', 'item1 - price', 'item2 - price']
    for key in keys_to_compare:
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                print(f"'{key}' has the same value on both pages: {dict1[key]}")
            else:
                mismatch = (f"'{key}' has different values: {dict1[key]} on Search Result Page and {dict2[key]} on "
                            f"the Item Page")
                print(mismatch)
                MISMATCHES.append(mismatch)
        else:
            print(f"'{key}' is missing")


def verification_report():
    print(f'{'#' * 10} VERIFICATION REPORT {'#' * 10}')
    if not MISMATCHES:
        print(f'No mismatches has been found')
    else:
        print(MISMATCHES)
