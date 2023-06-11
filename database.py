#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db/chinook.db')
session_db = sessionmaker()
session_db.configure(bind=engine)