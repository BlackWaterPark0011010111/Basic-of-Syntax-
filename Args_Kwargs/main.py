def create_plate(color, *args):
    print(f'Colour:  {color}' )
    print(f'Type:  {args}')

create_plate('black', 'oval', 'with print')

print(']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')

def create_plate(color, **kwargs):
    print(f'Colour:  {color}' )
    print(f'Type:  {kwargs}')

create_plate('black', shape = 'oval', pattern = 'with print')

print(']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')



def create_plate(color, *args, **kwargs):
    print(f'Colour:  {color}' )
    print(f'Type:  {kwargs}')
    for key, value in kwargs.items():
        print(f'{key} - {value}')
create_plate('black',  'oval',  'with print', address = '5th street', phone = '12345')