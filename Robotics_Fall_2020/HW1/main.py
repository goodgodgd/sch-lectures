import dbms


def main():
    columns = ['name', 'age', 'gender', 'country']
    data = dbms.init_columns(columns)
    data = dbms.append(data, {'name': 'tom', 'age': 3, 'gender': 'male', 'country': 'usa'})
    data = dbms.append(data, {'name': 'lee', 'age': 4, 'gender': 'female', 'country': 'china'})
    data = dbms.append(data, {'name': 'kim', 'age': 5, 'gender': 'male', 'country': 'korea'})
    try:
        data = dbms.append(data, {'name': 'jane', 'age': 6, 'gender': 'female'})
    except AssertionError as ae:
        print(ae)

    # data = {'name': ['tom', 'lee', 'kim'], 'age': [3, 4, 5], 'gender': ..., 'country': ...}
    dbms.print_data(data)

    # query_result = {'name': ['kim', 'tom'], 'age': [5, 3], 'gender': ..., 'country': ...}
    query_result = dbms.query_by_name(data, ['kim', 'tom'])
    dbms.print_data(query_result)

    # query_result = {'name': ['tom', 'lee'], 'age': [3, 4], 'gender': ..., 'country': ...}
    query_result = dbms.query_by_age(data, 2, 5)
    dbms.print_data(query_result)

    # merged_data = ['tom', 'lee', 'kim', 'jame'], 'age': [3, 4, 5, 6], 'gender': ..., 'country': ...}
    other = {'name': ['jane'], 'age': [6], 'gender': ['female'], 'country': ['uk']}
    merged_data = dbms.merge(data, other)
    dbms.print_data(merged_data)

    # reduced_data = ['kim', 'jame'], 'age': [5, 6], 'gender': ..., 'country': ...}
    reduced_data = dbms.remove_by_name(merged_data, ['tom', 'lee'])
    dbms.print_data(reduced_data)


if __name__ == "__main__":
    main()
