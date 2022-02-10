import logging

# Create a custom logger
logger = logging.getLogger(__name__)
minlog = logger.setLevel(logging.DEBUG)
# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('logs_file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

def info_log(class_name, function_name, message):
    logger.name = class_name
    logger.info(f'in {function_name} function: {message}')

def debug_log(class_name,function_name, message):
    logger.name = class_name
    logger.debug(f'in {function_name} function: {message}')

def warning_log(class_name, function_name, message):
    logger.name = class_name
    logger.warning(f'in {function_name} function: {message}')

def error_log(class_name, function_name, message):
    logger.name = class_name
    logger.error(f'in {function_name} function: {message}')