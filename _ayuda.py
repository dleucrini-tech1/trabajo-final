# Función auxiliar para las pruebas. No hace falta modificarla.
resultados = []


def chequear(descripcion, funcion):
    """Ejecuta funcion(); si devuelve True, la prueba pasó."""
    try:
        ok = funcion() is True
    except Exception as error:
        ok = False
        descripcion += f"  (error: {type(error).__name__}: {error})"
    resultados.append(ok)
    print(("OK     " if ok else "FALLA  ") + descripcion)


def resumen_final():
    print(f"\n{sum(resultados)} de {len(resultados)} pruebas pasaron")
    if all(resultados):
        print("¡Perfecto! Podés seguir con la próxima etapa.")
    else:
        print("Revisá las pruebas que fallaron (ver el TODO correspondiente).")
