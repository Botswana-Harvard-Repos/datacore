from pymongo import MongoClient


def get_db_handle(db_name, username, password, host=None, port=None):
    """ Creates a db client to interact with the specified database.
        If host and port not specified uses defaults to connect to client.
        @param db_name: database name
        @param host: mongoDB server host (default: 127.0.0.1)
        @param port: mongoDB server port
        @param username: username for access authorisation
        @param password: password for access authorisation
    """
    connection_params = {'username': username, 'password': password}
    if host and port:
        connection_params.update({'host': host, 'port': port})
    client = MongoClient(**connection_params)
    db_handle = client[db_name]
    return db_handle, client
