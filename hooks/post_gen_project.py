import configparser

def update_pylintrc(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    
    config['FORMAT']['indent-string'] = "'    '"  # conform to black
    config['FORMAT']['max-line-length'] = '120'
    
    with open(file_path, 'w') as configfile:
        config.write(configfile)

update_pylintrc('./.pylintrc')
