import os
import click
from pathlib import Path

import inquirer

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def run():
    try:
        ccr()
    except KeyboardInterrupt:
        click.echo('User exit...')
    except Exception as e:
        pass

@click.group()
def ccr():
    ''' 
    This is a script to replace measurement comments by values from source file
    '''
    pass

@ccr.command()
def mando():
    '''
    This is the way!
    '''
    click.echo('''
    ⣿⣿⣿⣿⣿⣿⢸⣿⡇⠀⣿⣿⡇⣿⣿⡇⣼⣿⣿⣿⣿⣿⠀⠀⡇⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀
    ⠉⠉⣿⣿⠉⠉⢸⣿⡇⠀⣿⣿⡃⣿⣿⡇⣿⣿⡇⠀⣿⣿⠀⠀⡇⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀
    ⠀⠀⣿⣿⠀⠀⢸⣿⣧⣤⣿⣿⡇⣿⣿⡇⠻⣿⣷⣦⡀⠀⠀⠀⡇⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀
    ⠀⠀⣿⣿⠀⠀⢸⣿⡟⠛⣿⣿⡇⣿⣿⡇⠀⠈⠻⢿⣿⣦⠀⠀⡇⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀
    ⠀⠀⣿⣿⠀⠀⢸⣿⡇⠀⣿⣿⡇⣿⣿⡇⣿⣿⡇⠀⣿⣿⠀⠀⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀
    ⠀⠀⣿⣿⠀⠀⢸⣿⡇⠀⣿⣿⡇⣿⣿⡇⣿⣿⣷⣶⣿⣿⠀⠀⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀
    ⠀⠀⠛⠛⠀⠀⠘⠛⠃⠀⠛⠛⠃⠛⠛⠃⠈⠛⠛⠛⠛⠋⠀⠀⠿⢟⣛⣛⣛⣛⣛⣛⣛⣛⣛⣰⡄
    ⣿⡇⢴⣿⣿⣿⡆⠀⢸⣿⣿⣿⣿⣿⣿⠀⣿⡇⢸⣿⣿⣿⡇⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿⣷
    ⣿⡇⢸⣿⡀⠛⠃⠀⠀⠀⣿⡇⠀⣿⣿⠀⣿⡇⢸⣿⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⣶⣶⣶⣾⣿⣿
    ⣿⡇⠈⠻⢿⣶⡄⠀⠀⠀⣿⡇⠀⣿⣿⠿⣿⡇⢸⣿⠿⠿⠇⠀⠀⠀⢸⣿⣿⣿⣿⣿⡿⠛⠋⣹⡿
    ⣿⡇⢰⣶⡀⣿⡇⠀⠀⠀⣿⡇⠀⣿⣿⠀⣿⡇⢸⣿⣀⣀⡀⠀⠀⠀⢸⣿⣿⣿⣿⠋⠀⠀⢰⣿⡇
    ⠿⠇⠸⠿⠿⠿⠇⠀⠀⠀⠿⠇⠀⠿⠿⠀⠿⠇⠸⠿⠿⠿⠇⠀⠀⠀⣿⣿⣿⣿⠃⠀⠀⢠⣿⣿⡇
    ⣶⣶⡆⠀⣶⣶⠀⢰⣶⣶⠀⢰⣶⣶⡀⢲⣶⣦⠀⢰⣶⣶⠀⠀⠀⠀⣿⣿⣿⠃⠀⣠⣤⣿⣿⣿⠃
    ⢸⣿⣧⠀⣿⣿⡇⢸⣿⣿⠀⣿⣿⣿⡇⠈⣿⣿⡀⣼⣿⡏⠀⠀⠀⠀⣿⣿⡏⢀⣾⣿⣿⣿⣿⣿⠀
    ⢸⣿⣿⢸⣿⣿⡇⣼⣿⡇⢸⣿⡿⣿⣧⠀⢻⣿⣇⣿⣿⠁⠀⠀⠀⠀⣿⣿⠇⣼⣿⣿⣿⣿⣿⣿⠀
    ⠀⣿⣿⢸⣿⣿⣇⣿⣿⠇⢸⣿⡇⣿⣿⡀⠘⣿⣿⣿⡏⠀⠀⠀⠀⠀⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⠀
    ⠀⣿⣿⣿⣿⢿⣿⣿⣿⠀⣾⣿⠷⢿⣿⡇⠀⢻⣿⣿⠀⠀⠀⠀⠀⠀⣿⡿⣾⣿⣿⣿⣿⣿⠟⠁⠀
    ⠀⢸⣿⣿⡏⢸⣿⣿⡿⢰⣿⣿⠀⢸⣿⣷⠀⢸⣿⣿⠀⠀⠀⠀⠀⢀⣿⡇⣿⣿⣿⠟⠋⠀⠀⠀⠀
    ⠀⢸⣿⣿⡇⢸⣿⣿⡇⢸⣿⡇⠀⠀⣿⣿⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠻⡇⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

@ccr.command()
def start():
    ''' 
    Start the replacement
    '''

    source_files, csv_files = list_valid_files()
    
    click.echo('Select source\n - reads every line starting from 2nd line\n - takes measurement until first \';\'')
    click.echo('Selected file will be excluded from scan!')

    source = source_files[0]
    if len(source_files) > 1:
        answer = inquirer.prompt([inquirer.List('source', message='choose', choices=source_files)])
        source = answer['source']
    print_green(f'Source: {source}\n')

    with open(source) as s:
        next(s) # skip 1st line
        source_lines = s.readlines()
        s.close()
    source_lines_first_column = list(map(lambda line: str(line).split(';')[0], source_lines))
    
    for index, csv in enumerate(csv_files):
        c = open(csv, 'r+')
        csv_lines = c.readlines()
        if len(csv_lines) > 0:
            if not csv_lines[0].startswith(';'):
                print_warning(f'Skipped "{csv}" as no comment in first line indicated by starting with \';\'')
                continue
            print_green(f'{csv} [{csv_lines[0]} --> {source_lines_first_column[index]}]'.replace('\n', ''))
            csv_lines[0] = source_lines_first_column[index] + "\n"
            c.seek(0,0)
            c.writelines(csv_lines)
        c.close()


def list_valid_files():
    click.echo(f'CSV loading...\n')
    files = list(file for file in os.listdir() if os.path.isfile(file))

    source_files = list(filter(lambda file: file.endswith('.txt'), files))
    if len(source_files) == 0:
        print_error('No .txt source files could be found!')
        exit(1)
    
    csv_files = list(filter(lambda file: file.endswith('.csv'), files))
    if len(csv_files) == 0:
        print_error('No .csv source files could be found!')
        exit(1)
    csv_files.sort()

    return source_files, csv_files


def print_warning(string):
    click.echo(f'{bcolors.WARNING}{string}{bcolors.ENDC}')

def print_green(string):
    click.echo(f'{bcolors.OKGREEN}{string}{bcolors.ENDC}')

def print_error(string):
    click.echo(f'{bcolors.FAIL}{string}{bcolors.ENDC}')
