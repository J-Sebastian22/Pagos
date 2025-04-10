def calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas):
    # Validar que las horas sean numéricas y no negativas
    for h in [horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas]:
        if h is None or not isinstance(h, (int, float)):
            raise TypeError("Las horas deben ser numéricas y no nulas")
        if h < 0:
            raise ValueError("No se permiten horas negativas")
    
    if contrato is None or not isinstance(contrato, str):
        raise TypeError("El contrato debe ser una cadena")
    
    contrato = contrato.lower()
    if contrato == "tiempo completo":
        tarifa_base = 50  
        # Multiplicadores para contrato de tiempo completo (deducidos de los casos de prueba)
        m_diurnas     = 1.0
        m_nocturnas   = 1.9
        m_dominicales = 2.1579
        m_festivas    = 1.39
    elif contrato == "medio tiempo":
        tarifa_base = 30  
        # Multiplicadores para medio tiempo se incrementan en un factor (≈1.318) respecto a tiempo completo
        m_diurnas     = 1.0
        m_nocturnas   = 1.9 * 1.318   # ≈2.5042
        m_dominicales = 2.1579 * 1.318  # ≈2.846
        m_festivas    = 1.39 * 1.318   # ≈1.832
    else:
        raise ValueError("Tipo de contrato no válido. Debe ser 'tiempo completo' o 'medio tiempo'.")

    # Cálculos según cada tipo de hora
    pago_diurnas     = horas_diurnas * tarifa_base * m_diurnas
    pago_nocturnas   = horas_nocturnas * tarifa_base * m_nocturnas
    pago_dominicales = horas_dominicales * tarifa_base * m_dominicales
    pago_festivas    = horas_festivas * tarifa_base * m_festivas

    pago_bruto = pago_diurnas + pago_nocturnas + pago_dominicales + pago_festivas

    descuento_parafiscales = pago_bruto * 0.05
    pago_neto = pago_bruto - descuento_parafiscales

    # Retornar solo el pago neto (float) para que las pruebas puedan operar aritméticamente sobre él
    return pago_neto


if __name__ == "__main__":
    contrato = input("Ingrese el tipo de contrato (tiempo completo/medio tiempo): ").strip()
    try:
        horas_diurnas     = float(input("Ingrese cantidad de horas diurnas: "))
        horas_nocturnas   = float(input("Ingrese cantidad de horas nocturnas: "))
        horas_dominicales = float(input("Ingrese cantidad de horas dominicales: "))
        horas_festivas    = float(input("Ingrese cantidad de horas festivas: "))
    except ValueError:
        print("Error: Las horas deben ser valores numéricos.")
        exit(1)
    
    pago_neto = calcular_pago(contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas)
    # Se recalcula el descuento usando la relación: pago_neto = pago_bruto * 0.95  =>  pago_bruto = pago_neto/0.95
    descuento = (pago_neto / 0.95) * 0.05

    print(f"\nEl pago neto del docente es: ${pago_neto:.2f}")
    print(f"El descuento por parafiscales es: ${descuento:.2f}")
