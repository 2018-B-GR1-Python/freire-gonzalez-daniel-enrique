daniel = {
    'name': 'Daniel'
}

number_array = [1, 2]

try:
    daniel['las_name']
    number_array['1'] = 0
except (KeyError, TypeError) as error:  # for keys
    print(f'err {error}')
    print(f'Trace {error.__traceback__.tb_frame}')
    print(f'Line {error.__traceback__.tb_lineno}')




