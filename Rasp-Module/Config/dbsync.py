#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:02:29 2020

@author: setup
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:30:13 2020

@author: Pedro Salamoni
"""

import dbmanager as dbm

class DBsync():
    
    def __init__(self):
        
        self._ldb = dbm.LocalDatabase()
        self._fdb = dbm.ForeignDatabase()
        
    def syncDB(self):
        
        data = self._ldb.get_data()
        
        if data:
            
            for i in data:
                if self._fdb.insert_data(data[1],data[2],data[3],data[4],data[5]):
                    self._ldb.del_data(data[0])
                else:
                    print('Couldn\'t insert data in Foreign Database, please check internet connection and/or Database Setup')
                    return
                
        print('You\'re safe. Your data is up-to-date in Foreign Database!')

if __name__ == '__main__':
    
    dbs = DBsync()
    
    dbs.syncDB()