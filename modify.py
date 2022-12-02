# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:28:01 2022
@author: Crystal
"""
import sqlite3

connection = sqlite3.connect('shopping-cart.db')

cursor = connection.cursor()

query =("ALTER TABLE shopping-cart RENAME TO myseventeen")

cursor.execute(query)

connection.commit()
connection.close()