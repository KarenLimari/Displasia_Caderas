class Radiografia:
    """
    Clase para evaluar posibles signos de displasia de cadera mediante análisis radiográfico.
    """
    def __init__(self):
        """
        Constructor de la clase Radiografia.

        Atributos:
            angulo_acetabular (float): Ángulo acetabular en grados.
            cuadrante_cabeza_femoral (str): Cuadrante de ubicación de la cabeza femoral.
            linea_shenton (str): Estado de la línea de Shenton (continua o discontinua).
        """
        self.angulo_acetabular = None
        self.cuadrante_cabeza_femoral = None
        self.linea_shenton = None

    def medidas_signos_radiologicos(self, angulo_acetabular, cuadrante_cabeza_femoral, linea_shenton):
        """
        Establece las medidas y signos radiológicos de la radiografía.

        Parámetros:
            angulo_acetabular (float): Ángulo acetabular en grados.
            cuadrante_cabeza_femoral (str): Cuadrante de ubicación de la cabeza femoral.
            linea_shenton (str): Estado de la línea de Shenton (continua o discontinua).
        """
        self.angulo_acetabular = angulo_acetabular
        self.cuadrante_cabeza_femoral = cuadrante_cabeza_femoral
        self.linea_shenton = linea_shenton

    def evaluar_displasia(self):
        """
        Evalúa las medidas y signos ingresados, y genera alertas si están fuera de lo esperado.

        Devuelve:
            list: Lista de alertas generadas.
        """

        medidas_normales = {"acetabular": 30, "cuadrante": "inferomedial", "shenton":"continua"}
        alertas = []

        # Verifica el ángulo acetabular
        if self.angulo_acetabular >= medidas_normales["acetabular"]:
            alertas.append(f"ALERTA de displasia: Ángulo acetabular elevado ({self.angulo_acetabular}°).")

        # Verifica la posición de la cabeza femoral en el cuadrante inferomedial
        if self.cuadrante_cabeza_femoral != medidas_normales["cuadrante"]:
            alertas.append(f"ALERTA de displasia: Cabeza femoral fuera del cuadrante correspondiente (actual: {self.cuadrante_cabeza_femoral}).")

        # Evalua la línea de Shenton
        if self.linea_shenton != medidas_normales["shenton"]:
            alertas.append(f"ALERTA de displasia: Línea de Shenton alterada (actual:{self.linea_shenton}).")

        return alertas

    def mostrar_medidas_signos(self):
        """
        Muestra las medidas y signos ingresados.

        Devuelve:
            str: Representación en cadena de las medidas ingresadas.
        """
        return (f"Medidas:\n- Ángulo acetabular: {self.angulo_acetabular}°\n"
            f"- Cuadrante de la cabeza femoral: {self.cuadrante_cabeza_femoral}\n"
            f"- Línea de Shenton: {self.linea_shenton}")

print("Evaluación de displasia de cadera")

# Caso 1: Radiografía con medidas alteradas
radiografia_paciente1 = Radiografia()
radiografia_paciente1.medidas_signos_radiologicos(32, "superolateral", "discontinua")  # Medidas alteradas
alertas1 = radiografia_paciente1.evaluar_displasia()

print("\nResultados para la radiografía del paciente 1:")
print("\n".join(alertas1) if alertas1 else "Las medidas son normales.")
print(radiografia_paciente1.mostrar_medidas_signos())

# Caso 2: Radiografía con medidas normales
radiografia_paciente2 = Radiografia()
radiografia_paciente2.medidas_signos_radiologicos(28, "inferomedial", "continua")  # Medidas normales
alertas2 = radiografia_paciente2.evaluar_displasia()

print("\nResultados para la radiografía del paciente 2:")
if alertas2:
    print("\n".join(alertas2))
else:
    print("Las medidas son normales, no se detectan ALERTAS de displasia.")
print(radiografia_paciente2.mostrar_medidas_signos())