import json

def cargar_datos():
    try:
        with open('inventario.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {'Objetos Comunes': [], 'Poké Balls': [], 'Objetos Clave': [], 'Bayas': [], 'MT/MO': []}
    
def guardar_datos(datos):
    with open('inventario.json', 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def guardar_item(datos, categoria):

    for i in categoria:
        print(f'{i}: {categoria[i]}')
    opcion = int(input('\nque quieres agregar: '))
    elemento = categoria[opcion]

    print('Guardar')
    nombre = input('> nombre: ')
    cantidad = int(input('> cantidad: '))
    efecto = input('> efecto: ')
    descripcion = input('> descripcion: ')

    
    nuevo_elemento = {
        'nombre': nombre,
        'cantidad': cantidad,
        'efecto': efecto,
        'descripcion': descripcion
    }

    if opcion:
        if opcion in categoria:
            datos[elemento].append(nuevo_elemento)
            guardar_datos(datos)
            print(f'se guardo con exito en {categoria[opcion]}')
        else:
            print('> ingrese una opcion valida')
    else:
        print('> la opcion no puede estar vacia')

def mostrar_items(datos, categoria):
    for i in categoria:
        print(f'{i}: {categoria[i]}')
                
    opcion = int(input('\n¿que categoria quieres ver?: '))
    elemento = categoria[opcion]
    
    print(f'\n======== {categoria[opcion]} ========')
    if opcion:
        if opcion in categoria:
            if datos[elemento]:
                for item in datos[elemento]:
                    print(f"-> nombre: {item['nombre']} \n - cantidad: {item['cantidad']} \n - descripcion: {item['descripcion']}")
            else:
                print('> esta categoria esta vacia')   
        else:
            print('> opcion invalida seleccione una opcion valida')        



def menu():
    datos = cargar_datos()
    categoria = {
        1: 'Objetos Comunes',
        2: 'Poké Balls',
        3: 'Objetos Clave',
        4: 'Bayas',
        5: 'MT/MO'
    }
    while True:
        print('\n========= MENU =========')
        print('1.Guardar item')
        print('2.mostrar inventario')
        print('3.salir')


        try:
            opcion = int(input('\ningresa la opcion: '))

            if opcion == 1:
                guardar_item(datos, categoria)

            elif opcion == 2:
                mostrar_items(datos, categoria)

            elif opcion == 3:
                print('cerrando...')
                break

        except ValueError:
            print('\nopcion invalida vuelve a intentarlo solo acepta numeros')

if __name__ == '__main__':
    menu()