import requests

def obtener_tipo_cambio(monedas):
    """
    Obtiene el tipo de cambio entre dos monedas.

    Args:
        monedas (dict): Diccionario con dos claves: "entrada" y "salida", que corresponden a los códigos de las
            dos monedas a convertir.

    Returns:
        float: El tipo de cambio entre la moneda origen y la moneda destino.

    Raises:
        Exception: Si ocurre un error al obtener el tipo de cambio.
    """

    url = f"https://api.exchangerate-api.com/v4/latest/{monedas['entrada']}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        tipo_cambio = datos["rates"][monedas["salida"]]
        return tipo_cambio
    else:
        raise Exception("Error al obtener el tipo de cambio")

def convertir_moneda(cantidad, monedas):
    """
    Convierte una cantidad de una moneda a otra.
    
    Pide el tipo de cambio a la API de exchangerate-api.com y devuelve el resultado de la conversión.
    
    Parameters:
    cantidad (float): cantidad a convertir
    monedas (dict): diccionario con las claves "entrada" y "salida" cuyos valores son los códigos de las monedas de entrada y salida
                    (Ej: {"entrada": "EUR", "salida": "USD"})
    
    Returns:
    float: resultado de la conversión o None si ocurre un error
    """

    tipo_cambio = obtener_tipo_cambio(monedas)
    resultado = cantidad * tipo_cambio
    return resultado

def main():
    """
    Programa principal que interact a con el usuario para convertir una cantidad de una moneda a otra.
    
    Pide al usuario la cantidad a convertir y las monedas de origen y destino, y muestra el resultado de la conversión.
    """

    print("Conversor de monedas")
    cantidad = float(input("Ingrese la cantidad a convertir: "))
    moneda_origen = (input("Ingrese la moneda de entrada (EUR, USD, etc.): ")).upper()
    moneda_destino = (input("Ingrese la moneda de salida (EUR, USD, etc.): ")).upper()
    monedas = {"entrada": moneda_origen, "salida": moneda_destino}
    try:
        resultado = convertir_moneda(cantidad, monedas)
        print(f"{cantidad} {moneda_origen} es igual a {resultado} {moneda_destino}")
    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    main()