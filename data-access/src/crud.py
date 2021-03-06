"""
Module to house the functions which cater for CRUD operations.
"""
from flask import Request

from src.etc.exceptions import DatabaseException
from src.adapters.database import DatabaseAdapter

def create(db_adapter: DatabaseAdapter, database: str, collection: str, request: Request):
    """
    Create/POST functionality for database interactions.
    """
    db_adapter.connect(database)
    response = db_adapter.insert(database, collection, request.get_json())
    return response

def read(db_adapter: DatabaseAdapter, database: str, collection: str, request: Request):
    """
    Read/GET functionality for database interactions.
    """
    db_adapter.connect(database)
    if request.args.get('oid') is not None:
        response = db_adapter.find_by_oid(database, collection, request.args.get('oid'))
    else:
        response = db_adapter.find_by_oid(database, collection)
    return response

def update(db_adapter: DatabaseAdapter, database: str, collection: str, request: Request):
    """
    Update/PATCH functionality for database interactions.
    """
    db_adapter.connect(database)
    if request.args.get('oid') is not None:
        response = db_adapter.update(database, collection, request.args.get('oid'), request.get_json())
    else:
        raise DatabaseException('Can not target document, Please pass a valid OID as a request arg.')
    return response

def delete(db_adapter: DatabaseAdapter, database: str, collection: str, request: Request):
    """
    Delete/DELETE functionality for database interactions.
    """
    db_adapter.connect(database)
    if request.args.get('oid') is not None:
        response = db_adapter.delete(database, collection, request.args.get('oid'))
    else:
        raise DatabaseException('Can not target document, Please pass a valid OID as a request arg.')
    return response
