# Understanding Relational Databases
# What is SQL?
# sqlite3 – Embedded Relational Database
# https://www.geeksforgeeks.org/python-sqlite/
# https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3

# https://www.youtube.com/watch?v=pd-0G0MigUA
# What is a relational database?
# What is SQL?
# What are the pros and cons of SQL?
# What is a query?
# How to start working with SQLite in Python?
# How to create a connection to a database?
# How to close a connection to a database?
# What is a cursor object in sqlite3?   #to excute a command
# How to execute a SQL statement using sqlite3? #c.execute
# How to commit changes to a database? #conn.commit

# sqlite3 cheatsheet for Python 3
# https://www.tomordonez.com/sqlite3-cheatsheet/
# https://www.alanwsmith.com/posts/python-sqlite3-cheat-sheet-examples--20eo2xoyornp


# Create a program that manages the work with SQLite databases using user input. 
# The program must be able to: 
#   - create connections to databases, 
#   - close the connections, and 
#   - execute a given SQL statement.

# To manage all the connections
#   - create a dict called connections, 
#   - store the 'filenames' of the databases as keys
#   - store the 'connection objects' as the values
#   - remove the dictionary item (key:value), everytime the connection is closed

# create a command list that prints out all avaliable commands

# 1. help 
#       returns list of commands

# 2. connect [database] 
#       creates a connection to [database]
#           if [database] exists, 
#           return msg
#
#           if error, 
#           return error
#
#           if successful, 
#           return msg 
#           add connection to dict
#
# 3. close [database]
#       close a connection to [database]
#           if connection not in [database]
#           return msg
#
#           if error, 
#           return error
#
#           if successful, 
#           return msg 
#           remove connection to dict           
#
# 3. execute [database] 'SQL statement'
#       execute a connection to [database]
#       create cursor
#       execute a command
#       commit
#           if connection not in [database]
#           return msg
#
#           if error, 
#           return error
#
#           if successful, 
#           return msg 
#
# 4. show 
#       print list of open database connection
#           if no connection 
#           return msg
#
# 5. exit 
#       close all connection
#       exit
#    
#
# try:
#   program
#
# except:
#   return msg
#
#

import sqlite3
import sys

def help():
    print('Available commands:',
           '- help',
           '- connect [database]',
           '- close [database]',
           '- execute [database] "[SQL statement]"',
           '- show',
           '- exit',
           sep='\n')

def connect(db_file, connections):
    try:
        conn = sqlite3.connect(db_file)
        if db_file in connections:
            print(f'Already connected to database "{db_file}".')
        else:
            print(f'Created connection to database "{db_file}".')
            connections.update({db_file: conn})
    except sqlite3.Error as e:
        print(e)

def close(db_file, connections):
    try:
        if db_file not in connections:
            print(f'Cannot close connection to "{db_file}". Not connected.')
        else:
            connections[db_file].close()
            print(f'Closed connection to database "{db_file}".')
            connections.pop(db_file)
    except sqlite3.Error as e:
        print(e)

def execute(db_file, query, connections):
    try:
        if db_file not in connections:
            print(f'Cannot execute SQL statement. Not connected to "{db_file}".')
        else:
            conn = connections[db_file]
            cur = conn.cursor()
            cur.execute(query)
            print('Executed SQL statement.')
    except sqlite3.Error as e:
        print(e)

def show(connections):
    try:
        if len(connections) == 0:
            print('No connections.')
        else:
         print([k for k, v in connections.items()])
    except:
        print('No connections.')

def exit(connections):
    for k, v in connections.items():
        v.close()
        print(f'Closed connection to database "{k}"')
    sys.exit(0)

# creating a handler list to manage the defined commands
def handler(commands):
    # at most there should be a max of 3 index (command, file, query)

    #define the command variabe 
    commands = commands[0:2]

    # if there is more than 3 index, create a new list of strings.
    ex_str = ' '.join(i for i in commands[2:]).split('"')

    #append it to the  command list.
    commands.append(ex_str[1])

    return commands

if __name__ == '__main__':
    connections = {}
    while True:
        commands = input('Enter command: ').split(' ')
        if len(commands) > 2:
            commands = handler(commands)
        if len(commands) == 1 and commands[0] == 'help':
            help()
        elif len(commands) == 2 and commands[0] == 'connect':
            connect(commands[1], connections)
        elif len(commands) == 2 and commands[0] == 'close':
            close(commands[1], connections)
        elif len(commands) == 3 and commands[0] == 'execute':
            execute(commands[1], commands[2], connections)
        elif len(commands) == 1 and commands[0] == 'show':
            show(connections)
        elif len(commands) == 1 and commands[0] == 'exit':
            exit(connections)
        else:
            print('Invalid command. Try "help" to see available commands.')

