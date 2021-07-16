#program 1
import logging

def foo():
    logging.warning('entering foo function')
    print("inside foo")
    logging.warning('exiting foo function')
    logging.error('error foo')
    logging.critical('critical foo')
    
def bar():
    logging.basicConfig(level=logging.debug) #we have set the level after that it works from debug
    logging.debug('entering baz()')
    print('inside bar')

def baz():
    print('inside baz')


foo()
bar()
baz()


#program 2 
#if we want to display all worning msg to a different log file
import logging

def foo():
    logging.basicConfig(level=logging.DEBUG, filename='app.log' , filemode='w') #the whole logging msg will print in app.log file, this file will create automatically in current folder
    #logging.basicConfig(level=logging.DEBUG, filename='app.log' , filemode='w'  ,format='%(name)s-%(levelname)s-%(message)s')
    #logging.basicConfig(level=logging.DEBUG, filename='app.log' , filemode='w'  ,format='%(name)s-%(levelname)s-%(message)s',datefmt='%d-%m-%y %H:%M:%S')
    logging.warning('entering foo function')
    print("inside foo")
    logging.warning('exiting foo function')
    logging.error('error foo')
    logging.critical('critical foo')
    
def bar():
    logging.basicConfig(level=logging.debug) #we have set the level after that it works from debug
    logging.debug('entering baz()')
    print('inside bar')

def baz():
    logging.debug('entering baz')
    try:
        print('inside baz')
        raise Exception ('custom exception')
    except Exception as e:
        logging.error('Error!',exc_info=True) #exc_info , by default it will take all kind of exception


foo()
bar()
baz()

#program 3
#custom logger
import logging 

logger = logging.getLogger('my custom logger') #custom logger created, so it not show root i.e you can create seperate custom logger for each class / method
def foo():
    
    logger.warning('starting foo()')
    print('inside foo()')
    logger.warning('exiting foo()')

def baz():
    logging.debug('entering baz')
    try:
        print('inside baz')
        raise Exception ('custom exception')
    except Exception as e:
        logging.error('Error!',exc_info=True) #exc_info , by default it will take all kind of exception


foo()
baz()