def init_columns(col_names):
    """
    col_names: list of column titles (string) e.g.=['name', 'age']
    return: empty database e.g.={'name': [], 'age': []}
    """
    pass


def append(data, newdata):
    """
    data: database object (dict of lists) e.g.={'name': ['tom', 'lee'], 'age': [3, 4]}
    newdata: new data to be appended (dict) e.g.={'name': 'kim', 'age': 5}
    return: appended database e.g.={'name': ['tom', 'lee', 'kim'], 'age': [3, 4, 5]}
    [Note] if one of keys of 'newdata' is NOT in 'data', print WARNING message
    e.g. newdata={'name': 'kim', 'gender': 'male'}
        -> print("'gender' is NOT in this database")
    [Note] if 'newdata' does NOT have all keys in 'data', raise error using assert
    e.g. newdata={'name': 'kim'}
        assert 'age' in newdata, "'age' is NOT in newdata"
    """
    pass


def remove_by_name(data, names):
    """
    data: database object (dict of lists) e.g.={'name': ['tom', 'lee', 'kim'], 'age': [3, 4, 5]}
    names: list of names e.g.=['kim', 'tom']
    return: reduced database e.g.={'name': ['lee'], 'age': [4]}
    """
    pass


def query_by_name(data, names):
    """
    data: database object (dict of lists) e.g.={'name': ['tom', 'lee', 'kim'], 'age': [3, 4, 5]}
    names: list of names e.g.=['kim', 'tom']
    return: extracted database e.g.={'name': ['kim', 'tom'], 'age': [5, 3]}
    """
    pass


def query_by_age(data, age_min, age_max):
    """
    extract database of which age_min <= age < age_max
    data: database object (dict of lists) e.g.={'name': ['tom', 'lee', 'kim'], 'age': [3, 4, 5]}
    age_min: minimum age e.g.=2
    age_max: maximum age e.g.=5
    return: extracted database e.g.={'name': ['tom', 'lee'], 'age': [3, 4]}
    """
    pass


def merge(data, other):
    """
    data: database object (dict of lists) e.g.={'name': ['tom', 'kim'], 'age': [3, 5]}
    other: database object (dict of lists) e.g.={'name': ['lee'], 'age': [4]}
    return: merged database e.g.={'name': ['tom', 'kim', 'lee'], 'age': [3, 5, 4]}
    [Note] if 'other' has the same names with 'data', ignore the duplicated data
    e.g. data={'name': ['tom', 'kim'], 'age': [3, 5]}
        other={'name': ['lee', 'kim'], 'age': [4, 6]}
        -> {'name': ['tom', 'kim', 'lee'], 'age': [3, 5, 4]}
    """
    pass


def print_data(data):
    """
    data: database object (dict of lists) e.g.={'name': ['tom', 'kim'], 'age': [3, 5]}
    print database vertically
    e.g.
    name    age
    ----    ---
    tom     3
    kim     5
    """
    pass
