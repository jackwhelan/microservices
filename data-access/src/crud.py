"""
Module to house the functions which cater for CRUD operations.
"""
from flask import Request

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
        response = db_adapter.find_by_oid(database, collection, request.args.get('id'))
    else:
        print('No oid passed with request')
        response = db_adapter.find_by_oid(database, collection)
    return response

def update():
    """
    Update/PATCH functionality for database interactions.
    """

def delete():
    """
    Delete/DELETE functionality for database interactions.
    """
