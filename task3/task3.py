import json


def load_json(filepath):
    with open(filepath) as file:
        data = json.load(file)
    return data


def save_json(data):
    with open('report.json', 'w+') as file:
        json.dump(data, file, indent=2)
    return True


def make_report(filepath_one, filepath_two):
    data_tests = load_json(filepath_one)
    data_values = load_json(filepath_two)
    tests = data_tests['tests']
    qty_start = len(tests)
    for test in tests:
        if test.get('values'):
            for value in test.get('values'):
                tests.append(value)
        for index, value in enumerate(data_values['values']):
            if test['id'] == value['id']:
                test['value'] = value['value']
                data_values['values'].pop(index)
                break
    qty_end = len(tests)
    for i in range(0, qty_end - qty_start):
        tests.pop(qty_start)
    data = {'tests': tests}
    return data


if __name__ == '__main__':
    filepath_one = input()
    filepath_two = input()
    data = make_report(filepath_one, filepath_two)
    save_json(data)
