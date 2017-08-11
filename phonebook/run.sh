#!/bin/bash
cd phonebook
gunicorn phonebook.wsgi
