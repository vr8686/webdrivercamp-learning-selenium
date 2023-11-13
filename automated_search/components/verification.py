from automated_search.components.search_results_page import SearchResults
mismatches = []

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
                mismatches.append(mismatch)
        else:
            print(f"'{key}' is missing")


def verification_report():
    print(f'{'#' * 10} VERIFICATION REPORT {'#' * 10}')
    if not mismatches:
        print(f'No mismatches have been found')
    else:
        print(mismatches)


def verify_title_contains(title_text, keyword: str):
    print(f'Checking if title text contains word \"{keyword}\"...')
    if keyword in title_text.lower():
        print(f'Success. The title contains \"{keyword}\".')
    else:
        mismatch = f'Mismatch. The title DOES NOT contain \"{keyword}\"'
        print(mismatch)
        mismatches.append(mismatch)