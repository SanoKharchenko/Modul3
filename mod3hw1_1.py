calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    str_ = (len(string), string.upper(), string.lower())
    return str_


def is_contains(string, list_to_search):
    count_calls()
    str_lower = string.lower()
    for i in list_to_search:
        if str_lower in i.lower():
            return True
    return False

print(string_info("Capibara"))
print(string_info("Armageddon"))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
