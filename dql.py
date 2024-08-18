def select_query(cursor, query):
    cursor.execute(query)
    results = cursor.fetchall()
    return results
