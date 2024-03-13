def generate_select_query_with_pkey(table_name, column_names):
    """
    Generate a select query with 'pkey' column and columns with their aliases prefixed with '_r' appended.
    
    Args:
    - table_name (str): Name of the table.
    - column_names (list of str): List of column names.
    
    Returns:
    - str: Generated SELECT query.
    """
    columns_with_aliases = [f"{col}, {col}_r" for col in column_names]
    select_query = f"SELECT pkey, {', '.join(columns_with_aliases)} FROM {table_name};"
    return select_query

def generate_select_queries(tables):
    """
    Generate select queries for multiple tables.
    
    Args:
    - tables (dict): Dictionary with table names as keys and list of column names as values.
    
    Returns:
    - dict: Dictionary with table names as keys and generated SELECT queries as values.
    """
    select_queries = {}
    for table_name, column_names in tables.items():
        select_query = generate_select_query_with_pkey(table_name, column_names)
        select_queries[table_name] = select_query
    return select_queries

# Example usage
tables = {
    "employee": ["emp_id", "emp_nm", "hire_dt", "salary"],
    "department": ["dept_id", "dept_nm", "manager_id"]
}

select_queries = generate_select_queries(tables)
for table_name, select_query in select_queries.items():
    print(f"Select query for table {table_name}:")
    print(select_query)
    print()
