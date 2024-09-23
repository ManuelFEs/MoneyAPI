import unittest
from monedas import obtener_tipo_cambio, convertir_moneda, main
from unittest.mock import patch

class TestConversion(unittest.TestCase):
    def test_obtener_tipo_cambio(self):
        # Test case for successful API request
        monedas = {"entrada": "EUR", "salida": "USD"}
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {
                "rates": {"USD": 1.2}
            }
            result = obtener_tipo_cambio(monedas)
            self.assertEqual(result, 1.2)
        
        # Test case for failed API request
        monedas = {"entrada": "EUR", "salida": "USD"}
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 500
            with self.assertRaises(Exception):
                obtener_tipo_cambio(monedas)
    
    def test_convertir_moneda(self):
        # Test case for successful conversion
        cantidad = 100
        monedas = {"entrada": "EUR", "salida": "USD"}
        with patch('monedas.obtener_tipo_cambio') as mock_obtener_tipo_cambio:
            mock_obtener_tipo_cambio.return_value = 1.2
            result = convertir_moneda(cantidad, monedas)
            self.assertEqual(result, 120.0)
        
        # Test case for failed conversion
        cantidad = 100
        monedas = {"entrada": "EUR", "salida": "USD"}
        with patch('monedas.obtener_tipo_cambio') as mock_obtener_tipo_cambio:
            mock_obtener_tipo_cambio.side_effect = Exception("Error al obtener el tipo de cambio")
            with self.assertRaises(Exception):
                convertir_moneda(cantidad, monedas)
    
    def test_main(self):
        # Test case for successful conversion
        with patch('builtins.input', side_effect=["100", "EUR", "USD"]):
            with patch('monedas.obtener_tipo_cambio', return_value=1.2):
                with patch('monedas.convertir_moneda', return_value=120.0):
                    main()
    
        # Test case for failed conversion
        with patch('builtins.input', side_effect=["100", "EUR", "USD"]):
            with patch('monedas.obtener_tipo_cambio', side_effect=Exception("Error al obtener el tipo de cambio")):
                with self.assertRaises(Exception):
                    main()

if __name__ == '__main__':
    unittest.main()