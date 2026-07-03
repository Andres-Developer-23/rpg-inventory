import json
import os
import tempfile
import unittest
from unittest.mock import patch, mock_open

import inventario


class TestCargarDatos(unittest.TestCase):
    def setUp(self):
        self.categorias = {
            'Objetos Comunes', 'Pok\u00e9 Balls',
            'Objetos Clave', 'Bayas', 'MT/MO'
        }

    def test_cargar_datos_sin_archivo(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            original_dir = os.getcwd()
            os.chdir(tmpdir)
            try:
                datos = inventario.cargar_datos()
                self.assertIsInstance(datos, dict)
                self.assertEqual(set(datos.keys()), self.categorias)
                for v in datos.values():
                    self.assertEqual(v, [])
            finally:
                os.chdir(original_dir)

    def test_cargar_datos_con_archivo(self):
        test_data = {
            'Objetos Comunes': [{'nombre': 'Poción', 'cantidad': 1}],
            'Poké Balls': [],
            'Objetos Clave': [],
            'Bayas': [],
            'MT/MO': []
        }
        with tempfile.TemporaryDirectory() as tmpdir:
            original_dir = os.getcwd()
            os.chdir(tmpdir)
            try:
                with open('inventario.json', 'w', encoding='utf-8') as f:
                    json.dump(test_data, f, indent=4, ensure_ascii=False)
                datos = inventario.cargar_datos()
                self.assertEqual(datos, test_data)
            finally:
                os.chdir(original_dir)

    def test_cargar_datos_archivo_invalido(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            original_dir = os.getcwd()
            os.chdir(tmpdir)
            try:
                with open('inventario.json', 'w', encoding='utf-8') as f:
                    f.write('esto no es json')
                datos = inventario.cargar_datos()
                self.assertIsInstance(datos, dict)
                self.assertEqual(set(datos.keys()), self.categorias)
            finally:
                os.chdir(original_dir)


class TestGuardarDatos(unittest.TestCase):
    def test_guardar_datos_crea_archivo(self):
        test_data = {
            'Objetos Comunes': [],
            'Poké Balls': [],
            'Objetos Clave': [],
            'Bayas': [],
            'MT/MO': []
        }
        with tempfile.TemporaryDirectory() as tmpdir:
            original_dir = os.getcwd()
            os.chdir(tmpdir)
            try:
                inventario.guardar_datos(test_data)
                self.assertTrue(os.path.exists('inventario.json'))
                with open('inventario.json', 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                self.assertEqual(loaded, test_data)
            finally:
                os.chdir(original_dir)


class TestGuardarItem(unittest.TestCase):
    @patch('builtins.print')
    @patch('builtins.input')
    def test_guardar_item_exitoso(self, mock_input, mock_print):
        datos = {
            'Objetos Comunes': [],
            'Pok\u00e9 Balls': [],
            'Objetos Clave': [],
            'Bayas': [],
            'MT/MO': []
        }
        categoria = {1: 'Objetos Comunes'}

        with tempfile.TemporaryDirectory() as tmpdir:
            original_dir = os.getcwd()
            os.chdir(tmpdir)
            try:
                mock_input.side_effect = ['1', 'Poción', '5', 'Restaura PS', 'Una poción simple']

                inventario.guardar_item(datos, categoria)

                self.assertEqual(len(datos['Objetos Comunes']), 1)
                item = datos['Objetos Comunes'][0]
                self.assertEqual(item['nombre'], 'Poción')
                self.assertEqual(item['cantidad'], 5)
                self.assertEqual(item['efecto'], 'Restaura PS')
                self.assertEqual(item['descripcion'], 'Una poción simple')

                self.assertTrue(os.path.exists('inventario.json'))
            finally:
                os.chdir(original_dir)


class TestMostrarItems(unittest.TestCase):
    @patch('builtins.print')
    @patch('builtins.input')
    def test_mostrar_items_categoria_vacia(self, mock_input, mock_print):
        datos = {
            'Objetos Comunes': [],
            'Poké Balls': [],
            'Objetos Clave': [],
            'Bayas': [],
            'MT/MO': []
        }
        categoria = {1: 'Objetos Comunes'}
        mock_input.return_value = '1'

        inventario.mostrar_items(datos, categoria)

        printed_text = ''.join(call[0][0] for call in mock_print.call_args_list)
        self.assertIn('esta categoria esta vacia', printed_text)

    @patch('builtins.print')
    @patch('builtins.input')
    def test_mostrar_items_con_items(self, mock_input, mock_print):
        datos = {
            'Objetos Comunes': [
                {'nombre': 'Poción', 'cantidad': 5, 'efecto': 'Restaura PS', 'descripcion': 'Una poción'}
            ],
            'Poké Balls': [],
            'Objetos Clave': [],
            'Bayas': [],
            'MT/MO': []
        }
        categoria = {1: 'Objetos Comunes'}
        mock_input.return_value = '1'

        inventario.mostrar_items(datos, categoria)

        printed_text = ''.join(call[0][0] for call in mock_print.call_args_list)
        self.assertIn('Poción', printed_text)
        self.assertIn('5', printed_text)


if __name__ == '__main__':
    unittest.main()
