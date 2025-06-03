materias = {
    "Calculo I": {"Creditos": 5, "Teoria": 5, "Laboratorio": 0, "Clases": [12, 12, 11]},
    "Calculo II": {"Creditos": 5, "Teoria": 5, "Laboratorio": 0, "Clases": [22, 22, 21]},
    "Calculo III": {"Creditos": 4, "Teoria": 4, "Laboratorio": 0, "Clases": [32, 32]},
    "Fisica I": {"Creditos": 5, "Teoria": 4, "Laboratorio": 2, "Clases": [42, 42]},
    "Fisica II": {"Creditos": 5, "Teoria": 4, "Laboratorio": 2, "Clases": [52, 52]},
    "Quimica I": {"Creditos": 4, "Teoria": 3, "Laboratorio": 3, "Clases": [62, 61]},
    "Ingles I": {"Creditos": 3, "Teoria": 3, "Laboratorio": 0, "Clases": [72, 71]},
    "Ingles II": {"Creditos": 3, "Teoria": 3, "Laboratorio": 0, "Clases": [82, 81]},
    "Comunicación Oral y Escrita": {"Creditos": 3, "Teoria": 3, "Laboratorio": 0, "Clases": [92, 91]},
    "Geografía": {"Creditos": 3, "Teoria": 3, "Laboratorio": 0, "Clases": [103]},
    "Dibujo I": {"Creditos": 4, "Teoria": 2, "Laboratorio": 4, "Clases": [113, 113]},
    "Desarrollo lógico y algoritmos": {"Creditos": 4, "Teoria": 3, "Laboratorio": 2, "Clases": [122, 123]}
}
preferencias = {
    "Calculo I": {"Matutino": [1, 1, 0, 0, 0, 1, 5000], "Vespertino": [5000, 0, 0, 0, 1, 3]},
    "Calculo II": {"Matutino": [1, 1, 0, 0, 0, 1, 5000], "Vespertino": [5000, 0, 0, 0, 1, 3]},
    "Calculo III": {"Matutino": [1, 1, 0, 0, 0, 1, 5000], "Vespertino": [5000, 0, 0, 0, 1, 3]},
    "Fisica I": {"Matutino": [1, 1, 0, 0, 0, 1, 5000], "Vespertino": [5000, 0, 0, 0, 1, 3]},
    "Fisica II": {"Matutino": [1, 1, 0, 0, 0, 1, 5000], "Vespertino": [5000, 0, 0, 0, 1, 3]},
    "Quimica I": {"Matutino": [1, 1, 0, 0, 0, 1, 5000], "Vespertino": [5000, 0, 0, 0, 1, 3]},
    "Ingles I": {"Matutino": [1, 10, 1, 0, 0, 0, 75000000], "Vespertino": [75000000, 0, 0, 0, 0, 0]},
    "Ingles II": {"Matutino": [1, 10, 1, 0, 0, 0, 75000000], "Vespertino": [75000000, 0, 0, 0, 0, 0]},
    "Comunicación Oral y Escrita": {"Matutino": [1, 10, 0, 0, 0, 0, 75000000], "Vespertino": [75000000, 0, 0, 0, 0, 0]},
    "Geografía": {"Matutino": [1, 10, 0, 0, 0, 0, 75000000], "Vespertino": [75000000, 0, 0, 0, 0, 0]},
    "Dibujo I": {"Matutino": [0, 0, 0, 0, 0, 0, 0], "Vespertino": [0, 0, 0, 0, 0, 0]},
    "Desarrollo lógico y algoritmos": {"Matutino": [1, 0, 0, 0, 0, 0, 5], "Vespertino": [1, 0, 0, 0, 1, 2]}
}
OpcionA = {
    "Semestre1": ["Calculo I", "Quimica I", "Comunicación Oral y Escrita", "Desarrollo lógico y algoritmos", "Fisica I", "Ingles I"],
    "Semestre2": ["Calculo II", "Calculo III", "Geografía", "Dibujo I", "Fisica II", "Ingles II"]
}

OpcionB = {
     "Semestre1": ["Calculo I", "Fisica I", "Ingles I", "Geografía", "Dibujo I", "Desarrollo lógico y algoritmos"],
     "Semestre2": ["Calculo II", "Calculo III", "Fisica II", "Ingles II", "Quimica I", "Comunicación Oral y Escrita"]
}

primera_ultima_hora = {
     "Semestre1": ["Dibujo I"],
     "Semestre2": ["Dibujo I"]
}
horas_minimas = 4

capacidad = {
    "Calculo I": 100,
    "Calculo II": 100,
    "Calculo III": 100,
    "Fisica I": 100,
    "Fisica II": 100,
    "Quimica I": 100,
    "Ingles I": 100,
    "Ingles II": 100,
    "Comunicación Oral y Escrita": 100,
    "Geografía": 100,
    "Dibujo I": 5,
    "Desarrollo lógico y algoritmos": 100,
}


separacion = {
    "Dibujo I": 1 , # Número mínimo de horas de separación entre clases de Dibujo I
    "Desarrollo lógico y algoritmos": 1  # Número mínimo de horas de separación entre clases de Dibujo I
}
# %%


import random


def movimiento_espejo_dia(individuo, horas_maximas, semestre, aptitud_ultimo_elite):
    """
    Realiza un movimiento de espejo en un individuo invirtiendo el orden de las clases en un día.

    Args:
        individuo: Una tupla con los dos cromosomas del individuo (Opción A y Opción B).
        horas_maximas: Número máximo de horas en el horario.
        semestre: El semestre actual.

    Returns:
        El individuo modificado si el movimiento mejora la aptitud; de lo contrario, el individuo original.
    """
    cromosoma_A, cromosoma_B = individuo
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    aptitud_anterior = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas, semestre)  # Calcular la aptitud inicial
    mejora_encontrada = False

    # ----> Recorrer primero el cromosoma B <----
    for grupo in cromosoma_B:
        for dia in dias_semana:
            # Guardar el estado original del día
            clases_originales = grupo[dia][1:]
            hora_inicio_original = grupo[dia][0]

            # Invertir las clases y poner la hora de inicio a 0
            grupo[dia] = [0] + clases_originales[::-1]

            # Calcular la aptitud del individuo con el cambio
            aptitud_actual = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas, semestre)

            # Verificar si la aptitud mejora
            if aptitud_actual < aptitud_anterior:
                aptitud_anterior = aptitud_actual
                mejora_encontrada = True
            else:
                # Revertir el cambio si no hay mejora
                grupo[dia] = [hora_inicio_original] + clases_originales

    # ----> Recorrer el cromosoma A si no se encontró una mejora en el cromosoma B <----
    if not mejora_encontrada:
        for grupo in cromosoma_A:
            for dia in dias_semana:
                # Guardar el estado original del día
                clases_originales = grupo[dia][1:]
                hora_inicio_original = grupo[dia][0]

                # Invertir las clases y poner la hora de inicio a 0
                grupo[dia] = [0] + clases_originales[::-1]

                # Calcular la aptitud del individuo con el cambio
                aptitud_actual = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas, semestre)

                # Verificar si la aptitud mejora
                if aptitud_actual < aptitud_anterior:
                    aptitud_anterior = aptitud_actual
                    mejora_encontrada = True
                else:
                    # Revertir el cambio si no hay mejora
                    grupo[dia] = [hora_inicio_original] + clases_originales

    return cromosoma_A, cromosoma_B


def aplicar_movimiento_espejo_dia(poblacion, horas_maximas, semestre, aptitud_ultimo_elite):
    """
    Aplica el movimiento de espejo a cada individuo de la población.

    Args:
        poblacion: Una lista de individuos.
        horas_maximas: Número máximo de horas en el horario.
        semestre: El semestre actual.
        aptitud_ultimo_elite: Aptitud del último individuo del grupo elite.

    Returns:
        La población modificada.
    """
    poblacion_modificada = []
    for individuo in poblacion:
        individuo_modificado = movimiento_espejo_dia(individuo, horas_maximas, semestre, aptitud_ultimo_elite)
        poblacion_modificada.append(individuo_modificado)

    return poblacion_modificada



def movimiento_cambio_dia(individuo, horas_maximas, semestre, aptitud_ultimo_elite):
    """
    Realiza un movimiento de mejora en un individuo intercambiando días de un grupo.

    Args:
        individuo: Una tupla con los dos cromosomas del individuo (Opción A y Opción B).
        horas_maximas: Número máximo de horas en el horario.
        semestre: El semestre actual.
        aptitud_ultimo_elite: La aptitud del último individuo del grupo elite.

    Returns:
        El individuo modificado.
    """
    cromosoma_A, cromosoma_B = individuo
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    aptitud_anterior = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas, semestre)  # Calcular la aptitud inicial
    mejora_encontrada = False

    # Si la aptitud del individuo es mejor o igual que la del último elite, no intentamos mejorar
    if aptitud_anterior >= aptitud_ultimo_elite:
        return individuo

    # ----> Recorrer el cromosoma A <----
    for grupo_idx, grupo in enumerate(cromosoma_A):
        for dia_idx_1 in range(len(dias_semana) - 1):
            for dia_idx_2 in range(dia_idx_1 + 1, len(dias_semana)):
                # Intercambiar los días
                grupo[dias_semana[dia_idx_1]], grupo[dias_semana[dia_idx_2]] = (
                    grupo[dias_semana[dia_idx_2]],
                    grupo[dias_semana[dia_idx_1]],
                )

                # Calcular la aptitud del individuo después del intercambio
                aptitud_actual = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas, semestre)

                # Deshacer el intercambio si la aptitud no mejora
                if aptitud_actual > aptitud_anterior:
                    grupo[dias_semana[dia_idx_1]], grupo[dias_semana[dia_idx_2]] = (
                        grupo[dias_semana[dia_idx_2]],
                        grupo[dias_semana[dia_idx_1]],
                    )
                else:
                    aptitud_anterior = aptitud_actual  # Actualizar la aptitud anterior si mejora
                    mejora_encontrada = True
                    break  # Salir del bucle si se encontró una mejora
            if mejora_encontrada:
                break  # Salir del bucle de 'dia_idx_1' si se encontró una mejora
        if mejora_encontrada:
            break  # Salir del bucle de 'grupo' si se encontró una mejora

    # ----> Recorrer el cromosoma B si no se encontró una mejora en el cromosoma A <----
    if not mejora_encontrada:
        for grupo_idx, grupo in enumerate(cromosoma_B):
            for dia_idx_1 in range(len(dias_semana) - 1):
                for dia_idx_2 in range(dia_idx_1 + 1, len(dias_semana)):
                    # Intercambiar los días
                    grupo[dias_semana[dia_idx_1]], grupo[dias_semana[dia_idx_2]] = (
                        grupo[dias_semana[dia_idx_2]],
                        grupo[dias_semana[dia_idx_1]],
                    )

                    # Calcular la aptitud del individuo después del intercambio
                    aptitud_actual = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas, semestre)

                    # Deshacer el intercambio si la aptitud no mejora
                    if aptitud_actual > aptitud_anterior:
                        grupo[dias_semana[dia_idx_1]], grupo[dias_semana[dia_idx_2]] = (
                            grupo[dias_semana[dia_idx_2]],
                            grupo[dias_semana[dia_idx_1]],
                        )
                    else:
                        aptitud_anterior = aptitud_actual  # Actualizar la aptitud anterior si mejora
                        mejora_encontrada = True
                        break  # Salir del bucle si se encontró una mejora
                if mejora_encontrada:
                    break  # Salir del bucle de 'dia_idx_1' si se encontró una mejora
            if mejora_encontrada:
                break  # Salir del bucle de 'grupo' si se encontró una mejora

    return cromosoma_A, cromosoma_B


def aplicar_movimiento_cambio_dia(poblacion, horas_maximas, semestre, aptitud_ultimo_elite):
    """
    Aplica el movimiento de cambio de día a cada individuo de la población.

    Args:
        poblacion: Una lista de individuos.
        horas_maximas: Número máximo de horas en el horario.
        semestre: El semestre actual.
        aptitud_ultimo_elite: La aptitud del último individuo del grupo elite.

    Returns:
        La población modificada.
    """
    poblacion_modificada = []
    for individuo in poblacion:
        individuo_modificado = movimiento_cambio_dia(individuo, horas_maximas, semestre, aptitud_ultimo_elite)
        poblacion_modificada.append(individuo_modificado)

    return poblacion_modificada




def calcular_penalizacion_primera_ultima(cromosoma_A, cromosoma_B, semestre):
    """
    Calcula la penalización por clases que no están en la primera o última hora del día.

    Args:
        cromosoma_A: Cromosoma A del individuo.
        cromosoma_B: Cromosoma B del individuo.
        semestre: El semestre actual.

    Returns:
        La cantidad de veces que la materia no está en la primera o última hora del día.
    """
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    penalizacion = 0
    
    # Recorremos todas las materias que necesitan estar en la primera o última hora
    for materia in primera_ultima_hora[semestre]:
        # Verificamos en el cromosoma A si la materia está presente
        if materia in OpcionA[semestre]:
            for grupo in cromosoma_A:
                for dia in dias_semana:
                    # Verificar si la materia está en el día actual
                    clases_dia = grupo[dia]
                    for codigo_clase in clases_dia[1:]:
                        if codigo_clase // 10 in [c // 10 for c in materias[materia]["Clases"]]:
                            # Verificar si la clase es la primera del día (hora de desfase es 0)
                            if clases_dia.index(codigo_clase) == 1 and clases_dia[0] == 0:
                                continue
                            # Verificar si la clase es la última del día
                            horas_totales = sum(clase % 10 for clase in clases_dia[1:]) + clases_dia[0]
                            if clases_dia.index(codigo_clase) == len(clases_dia) - 1 and horas_totales == horas_maximas:
                                continue
                            # Si no cumple ninguna condición, penalizamos
                            penalizacion += 1

        # Verificamos en el cromosoma B si la materia está presente
        if materia in OpcionB[semestre]:
            for grupo in cromosoma_B:
                for dia in dias_semana:
                    # Verificar si la materia está en el día actual
                    clases_dia = grupo[dia]
                    for codigo_clase in clases_dia[1:]:
                        if codigo_clase // 10 in [c // 10 for c in materias[materia]["Clases"]]:
                            # Verificar si la clase es la primera del día (hora de desfase es 0)
                            if clases_dia.index(codigo_clase) == 1 and clases_dia[0] == 0:
                                continue
                            # Verificar si la clase es la última del día
                            horas_totales = sum(clase % 10 for clase in clases_dia[1:]) + clases_dia[0]
                            if clases_dia.index(codigo_clase) == len(clases_dia) - 1 and horas_totales == horas_maximas:
                                continue
                            # Si no cumple ninguna condición, penalizamos
                            penalizacion += 1
               
    return penalizacion






def calcular_penalizacion_separacion(cromosoma_A, cromosoma_B, semestre):
    """Calcula la penalización por incumplir la separación mínima entre clases según las restricciones."""
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    penalizacion = 0

    for materia, separacion_minima in separacion.items():
        # Verificar si la materia está presente en el semestre para cada cromosoma
        if materia in OpcionA[semestre]:
            penalizacion += calcular_penalizacion_separacion_materia(cromosoma_A, materia, dias_semana, separacion_minima)

        if materia in OpcionB[semestre]:
            penalizacion += calcular_penalizacion_separacion_materia(cromosoma_B, materia, dias_semana, separacion_minima)

    return penalizacion

def calcular_penalizacion_separacion_materia(cromosoma, materia, dias_semana, separacion_minima):
    """Calcula la penalización por incumplir la separación mínima para una materia en un cromosoma."""
    penalizacion = 0
    
    # Recorremos cada grupo del cromosoma para la materia dada
    for grupo in cromosoma:
        vector_dias = [0] * len(dias_semana)

        # Crear el vector que indica la presencia de la materia cada día
        for dia_idx, dia in enumerate(dias_semana):
            for clase in grupo[dia]:
                if clase // 10 in [c // 10 for c in materias[materia]["Clases"]]:
                    vector_dias[dia_idx] = 1
                    break

        # Calcular la distancia mínima entre dos 1 en el vector
        distancia_minima = len(dias_semana)  # Inicializar con un valor máximo
        ultimo_1 = -1

        for i, valor in enumerate(vector_dias):
            if valor == 1:
                if ultimo_1 != -1:
                    distancia = i - ultimo_1 - 1
                    distancia_minima = min(distancia_minima, distancia)
                ultimo_1 = i

        # Penalizar si la distancia mínima es menor que la requerida
        if distancia_minima < separacion_minima:
            
            penalizacion += 1


    return penalizacion






def generar_matriz_frecuencias_asignatura(cromosoma_A, cromosoma_B, horas_maximas):
    """
    Genera una matriz de frecuencias por hora para cada asignatura.

    Args:
        cromosoma_A: Cromosoma A del individuo.
        cromosoma_B: Cromosoma B del individuo.
        horas_maximas: Número máximo de horas en el horario.

    Returns:
        Un diccionario donde la clave es el nombre de la asignatura y el valor es una matriz de frecuencias por hora.
    """
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    num_asignaturas = len(materias)
    
    # Inicializar una matriz para cada asignatura
    frecuencias_asignaturas = {
        nombre_materia: [[0 for _ in range(len(dias_semana))] for _ in range(horas_maximas)]
        for nombre_materia in materias.keys()
    }

    # Recorrer ambos cromosomas para contar las frecuencias de cada asignatura
    for cromosoma in [cromosoma_A, cromosoma_B]:
        for grupo in cromosoma:
            for dia_idx, dia in enumerate(dias_semana):
                for clase in grupo[dia]:
                    if clase != 0:
                        materia_id = clase // 10
                        nombre_materia = list(materias.keys())[materia_id - 1]
                        duracion_clase = clase % 10
                        hora_inicio = grupo[dia][0]
                        for i in range(duracion_clase):
                            hora_actual = hora_inicio + i
                            if hora_actual < horas_maximas:
                                frecuencias_asignaturas[nombre_materia][hora_actual][dia_idx] += 1

    return frecuencias_asignaturas


def calcular_penalizacion_exceso_capacidad(cromosoma_A, cromosoma_B, horas_maximas):
    """
    Calcula la penalización por exceder la capacidad en cada asignatura.

    Args:
        cromosoma_A: Cromosoma A del individuo.
        cromosoma_B: Cromosoma B del individuo.
        horas_maximas: Número máximo de horas en el horario.

    Returns:
        La penalización total por exceder la capacidad de cada asignatura.
    """
    cromosomas = [cromosoma_A, cromosoma_B]
    penalizacion_total = 0

    # Inicializamos un diccionario para almacenar los laboratorios simultáneos por materia
    laboratorios_simultaneos = {materia: [] for materia in capacidad.keys()}

    # Recorrer cada grupo en cada cromosoma
    for cromosoma in cromosomas:
        for grupo in cromosoma:
            # Recorrer cada día de la semana
            for dia in grupo.keys():
                # Obtener la hora de inicio para el grupo actual en el día
                hora_inicio = grupo[dia][0]

                # Recorrer todas las clases del día
                for idx, clase in enumerate(grupo[dia][1:], start=1):
                    materia_id = clase // 10
                    nombre_materia = list(materias.keys())[materia_id - 1]
                    duracion_clase = clase % 10

                    # Verificar si la materia tiene laboratorio
                    if "Laboratorio" in materias[nombre_materia] and materias[nombre_materia]["Laboratorio"] > 0:
                        # Determinar el rango de la clase actual (hora de inicio y fin)
                        hora_fin = hora_inicio + duracion_clase
                        choques = 0

                        # Comparar la clase con todas las demás clases en otros grupos
                        for otro_cromosoma in cromosomas:
                            for otro_grupo in otro_cromosoma:
                                if otro_grupo == grupo:
                                    continue  # Saltar el mismo grupo que se está evaluando

                                # Obtener la hora de inicio para el otro grupo en el mismo día
                                otro_hora_inicio = otro_grupo[dia][0]

                                # Comparar todas las clases del día en el otro grupo
                                for otro_idx, otra_clase in enumerate(otro_grupo[dia][1:], start=1):
                                    otro_materia_id = otra_clase // 10
                                    otro_duracion_clase = otra_clase % 10

                                    # Determinar el rango de la otra clase (hora de inicio y fin)
                                    otro_hora_fin = otro_hora_inicio + otro_duracion_clase

                                    # Verificar si ambas clases son de la misma materia y si se solapan
                                    if materia_id == otro_materia_id and (
                                            (hora_inicio < otro_hora_fin and hora_fin > otro_hora_inicio)):
                                        choques += 1

                                    # Avanzar la hora de inicio para la siguiente clase en el otro grupo
                                    otro_hora_inicio += otro_duracion_clase

                        # Sumamos 1 para incluir la clase misma y almacenamos el resultado
                        laboratorios_simultaneos[nombre_materia].append(choques + 1)

                    # Avanzar la hora de inicio para la siguiente clase
                    hora_inicio += duracion_clase

    # Calcular la penalización si alguna frecuencia excede la capacidad
    for nombre_materia, valores in laboratorios_simultaneos.items():
        capacidad_maxima = capacidad[nombre_materia]

        for valor in valores:
            if valor > capacidad_maxima:
                penalizacion_total += (valor - capacidad_maxima) * 10000000  # Penalización proporcional al exceso
                
    # print(f"Penalización por exceso de capacidad en {nombre_materia}: {valor}")

    return penalizacion_total





def aplicar_movimiento_intercambio_dias(poblacion, horas_maximas, semestre,aptitud_ultimo_elite):
    """
    Aplica el movimiento de intercambio de asignaturas entre días a cada individuo de la población.

    Args:
        poblacion: Una lista de individuos.
        horas_maximas: Número máximo de horas en el horario.
        semestre: El semestre actual.

    Returns:
        La población modificada.
    """
    poblacion_modificada = []
    for individuo in poblacion:
        cromosoma_A, cromosoma_B = individuo
        aptitud_actual = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas, semestre)
      

        if aptitud_actual >= aptitud_ultimo_elite:
            poblacion_modificada.append((cromosoma_A, cromosoma_B))
            continue

        mejora_encontrada = False
        nueva_aptitud = aptitud_actual

        # Recorrer el cromosoma A
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        # 1. Crear el diccionario de días para cada código de asignatura
        
        for grupo_idx, grupo in enumerate(cromosoma_A):
            
            dias_por_asignatura = {}
            for dia in dias_semana:
                for i, clase in enumerate(grupo[dia]):
                    if i == 0:  # Ignorar la hora de inicio
                        continue
                    asignatura = clase // 10
                    if asignatura not in dias_por_asignatura:
                        dias_por_asignatura[asignatura] = [0] * len(dias_semana)  # Inicializar con ceros
                    dias_por_asignatura[asignatura][dias_semana.index(dia)] = 1  # Marcar el día como ocupado

            # 2. Recorrer los días
            for i in range(len(dias_semana) - 1):
                for j in range(i + 1, len(dias_semana)):
                    dia_i = dias_semana[i]
                    dia_j = dias_semana[j]

                    # 3. Recorrer las clases del día i
                    for k in range(1, len(grupo[dia_i])):
                        clase_i = grupo[dia_i][k]
                        asignatura_i = clase_i // 10  # Obtener el ID de la asignatura

                        # 4. Recorrer las clases del día j
                        for l in range(1, len(grupo[dia_j])):
                            clase_j = grupo[dia_j][l]
                            asignatura_j = clase_j // 10  # Obtener el ID de la asignatura

                            # 5. Verificar si las clases tienen la misma duración
                            if clase_i % 10 == clase_j % 10:
                                # 6. Verificar que las asignaturas no estén en el mismo día
                                if dias_por_asignatura[asignatura_i][j] == 0 and dias_por_asignatura[asignatura_j][i] == 0:
                                    # 7. Intercambiar las clases
                                    grupo[dia_i][k], grupo[dia_j][l] = grupo[dia_j][l], grupo[dia_i][k]

                                    # Actualizar el diccionario dias_por_asignatura después del intercambio
                                    dias_por_asignatura[asignatura_i][dias_semana.index(dia_j)] = 1
                                    dias_por_asignatura[asignatura_j][dias_semana.index(dia_i)] = 1

                                    # 8. Calcular la nueva aptitud
                                    nueva_aptitud = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas, semestre)

                                    # 9. Verificar si la nueva aptitud es mejor
                                    if nueva_aptitud < aptitud_actual:
                                        cromosoma_A[grupo_idx] = grupo
                                        aptitud_actual = nueva_aptitud
                                        mejora_encontrada = True
                                        break # Salir del bucle interno si se encuentra una mejora
                                    else:
                                        # Deshacer el intercambio
                                        grupo[dia_i][k], grupo[dia_j][l] = grupo[dia_j][l], grupo[dia_i][k]
                                        # Actualizar el diccionario dias_por_asignatura después de deshacer el intercambio
                                        dias_por_asignatura[asignatura_i][dias_semana.index(dia_j)] = 0
                                        dias_por_asignatura[asignatura_j][dias_semana.index(dia_i)] = 0
                        if mejora_encontrada:
                            break # Salir del bucle interno si se encuentra una mejora
                if mejora_encontrada:
                    break # Salir del bucle interno si se encuentra una mejora
            if mejora_encontrada:
                break # Salir del bucle interno si se encuentra una mejora


        # Recorrer el cromosoma B (igual lógica que para el A)
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        # 1. Crear el diccionario de días para cada código de asignatura
        
        for grupo_idx, grupo in enumerate(cromosoma_B):
            dias_por_asignatura = {}
            for dia in dias_semana:
                for i, clase in enumerate(grupo[dia]):
                    if i == 0:  # Ignorar la hora de inicio
                        continue
                    asignatura = clase // 10
                    if asignatura not in dias_por_asignatura:
                        dias_por_asignatura[asignatura] = [0] * len(dias_semana)  # Inicializar con ceros
                    dias_por_asignatura[asignatura][dias_semana.index(dia)] = 1  # Marcar el día como ocupado

            # 2. Recorrer los días
            for i in range(len(dias_semana) - 1):
                for j in range(i + 1, len(dias_semana)):
                    dia_i = dias_semana[i]
                    dia_j = dias_semana[j]

                    # 3. Recorrer las clases del día i
                    for k in range(1, len(grupo[dia_i])):
                        clase_i = grupo[dia_i][k]
                        asignatura_i = clase_i // 10  # Obtener el ID de la asignatura

                        # 4. Recorrer las clases del día j
                        for l in range(1, len(grupo[dia_j])):
                            clase_j = grupo[dia_j][l]
                            asignatura_j = clase_j // 10  # Obtener el ID de la asignatura

                            # 5. Verificar si las clases tienen la misma duración
                            if clase_i % 10 == clase_j % 10:
                                # 6. Verificar que las asignaturas no estén en el mismo día
                                if dias_por_asignatura[asignatura_i][j] == 0 and dias_por_asignatura[asignatura_j][i] == 0:
                                    # 7. Intercambiar las clases
                                    grupo[dia_i][k], grupo[dia_j][l] = grupo[dia_j][l], grupo[dia_i][k]

                                    # Actualizar el diccionario dias_por_asignatura después del intercambio
                                    dias_por_asignatura[asignatura_i][dias_semana.index(dia_j)] = 1
                                    dias_por_asignatura[asignatura_j][dias_semana.index(dia_i)] = 1

                                    # 8. Calcular la nueva aptitud
                                    nueva_aptitud = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas, semestre)

                                    # 9. Verificar si la nueva aptitud es mejor
                                    if nueva_aptitud < aptitud_actual:
                                        cromosoma_B[grupo_idx] = grupo
                                        aptitud_actual = nueva_aptitud
                                        break # Salir del bucle interno si se encuentra una mejora
                                    else:
                                        # Deshacer el intercambio
                                        grupo[dia_i][k], grupo[dia_j][l] = grupo[dia_j][l], grupo[dia_i][k]
                                        # Actualizar el diccionario dias_por_asignatura después de deshacer el intercambio
                                        dias_por_asignatura[asignatura_i][dias_semana.index(dia_j)] = 0
                                        dias_por_asignatura[asignatura_j][dias_semana.index(dia_i)] = 0
                        if mejora_encontrada:
                            break # Salir del bucle interno si se encuentra una mejora
                if mejora_encontrada:
                    break # Salir del bucle interno si se encuentra una mejora
            if mejora_encontrada:
                break # Salir del bucle interno si se encuentra una mejora


        poblacion_modificada.append((cromosoma_A, cromosoma_B))

    return poblacion_modificada

def aplicar_movimiento_clase_a_otro_dia(poblacion, horas_maximas, semestre, aptitud_ultimo_elite):
    """
    Intenta mover una clase a otro día si hay espacio disponible y mejora la aptitud.

    Args:
        poblacion: Una lista de individuos.
        horas_maximas: Número máximo de horas en el horario.
        semestre: El semestre actual.
        aptitud_ultimo_elite: Aptitud del último individuo del grupo elite.

    Returns:
        La población modificada.
    """
    poblacion_modificada = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    for individuo in poblacion:
        cromosoma_A, cromosoma_B = individuo
        aptitud_actual = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas, semestre)
        
        if aptitud_actual >= aptitud_ultimo_elite:
            poblacion_modificada.append((cromosoma_A, cromosoma_B))
            continue

        mejora_encontrada = False
        #nueva_aptitud = aptitud_actual  # Inicializar nueva_aptitud No es necesario inicializarla aquí

        # Recorrer el cromosoma A
        for grupo_idx, grupo in enumerate(cromosoma_A):
            # 1. Crear el diccionario de días para cada código de asignatura
            dias_por_asignatura = {}
            for dia in dias_semana:
                for i, clase in enumerate(grupo[dia]):
                    if i == 0:  # Ignorar la hora de inicio
                        continue
                    asignatura = clase // 10
                    if asignatura not in dias_por_asignatura:
                        dias_por_asignatura[asignatura] = [0] * len(dias_semana)  # Inicializar con ceros
                    dias_por_asignatura[asignatura][dias_semana.index(dia)] = 1  # Marcar el día como ocupado

            # 2. Recorrer las clases del cromosoma
            for dia_idx, dia in enumerate(dias_semana):
                for i, clase in enumerate(grupo[dia]):
                    if i == 0:  # Ignorar la hora de inicio
                        continue

                    # Obtener el ID de la asignatura y la duración
                    asignatura = clase // 10
                    duracion = clase % 10

                    # 3. Buscar un día alternativo donde se pueda mover la clase
                    for dia_destino_idx in range(len(dias_semana)):
                        if dia_destino_idx == dia_idx:
                            continue  # No se mueve al mismo día

                        dia_destino = dias_semana[dia_destino_idx]

                        # 4. Verificar si el día destino está disponible
                        if dias_por_asignatura[asignatura][dia_destino_idx] == 0:
                            # 5. Verificar si hay espacio en el día destino
                            horas_dia_destino = sum(c % 10 for c in grupo[dia_destino][1:]) + grupo[dia_destino][0]
                            if horas_dia_destino + duracion <= horas_maximas:
                                # 6. Probar a mover la clase a diferentes posiciones en el día destino
                                for posicion_destino in range(1, len(grupo[dia_destino]) + 1):
                                    # 7. Realizar el movimiento de prueba
                                    grupo[dia_destino].insert(posicion_destino, clase)
                                    grupo[dia].pop(i)  # Eliminar la clase del día original
                                    
                                    # 8. Calcular la nueva aptitud
                                    nueva_aptitud = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas, semestre)

                                    # 9. Verificar si la nueva aptitud es mejor
                                    if nueva_aptitud < aptitud_actual:
                                        # 10. Realizar el movimiento en el grupo real
                                        #grupo[dia_destino].insert(posicion_destino, clase) # No es necesario porque ya se hizo el cambio en el paso anterior
                                        #grupo[dia].pop(i)  # No es necesario porque ya se hizo el cambio en el paso anterior
                                        aptitud_actual = nueva_aptitud  # Actualizar aptitud_actual
                                        mejora_encontrada = True
                                        break  # Salir del bucle de posiciones si se encontró una mejora
                                    else:
                                        # 11. Deshacer el cambio en el grupo de prueba
                                        grupo[dia_destino].pop(posicion_destino)
                                        grupo[dia].insert(i, clase)

                        if mejora_encontrada:
                            break  # Salir del bucle de días destino si se encontró una mejora

                if mejora_encontrada:
                    break  # Salir del bucle de clases si se encontró una mejora

            if mejora_encontrada:
                break  # Salir del bucle de grupos si se encontró una mejora

        # Recorrer el cromosoma B (igual lógica que para el A)
        mejora_encontrada = False
        #nueva_aptitud = aptitud_actual  # Inicializar nueva_aptitud No es necesario inicializarla aquí

        for grupo_idx, grupo in enumerate(cromosoma_B):
            # 1. Crear el diccionario de días para cada código de asignatura
            dias_por_asignatura = {}
            for dia in dias_semana:
                for i, clase in enumerate(grupo[dia]):
                    if i == 0:  # Ignorar la hora de inicio
                        continue
                    asignatura = clase // 10
                    if asignatura not in dias_por_asignatura:
                        dias_por_asignatura[asignatura] = [0] * len(dias_semana)  # Inicializar con ceros
                    dias_por_asignatura[asignatura][dias_semana.index(dia)] = 1  # Marcar el día como ocupado

            # 2. Recorrer las clases del cromosoma
            for dia_idx, dia in enumerate(dias_semana):
                for i, clase in enumerate(grupo[dia]):
                    if i == 0:  # Ignorar la hora de inicio
                        continue

                    # Obtener el ID de la asignatura y la duración
                    asignatura = clase // 10
                    duracion = clase % 10

                    # 3. Buscar un día alternativo donde se pueda mover la clase
                    for dia_destino_idx in range(len(dias_semana)):
                        if dia_destino_idx == dia_idx:
                            continue  # No se mueve al mismo día

                        dia_destino = dias_semana[dia_destino_idx]

                        # 4. Verificar si el día destino está disponible
                        if dias_por_asignatura[asignatura][dia_destino_idx] == 0:
                            # 5. Verificar si hay espacio en el día destino
                            horas_dia_destino = sum(c % 10 for c in grupo[dia_destino][1:]) + grupo[dia_destino][0]
                            if horas_dia_destino + duracion <= horas_maximas:
                                # 6. Probar a mover la clase a diferentes posiciones en el día destino
                                for posicion_destino in range(1, len(grupo[dia_destino]) + 1):
                                    # 7. Realizar el movimiento de prueba
                                    grupo[dia_destino].insert(posicion_destino, clase)
                                    grupo[dia].pop(i)  # Eliminar la clase del día original
                                    
                                    # 8. Calcular la nueva aptitud
                                    nueva_aptitud = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas, semestre)

                                    # 9. Verificar si la nueva aptitud es mejor
                                    if nueva_aptitud < aptitud_actual:
                                        # 10. Realizar el movimiento en el grupo real
                                        #grupo[dia_destino].insert(posicion_destino, clase) # No es necesario porque ya se hizo el cambio en el paso anterior
                                        #grupo[dia].pop(i)  # No es necesario porque ya se hizo el cambio en el paso anterior
                                        aptitud_actual = nueva_aptitud  # Actualizar aptitud_actual
                                        mejora_encontrada = True
                                        break  # Salir del bucle de posiciones si se encontró una mejora
                                    else:
                                        # 11. Deshacer el cambio en el grupo de prueba
                                        grupo[dia_destino].pop(posicion_destino)
                                        grupo[dia].insert(i, clase)

                        if mejora_encontrada:
                            break  # Salir del bucle de días destino si se encontró una mejora

                if mejora_encontrada:
                    break  # Salir del bucle de clases si se encontró una mejora

            if mejora_encontrada:
                break  # Salir del bucle de grupos si se encontró una mejora

        # Calcular la aptitud después de hacer cambios
        #cromosoma_A, cromosoma_B = poblacion_modificada[-1]  # Tomar los cromosomas del último individuo de la población
        #aptitud_final = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas, semestre)
        #print(f"Aptitud actual al terminar de hacer cambios: {aptitud_final}")

        poblacion_modificada.append((cromosoma_A, cromosoma_B))

        

    return poblacion_modificada




def crear_horario(opcion, semestre, horas_maximas):
    materias_semestre = opcion[semestre]
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    horario_dias = [[] for _ in range(5)]  # Lista para almacenar las materias por día

    for materia in materias_semestre:
        clases_materia = materias[materia]["Clases"]
        num_clases = len(clases_materia)

        # Permutación aleatoria de días, considerando el número de clases de la materia
        permutacion_dias = random.sample(range(5), k=num_clases)

        # Asignar clases a los días según la permutación
        for i, dia_indice in enumerate(permutacion_dias):
            horario_dias[dia_indice].append(clases_materia[i])

    # Permutar los valores de cada día
    horas_de_clases = [0] * 5  # Lista para almacenar las horas de clases por día
    for dia_index, clases_dia in enumerate(horario_dias):
        # Permutar las clases del día
        clases_permutadas = random.sample(clases_dia, k=len(clases_dia))

        # Sumar las horas de clases del día
        for clase in clases_permutadas:
            horas_de_clases[dia_index] += clase % 10

        # Actualizar la lista de clases del día
        horario_dias[dia_index] = clases_permutadas

    # Balancear las horas de clases
    materias_por_dia = {dia: set(clase // 10 for clase in clases) for dia, clases in zip(dias, horario_dias)}

    # *** Agregar contador y límite al bucle ***
    contador_iteraciones = 0
    limite_iteraciones = 20  # Define el límite de iteraciones
    while any(horas > horas_maximas for horas in horas_de_clases) and contador_iteraciones < limite_iteraciones:
        dia_sobrecargado = horas_de_clases.index(max(horas_de_clases))
        clases_dia = horario_dias[dia_sobrecargado]

        # Buscar un día con menos horas para transferir una clase
        dias_ordenados = sorted(range(5), key=lambda i: horas_de_clases[i])
        for dia_destino_index in dias_ordenados:
            horas_ultima_clase = clases_dia[-1] % 10
            if horas_de_clases[dia_destino_index] + horas_ultima_clase <= horas_maximas:
                materia_a_transferir = clases_dia[-1]
                materia_id = materia_a_transferir // 10

                if materia_id not in materias_por_dia[dias[dia_destino_index]]:
                    # Transferir la clase y actualizar las horas
                    horario_dias[dia_destino_index].append(materia_a_transferir)
                    horario_dias[dia_sobrecargado].pop()
                    horas_de_clases[dia_destino_index] += horas_ultima_clase
                    horas_de_clases[dia_sobrecargado] -= horas_ultima_clase

                    # Actualizar el diccionario de materias por día
                    materias_por_dia[dias[dia_destino_index]].add(materia_id)
                    materias_por_dia[dias[dia_sobrecargado]].remove(materia_id)
                    break
        contador_iteraciones += 1

    # *** Revisar si el bucle se detuvo por el límite ***
    if contador_iteraciones == limite_iteraciones:
        #print(f"Bucle infinito en crear_horario para {semestre}, {opcion}. Reiniciando el horario...")
        return crear_horario(opcion, semestre, horas_maximas)  # Volver a generar el horario

    # Agregar el número aleatorio al inicio  <<<--- Movido aquí
    for dia_index, clases_dia in enumerate(horario_dias):
        # Agregar un valor aleatorio al inicio
        horas_restantes = horas_maximas - horas_de_clases[dia_index]
        valor_aleatorio = random.randint(0, horas_restantes) if horas_restantes > 0 else 0
        clases_dia.insert(0, valor_aleatorio)

    # Crear el diccionario del horario con los días y las clases
    horario = {dia: clases for dia, clases in zip(dias, horario_dias)}

    return horario

def construir_matriz_horario(horario, horas_maximas):
    matriz = [[''] * 5 for _ in range(horas_maximas)]  # Inicializar la matriz con celdas vacías

    for dia_index, dia in enumerate(horario.keys()):
        clases_dia = horario[dia]
        hora_actual = 0  # *** Reiniciar hora_actual al principio del bucle ***
        for codigo_clase in clases_dia[1:]:
            materia_id = codigo_clase // 10
            horas = codigo_clase % 10
            for _ in range(horas):
                matriz[hora_actual][dia_index] = materia_id
                hora_actual += 1
                if hora_actual >= horas_maximas:
                    break  # Salir del bucle si se alcanza el límite de horas

    return matriz

def generar_matrices_horarios(individuo, horas_maximas):
    matrices_horarios = []
    for grupo in individuo:
        matriz_horario = construir_matriz_horario(grupo, horas_maximas)
        matrices_horarios.append(matriz_horario)
    return matrices_horarios

def calcular_frecuencias_asignaturas(matrices_horarios, horas_maximas):
    num_materias = len(materias)
    frecuencias_asignaturas = []
    for matrices_individuo in matrices_horarios:
        frecuencias_individuo = []  # Lista para las matrices de frecuencia de cada materia
        for materia_id in range(1, num_materias + 1):
            matriz_frecuencia = [[0] * 5 for _ in range(horas_maximas)]
            for matriz_grupo in matrices_individuo:
                for fila_index, fila in enumerate(matriz_grupo):
                    for columna_index, materia_actual in enumerate(fila):
                        if materia_actual == materia_id:
                            matriz_frecuencia[fila_index][columna_index] += 1
            frecuencias_individuo.append(matriz_frecuencia)
        frecuencias_asignaturas.append(frecuencias_individuo)
    return frecuencias_asignaturas

def calcular_suma_cuadrados(frecuencias_asignaturas):
    sumas_cuadrados = []
    for frecuencias_individuo in frecuencias_asignaturas:
        suma_cuadrados_individuo = 0
        for matriz_frecuencia in frecuencias_individuo:
            for fila in matriz_frecuencia:
                for valor in fila:
                    suma_cuadrados_individuo += valor**2
        sumas_cuadrados.append(suma_cuadrados_individuo)
    return sumas_cuadrados

def seleccion_por_permutacion(poblacion, sizePoblacion):
    indices_permutados = random.sample(range(sizePoblacion), sizePoblacion)
    parejas_cruce = [(poblacion[indices_permutados[i]], poblacion[indices_permutados[i+1]]) for i in range(0, sizePoblacion, 2)]
    return parejas_cruce

def cruce_alternado(padre1, padre2):
    hijo1 = []
    hijo2 = []

    for grupo_index in range(len(padre1)):
        grupo_padre1 = padre1[grupo_index]
        grupo_padre2 = padre2[grupo_index]

        hijo1_grupo = {}
        hijo2_grupo = {}

        for dia in grupo_padre1.keys():
            clases_padre1 = grupo_padre1[dia]
            clases_padre2 = grupo_padre2[dia]

            # Copiar el primer elemento (hora de inicio) de cada padre
            hijo1_grupo[dia] = [clases_padre1[0]]
            hijo2_grupo[dia] = [clases_padre2[0]]

            # Encontrar el tamaño mínimo de las listas de clases (sin el primer elemento)
            min_tamaño = min(len(clases_padre1) - 1, len(clases_padre2) - 1)

            # Cruce alternado desde el segundo elemento hasta el tamaño mínimo
            for j in range(1, min_tamaño + 1):  # Comenzar desde el índice 1
                if j % 2 == 0:
                    hijo1_grupo[dia].append(clases_padre1[j])
                    hijo2_grupo[dia].append(clases_padre2[j])
                else:
                    hijo1_grupo[dia].append(clases_padre2[j])
                    hijo2_grupo[dia].append(clases_padre1[j])

            # Agregar el resto de las clases del padre más largo (sin el primer elemento)
            hijo1_grupo[dia].extend(clases_padre1[min_tamaño + 1:])
            hijo2_grupo[dia].extend(clases_padre2[min_tamaño + 1:])

        hijo1.append(hijo1_grupo)
        hijo2.append(hijo2_grupo)



    return hijo1, hijo2
def eliminar_errores_cruce(horario):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    for grupo_index, grupo in enumerate(horario):
        for dia, clases_dia in grupo.items():

            # ----> Solución: Insertar 1 al inicio si es necesario <----
            if clases_dia[0] > 10:  # Si el primer valor es una clase...

                clases_dia.insert(0, 1)  # ... insertar 1 al inicio.

            # Verificar y eliminar clases incorrectas en el resto del día
            for i, clase in enumerate(clases_dia[1:]):
                if clase < 10:
                    #print(f"Error de cruce detectado en el día {dia} del grupo {grupo_index + 1}: clase {clase}")
                    del grupo[dia][i + 1]  # Eliminar la clase errónea (índice + 1)

    return horario
def eliminar_clases_repetidas(horario):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    for grupo_index, grupo in enumerate(horario):
        for dia, clases_dia in grupo.items():
            # Eliminar clases repetidas dentro del grupo y día
            clases_unicas = []
            for clase in clases_dia:
                if not any(clase_unica // 10 == clase // 10 for clase_unica in clases_unicas):
                    clases_unicas.append(clase)
            grupo[dia] = clases_unicas
    return horario
def ajustar_hora_inicio(horario, horas_maximas):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    for grupo_index, grupo in enumerate(horario):
        for dia, clases_dia in grupo.items():
            # Verificar y corregir exceso de horas en el día
            horas_dia = calcular_horas_de_clase_dia(clases_dia)
            if horas_dia > horas_maximas:
                #print(f"Ajuste de hora de inicio en el día {dia} del grupo {grupo_index + 1} debido a exceso de horas.")
                grupo[dia][0] = 0  # Ajustar la hora de inicio a cero
    return horario

def corregir_exceso_horas(horario, horas_maximas):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    for grupo_index, grupo in enumerate(horario):
        #print(f"Horario original del grupo {grupo_index + 1}: {grupo}")
        for dia in dias_semana:
            # 1. Calcular las horas totales del día
            horas_dia = calcular_horas_de_clase_dia(grupo[dia])

            # 2. Verificar el exceso de horas
            while horas_dia > horas_maximas:
                #print(horas_dia, horas_maximas)
                #print(f"Día con exceso de horas: {dia}, Clases: {grupo[dia]}")

                # 3. Seleccionar clase al azar para mover
                clase_a_mover = random.choice(grupo[dia][1:])

                # 4. Buscar día destino
                horas_de_clases = [calcular_horas_de_clase_dia(grupo[d]) for d in dias_semana]
                dias_ordenados = sorted(range(5), key=lambda i: horas_de_clases[i])
                dia_destino_encontrado = False
                for dia_destino_index in dias_ordenados:
                    if horas_de_clases[dia_destino_index] + clase_a_mover % 10 <= horas_maximas:  # Verificar que el día destino tenga espacio
                        materia_id = clase_a_mover // 10
                        clase_en_dia_destino = False
                        for clase_actual in grupo[dias_semana[dia_destino_index]][1:]:
                            if clase_actual // 10 == materia_id:
                                clase_en_dia_destino = True
                                break

                        if not clase_en_dia_destino:  # Verificar que la materia no esté en el día destino
                            # Mover la clase
                            grupo[dias_semana[dia_destino_index]].append(clase_a_mover)
                            # *** Asegurar que la clase está en el día antes de eliminar ***
                            if clase_a_mover in grupo[dia]:
                                grupo[dia].remove(clase_a_mover)
                            # *** Actualizar horas_de_clases ***
                            horas_de_clases = [calcular_horas_de_clase_dia(grupo[d]) for d in dias_semana]

                            # *** Imprimir las horas del día y el límite ***
                            #print(f"Horas del día {dia}: {calcular_horas_de_clase_dia(grupo[dia])}, Horas máximas: {horas_maximas}")

                            dia_destino_encontrado = True

                            # *** Verificar si se cumple la restricción ***
                            # *** Corregir el día de la verificación ***
                            horas_dia = calcular_horas_de_clase_dia(grupo[dia])
                            if calcular_horas_de_clase_dia(grupo[dias_semana[dia_destino_index]]) <= horas_maximas:
                                break  # Salir del bucle si la restricción se cumple

                # 5. Ajustar hora de inicio o intentar mover la clase de nuevo
                if not dia_destino_encontrado:
                    #print(f"No se encontró un día disponible, ajustando la hora de inicio en {dia}...")
                    grupo[dia][0] = 0  # Ajustar la hora de inicio a cero
                    horas_dia = calcular_horas_de_clase_dia(grupo[dia])  # Actualizar horas_dia
                    if horas_dia > horas_maximas:
                        #print(f"Ajustar la hora de inicio no fue suficiente, intentar mover la clase de nuevo...")
                        continue  # Volver a intentar mover la clase

            # 6. Chequear la hora de inicio
            horas_clase_dia = sum(c % 10 for c in grupo[dia][1:])  # Calcular las horas de clase en el día
            desfase = grupo[dia][0]  # Obtener el desfase (hora de inicio)
            total_horas = horas_clase_dia + desfase
            if total_horas > horas_maximas:
                # Ajustar la hora de inicio
                espacio_disponible = horas_maximas - horas_clase_dia-1  # Calcular el espacio disponible
                grupo[dia][0] = max(0,  espacio_disponible)
    return horario

def corregir_materias_repetidas(horario, horas_maximas):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    for grupo_index, grupo in enumerate(horario):
        #print(f"Horario original del grupo {grupo_index + 1}: {grupo}")
        for dia_index, dia in enumerate(dias_semana):
            #print(f"Día {dia}: {grupo[dia]}")
            # 1. Verificar si hay materias repetidas en el día
            materias_dia = [0] * (len(materias) + 1)
            for clase in grupo[dia]:
                if clase != 0:
                    materia_id = clase // 10
                    materias_dia[materia_id] += 1
            #print(materias_dia)
            if max(materias_dia) > 1:
                #print(f"ERROR: Materias repetidas en el día {dia}")
                # 2. Buscar otro día para mover la materia
                materia_repetida = materias_dia.index(max(materias_dia))  # Obtener el ID de la materia repetida
                dia_a_mover = dia_index
                # 3. Buscar la clase a mover y su posición
                clase_a_mover = None
                posicion_a_mover = None
                for i, clase in enumerate(grupo[dias_semana[dia_a_mover]]):
                    if clase // 10 == materia_repetida:
                        clase_a_mover = clase
                        posicion_a_mover = i
                        break

                dia_destino_encontrado = False
                for dia_destino_index in range(len(dias_semana)):
                    #print(f"dia_destino_index: {dia_destino_index}")
                    # 3. Buscar una materia para intercambiar
                    if dia_destino_index != dia_index:
                        # Buscar una materia que no esté en el día actual
                        materias_dia_destino = [0] * (len(materias) + 1)
                        for clase in grupo[dias_semana[dia_destino_index]]:
                            if clase != 0:
                                materia_id_destino = clase // 10
                                materias_dia_destino[materia_id_destino] += 1
                        # Verificar si la materia repetida no está presente en el día destino
                        if materias_dia_destino[materia_repetida] == 0:
                            # Buscar la clase a intercambiar en el día actual
                            clase_a_intercambiar = None
                            for i, clase in enumerate(grupo[dias_semana[dia_destino_index]]):
                                # Comparar la duración de la clase con la clase a mover
                                if clase % 10 == clase_a_mover % 10:
                                   if clase > 10:
                                      # Verificar si el ID de la materia a intercambiar no está presente en el día actual
                                      #print(materias_dia)
                                      #print(clase_a_mover)
                                      #print(clase)
                                      if materias_dia[clase// 10] == 0:
                                          clase_a_intercambiar = clase
                                          posicion_intercambio = i
                                          #print(clase_a_intercambiar,posicion_intercambio)
                                          break
                                      else:
                                          continue  # Buscar otra clase para intercambiar
                            # Definir clase_a_mover aquí, dentro del bucle
                            # Buscar la clase a mover en el día actual
                            if clase_a_intercambiar is not None:
                                # 5. Intercambiar las clases
                                # Intercambiar las clases en las posiciones correspondientes
                                grupo[dias_semana[dia_a_mover]][posicion_a_mover], grupo[dias_semana[dia_destino_index]][posicion_intercambio] = grupo[dias_semana[dia_destino_index]][posicion_intercambio], grupo[dias_semana[dia_a_mover]][posicion_a_mover]

                                #print(f"Se movió la clase {clase_a_mover} del día {dia} al día {dias_semana[dia_destino_index]}")
                                #print(f"Horario del grupo {grupo_index + 1} después de mover la clase {clase_a_mover}: {grupo}")
                                #print(f"Se movió la materia {materia_repetida} del día {dias_semana[dia_a_mover]} al día {dias_semana[dia_destino_index]}")
                                #print(f"Nuevo horario del grupo: {grupo}")
                                dia_destino_encontrado = True
                                break
                        else:
                            # Verificar si se llegó al viernes
                            if dia_destino_index == 4:
                                dia_destino_encontrado = True
                                break
                            else:
                                continue  # Buscar otro día destino

                if dia_destino_encontrado:
                    break

    return horario

def reparar_horario(horario, horas_maximas, padre1, padre2, opcion, semestre):

    horario = eliminar_errores_cruce(horario) #Repara la hora de inicio, y si hay una materia con codigo inferior a 10
    horario = eliminar_clases_repetidas(horario) #Elimina las clases, misma materia, repetidas en un mismo dia.

    horario = ajustar_hora_inicio(horario, horas_maximas)
    #horario = corregir_materias_repetidas(horario, horas_maximas)
    #horario = asegurar_cantidad_clases(horario, horas_maximas, opcion, semestre, padre1, padre2) #Obsoleta por reparar frecuencia
    #horario = ajustar_hora_inicio2(horario, horas_maximas)


    horario = reparar_frecuencia(horario, horas_maximas, padre1, padre2, opcion, semestre)
    horario = corregir_exceso_horas(horario, horas_maximas)
    #horario = reparar_frecuencia2(horario, horas_maximas, padre1, padre2, opcion, semestre)
    #horario = corregir_exceso_horas(horario, horas_maximas)


    return horario


def reparar_frecuencia(horario, horas_maximas, padre1, padre2, opcion, semestre):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    # Crear matrices de referencia para las opciones
    matrices_referencia = crear_matrices_referencia(opcion, semestre)

    # Crear matrices de conteo para el hijo
    matrices_conteo = crear_matrices_conteo(horario, semestre, matrices_referencia)

    # Detectar grupos con problemas de frecuencia
    grupos_con_problemas = []
    for clase_idx, fila in enumerate(matrices_conteo):  # Iterar sobre cada clase
        for grupo_idx in range(1, len(fila)):  # Iterar sobre cada grupo (desde el grupo 1 al grupo 22)
            if fila[grupo_idx] != matrices_referencia[clase_idx][1]:
                grupos_con_problemas.append((grupo_idx, clase_idx, matrices_referencia[clase_idx][1] - fila[grupo_idx]))


    # Corregir las frecuencias en los grupos con problemas
    for grupo_idx, clase_idx, diferencia in grupos_con_problemas:
        clase_con_problema = matrices_referencia[clase_idx][0]  # Obtener el código de la clase con problemas
        grupo = horario[grupo_idx - 2]



        if diferencia > 0:
          # Agregar la clase faltante al grupo
          for _ in range(diferencia):  # Se repite el bucle 'diferencia' veces
              clase_agregada = False
              for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
                  # Verificar si la clase ya está en el día
                  if not any(clase // 10 == clase_con_problema // 10 for clase in grupo[dia]):
                      # Verificar si cabe la clase, considerando el desfase
                      horas_dia = sum(c % 10 for c in grupo[dia][1:]) + grupo[dia][0]
                      if horas_dia + clase_con_problema % 10 <= horas_maximas:
                          # Agregar la clase al día
                          grupo[dia].append(clase_con_problema)
                          clase_agregada = True
                          break  # Se sale del bucle del día si se agregó la clase
                      else:
                          # Verificar si cabe la clase, ajustando el desfase a 0
                          if sum(c % 10 for c in grupo[dia][1:]) + clase_con_problema % 10 <= horas_maximas:
                              # Agregar la clase al día y ajustar el desfase

                              grupo[dia].append(clase_con_problema)
                              grupo[dia][0] = 0
                              clase_agregada = True
                              break  # Se sale del bucle del día si se agregó la clase
              if not clase_agregada:  # Si no se ha podido agregar la clase, agregarla en un día donde no esté la materia
                  for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
                      if not any(clase // 10 == clase_con_problema // 10 for clase in grupo[dia]):

                          grupo[dia].insert(1, clase_con_problema) # Se inserta en la posición 1 para no afectar la hora de inicio
                          break  # Se sale del bucle de días si se agregó la clase

        elif diferencia < 0:
            # Eliminar la clase sobrante del grupo
             for _ in range(abs(diferencia)):  # Se repite el bucle 'diferencia' veces
                clase_eliminada = False  # Variable booleana para controlar si se ha eliminado una clase
                for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
                    for i, clase in enumerate(grupo[dia]):
                        if clase == clase_con_problema:  # Se compara la clase completa

                            del grupo[dia][i]
                            clase_eliminada = True  # Se establece la variable en True si se ha eliminado una clase
                            break  # Se sale del bucle del día si se eliminó una clase
                    if clase_eliminada:
                        break  # Se sale del bucle de días si se eliminó una clase



    return horario




def asegurar_cantidad_clases(horario, horas_maximas, opcion, semestre, padre1, padre2):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    for grupo_index, grupo in enumerate(horario):
        # Obtener un diccionario con las clases requeridas y su cantidad
        clases_requeridas = {}
        for materia in opcion[semestre]:
            for clase in materias[materia]["Clases"]:
                clases_requeridas[clase] = clases_requeridas.get(clase, 0) + 1

        # Encontrar las clases faltantes y sobrantes en el grupo
        clases_presentes = {}
        for dia, clases_dia in grupo.items():
            for clase in clases_dia:
                clases_presentes[clase] = clases_presentes.get(clase, 0) + 1

        clases_faltantes = []
        clases_sobrantes = []
        for clase, cantidad_requerida in clases_requeridas.items():
            cantidad_presente = clases_presentes.get(clase, 0)
            diferencia = cantidad_requerida - cantidad_presente
            if diferencia > 0:
                clases_faltantes.extend([clase] * diferencia)
            elif diferencia < 0:
                clases_sobrantes.extend([clase] * abs(diferencia))

        #print("Clases faltantes en el grupo:", clases_faltantes)
        #print("Clases sobrantes en el grupo:", clases_sobrantes)

        # Eliminar clases sobrantes utilizando la información del padre 1
        for clase_sobrante in clases_sobrantes:
            # Crear vectores de presencia para el hijo y el padre
            presencia_hijo = [0] * 5
            presencia_padre = [0] * 5

            # Recorrer los días del hijo y del padre
            for dia_index, (clases_dia_hijo, clases_dia_padre) in enumerate(zip(grupo.values(), padre1[grupo_index].values())):
                if clase_sobrante in clases_dia_hijo:
                    presencia_hijo[dia_index] = 1
                if clase_sobrante in clases_dia_padre:
                    presencia_padre[dia_index] = 1

            # Encontrar días para eliminar la clase sobrante
            dias_para_eliminar = []
            for i in range(len(presencia_hijo)):
                if presencia_hijo[i] == 1 and presencia_padre[i] == 0:
                    dias_para_eliminar.append(dias_semana[i])

            # Eliminar clases sobrantes solo si hay sobrantes
            while dias_para_eliminar and clases_presentes.get(clase_sobrante, 0) > clases_requeridas.get(clase_sobrante, 0):  # Nueva condición
                dia_a_eliminar = random.choice(dias_para_eliminar)
                eliminar_clase_especifica(grupo, dia_a_eliminar, clase_sobrante)
                dias_para_eliminar.remove(dia_a_eliminar)
                clases_presentes[clase_sobrante] -= 1  # Actualizar la cantidad de clases presentes

        # Agregar clases faltantes utilizando la información del padre 1
        horas_por_dia = [sum(int(c) % 10 for c in clases[1:]) for clases in grupo.values()]
        for clase_faltante in clases_faltantes:
            # Crear vectores de presencia y horas disponibles para el hijo y el padre
            presencia_hijo = [0] * 5
            presencia_padre = [0] * 5
            horas_disponibles_hijo = [0] * 5
            posiciones_en_padre = [None] * 5

            # Recorrer los días del hijo y del padre
            for dia_index, (clases_dia_hijo, clases_dia_padre) in enumerate(zip(grupo.values(), padre1[grupo_index].values())):
                if clase_faltante in clases_dia_hijo:
                    presencia_hijo[dia_index] = 1
                if clase_faltante in clases_dia_padre:
                    presencia_padre[dia_index] = 1
                    # Buscar la posición de la clase faltante en el padre
                    for i, clase in enumerate(clases_dia_padre):
                        if int(clase) == clase_faltante:
                            posiciones_en_padre[dia_index] = i
                            break
                horas_disponibles_hijo[dia_index] = horas_maximas - sum(int(c) % 10 for c in clases_dia_hijo[1:])

            # Crear vectores de días posibles
            dias_con_clase_padre = []
            dias_sin_clase_padre = []
            for dia_index in range(5):
                if presencia_padre[dia_index] == 1:
                    dias_con_clase_padre.append(dia_index)
                else:
                    dias_sin_clase_padre.append(dia_index)

            random.shuffle(dias_con_clase_padre)
            random.shuffle(dias_sin_clase_padre)
            dias_posibles = dias_con_clase_padre + dias_sin_clase_padre

            # Intentar agregar la clase faltante
            clase_agregada = False
            for dia_index in dias_posibles:
                if presencia_hijo[dia_index] == 0 and horas_disponibles_hijo[dia_index] >= clase_faltante % 10:
                    dia = dias_semana[dia_index]
                    #print("dia", dia, "grupo", grupo_index)
                    if posiciones_en_padre[dia_index] is not None:
                        posicion_a_insertar = min(posiciones_en_padre[dia_index] + 1, len(grupo[dia]) - 1)
                        grupo[dia].insert(posicion_a_insertar, clase_faltante)
                    else:
                        posicion_a_insertar = random.randint(1, len(grupo[dia]))
                        grupo[dia].insert(posicion_a_insertar, clase_faltante)
                    presencia_hijo[dia_index] = 1
                    horas_disponibles_hijo[dia_index] -= clase_faltante % 10
                    clase_agregada = True
                    break

    return horario

# Función auxiliar para eliminar una clase específica de un día:
def eliminar_clase_especifica(grupo, dia, clase):
    for i, c in enumerate(grupo[dia]):
        if c == clase:
            del grupo[dia][i]
            return

def calcular_horas_de_clase_dia(clases_dia):
    """Calcula las horas totales de clase en un día.

    Args:
        clases_dia: Una lista que representa las clases de un día.

    Returns:
        El número total de horas de clase en el día.
    """
    return sum(int(c) % 10 for c in clases_dia[1:])  # Ignorar la hora de inicio






def generar_hijos(parejas_cruce, horas_maximas):
    hijos = []

    for padre1, padre2 in parejas_cruce:

        hijo1_dias, hijo2_dias = cruce_alternado(padre1, padre2)
        #print("\n padre1",padre1)
        #print("\n padre2",padre2)
        #print("\n hijo_dias1",hijo1_dias)
        #print("\n hijo_dias2",hijo2_dias)
        hijo1 = reparar_horario(hijo1_dias, horas_maximas)
        hijo2 = reparar_horario(hijo2_dias, horas_maximas)

        #print("\n hijo1",hijo1)
        #print("\n hijo2",hijo2)
        hijos.append(hijo1)
        hijos.append(hijo2)
    return hijos

def individuo_valido(individuo, horas_maximas, opcion, semestre):
    for grupo_index, grupo in enumerate(individuo):
        # Verificar si hay clases repetidas en un día
        for dia, clases_dia in grupo.items():
            if len(clases_dia) != len(set(clases_dia)):
                #print(f"Individuo inválido: Clases repetidas en el día {dia} del grupo {grupo_index+1}: {clases_dia}")
                return 0

        # Obtener un diccionario con las clases requeridas (ID y horas) y su cantidad
        clases_requeridas = {}
        for materia in opcion[semestre]:
            for clase in materias[materia]["Clases"]:
                materia_id = clase // 10
                horas = clase % 10
                clases_requeridas[(materia_id, horas)] = clases_requeridas.get((materia_id, horas), 0) + 1

        # Contar las clases presentes en el grupo
        clases_presentes = {}
        for dia, clases_dia in grupo.items():
            for clase in clases_dia:
                materia_id = clase // 10
                horas = clase % 10
                clases_presentes[(materia_id, horas)] = clases_presentes.get((materia_id, horas), 0) + 1

        # Verificar si faltan o sobran clases
        for (materia_id, horas), cantidad_requerida in clases_requeridas.items():
            if clases_presentes.get((materia_id, horas), 0) != cantidad_requerida:
                #print(f"Individuo inválido: Cantidad incorrecta de clases de {materia_id * 10 + horas} en el grupo {grupo_index+1}")
                #print(f"Semana: {grupo}")
                return 0

        # Verificar si se excede el límite de horas por día
        for dia, clases_dia in grupo.items():
            horas_dia = sum(c % 10 for c in clases_dia[1:])  # Sumar las horas directamente
            if horas_dia > horas_maximas:
                #print(f"Individuo inválido: Exceso de horas ({horas_dia}) en el día {dia} del grupo {grupo_index+1}")
                #print(f"Semana: {grupo}")
                return 0

    return 1  # El individuo es válido



def construir_diccionario_asignaturas(individuo, horas_maximas):
    """
    Construye un diccionario que asocia cada ID de asignatura
    con una lista de vectores, donde cada vector contiene los índices
    de esa asignatura para un grupo, considerando todos los días.

    Args:
        individuo: Un individuo de la población (lista de diccionarios).
        horas_maximas: El número máximo de horas en un día.

    Returns:
        Un diccionario donde la clave es el ID de la asignatura y
        el valor es una lista de vectores de índices.
    """
    num_asignaturas = len(materias) + 1
    diccionario_asignaturas = {i: [[] for _ in range(len(individuo))] for i in range(num_asignaturas)}

    for grupo_index, grupo in enumerate(individuo):
        #print(grupo)
        for dia_index, dia in enumerate(grupo):  # Iterar sobre los días de la semana
            horario_dia = grupo[dia]
            hora_inicio = horario_dia[0]
            for i in range(1, len(horario_dia)):
                asignatura = horario_dia[i]
                if asignatura:
                    id_asignatura = asignatura // 10
                    indice =  hora_inicio + i  + (dia_index * horas_maximas)
                    diccionario_asignaturas[id_asignatura][grupo_index].append(indice)

    return diccionario_asignaturas




import random

def corregir_exceso_horas(horario, horas_maximas):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    for grupo_index, grupo in enumerate(horario):
        #print(f"Horario original del grupo {grupo_index + 1}: {grupo}")
        for dia_index, dia in enumerate(dias_semana):
            # 1. Calcular el desbalance del día
            horas_dia = calcular_horas_de_clase_dia(grupo[dia])
            desbalance = horas_dia - horas_maximas
            #print(f"Día {dia}: Desbalance {desbalance}")

            # 2. Verificar si el día se puede ajustar con la hora de inicio
            if desbalance <= 0:  # No hay exceso de horas
                continue

            # 3. Ajustar la hora de inicio si es posible
            if sum(c % 10 for c in grupo[dia][1:]) <= horas_maximas:
                grupo[dia][0] = horas_maximas - sum(c % 10 for c in grupo[dia][1:])
                #print(f"Se ajustó la hora de inicio del día {dia} a {grupo[dia][0]}.")
                # Actualizar y mostrar desbalance después de ajustar la hora de inicio
                desbalance = calcular_horas_de_clase_dia(grupo[dia]) - horas_maximas
                #print(f"Desbalance del día {dia}: {desbalance}")
                continue

            # 4. Verificar si el día tiene exceso de horas
            if desbalance > 0:  # Hay exceso de horas
                # 4. Recorrer las clases del día con exceso de horas
                for i in range(len(grupo[dia]) - 1, -1, -1):  # Recorrer al revés
                    clase = grupo[dia][i]
                    #print(f"Clase: {clase}")

                    # Se recalcula el desbalance del día antes de buscar un día destino
                    horas_dia = calcular_horas_de_clase_dia(grupo[dia])
                    desbalance = horas_dia - horas_maximas
                    #print(f"Día {dia}: Desbalance {desbalance}")

                    # Se verifica si el día tiene exceso de horas para realizar el cambio
                    if desbalance > 0:
                        # 5. Buscar un día destino
                        for dia_destino_index in range(len(dias_semana)):
                            if dia_destino_index == dia_index:
                                continue

                            # Se recalcula el desbalance del día antes de buscar un día destino
                            horas_dia = calcular_horas_de_clase_dia(grupo[dia])
                            desbalance = horas_dia - horas_maximas
                            #print(f"Día {dia}: Desbalance {desbalance}")

                            # Se verifica si el día tiene exceso de horas para realizar el cambio
                            if desbalance > 0:

                                # 1. Calcular el desbalance del día destino
                                desbalance_destino = calcular_horas_de_clase_dia(grupo[dias_semana[dia_destino_index]]) - horas_maximas
                                #print(f"Desbalance del día {dias_semana[dia_destino_index]}: {desbalance_destino}")

                                # 2. Verificar si el día destino tiene exceso de horas
                                if desbalance_destino > 0:
                                    #print(f"El día {dias_semana[dia_destino_index]} ya tiene exceso de horas.")
                                    continue

                                # 3. Verificar si la asignatura ya está en el día destino
                                if clase // 10 in [c // 10 for c in grupo[dias_semana[dia_destino_index]][1:]]:
                                    #print(f"La asignatura ya está en el día {dias_semana[dia_destino_index]}.")
                                    continue

                                # 5.1 Si el desbalance del día destino es menor o igual a cero (hay espacio para la clase):
                                if desbalance_destino + clase % 10  <= 0:
                                    #print(f"Se encontró un día destino: {dias_semana[dia_destino_index]}.")
                                    # Mover la clase
                                    grupo[dias_semana[dia_destino_index]].append(clase)
                                    # Eliminar la clase del día de origen
                                    #print(i,grupo[dia])
                                    grupo[dia].pop(i)
                                    # Ajustar la hora de inicio del día destino a 0
                                    grupo[dias_semana[dia_destino_index]][0] = 0
                                    # Ajustar la hora de inicio del día de origen a 0
                                    grupo[dia][0] = 0

                                    # Actualizar y mostrar desbalance después del movimiento
                                    #print(f"Desbalance del día {dia}: {calcular_horas_de_clase_dia(grupo[dia]) - horas_maximas}")
                                    #print(f"Desbalance del día {dias_semana[dia_destino_index]}: {calcular_horas_de_clase_dia(grupo[dias_semana[dia_destino_index]]) - horas_maximas}")

                                    # Verificar si el día de origen ya cumple con las horas máximas
                                    if calcular_horas_de_clase_dia(grupo[dia]) <= horas_maximas:
                                        #print(f"El día {dia} cumple con el límite de horas.")
                                        break  # Salir del bucle de días destino

                                    # Ajustar el índice i (se restó 1 a la i)
                                    # i -= 1
                                    break  # Salir del bucle de días destino

                                # 5.2 Si no se encontró un día destino válido, intentar intercambiar la clase
                                else:
                                    #print(f"No se encontró un día destino para mover {clase}, intentando intercambiar.")
                                    # Ajustar la hora de inicio del día destino a 0
                                    grupo[dias_semana[dia_destino_index]][0] = 0
                                    # Verificar que la lista del día destino no esté vacía
                                    if len(grupo[dias_semana[dia_destino_index]]) > 1:
                                        # Iterar sobre la lista del día destino
                                        for j, clase_destino in enumerate(grupo[dias_semana[dia_destino_index]][1:]):
                                            if clase_destino // 10 in [c // 10 for c in grupo[dia][1:]]:
                                                #print(f"La asignatura ya está en el día {dia}.")
                                                continue

                                            # Calcular el desbalance resultante
                                            desbalance_origen = calcular_horas_de_clase_dia(grupo[dia]) - clase % 10 + clase_destino % 10 - horas_maximas
                                            desbalance_destino = calcular_horas_de_clase_dia(grupo[dias_semana[dia_destino_index]]) + clase % 10 - clase_destino % 10 - horas_maximas
                                           # print(f"Desbalance del día {dia}: {desbalance_origen}")
                                           # print(f"Desbalance del día {dias_semana[dia_destino_index]}: {desbalance_destino}")

                                            # Intercambiar las clases
                                            if desbalance_origen <= 0 and desbalance_destino <= 0:
                                               # print(f"Se encontró una clase para intercambiar: {clase_destino}.")
                                                # Verificar que j sea un índice válido antes de acceder a la lista
                                                if j < len(grupo[dias_semana[dia_destino_index]]):
                                                 #   print(j,grupo[dias_semana[dia_destino_index]])
                                                 #   print(i,grupo[dia])
                                                    grupo[dias_semana[dia_destino_index]][j + 1], grupo[dia][i] = grupo[dia][i], grupo[dias_semana[dia_destino_index]][j + 1]
                                                    # Ajustar la hora de inicio de ambos días a 0
                                                    grupo[dia][0] = 0
                                                    grupo[dias_semana[dia_destino_index]][0] = 0

                                                    # Actualizar y mostrar desbalance después del intercambio
                                                #    print(f"Desbalance del día {dia}: {calcular_horas_de_clase_dia(grupo[dia]) - horas_maximas}")
                                                #    print(f"Desbalance del día {dias_semana[dia_destino_index]}: {calcular_horas_de_clase_dia(grupo[dias_semana[dia_destino_index]]) - horas_maximas}")

                                                    break  # Salir del bucle de intercambio
                                                else:
                                                    j=j
                                                    #print(f"El índice {j} es inválido para la lista {dias_semana[dia_destino_index]}.")
                                            else:
                                                j=j
                                                #print(f"No se pudo intercambiar {clase} con {clase_destino}.")
                            else:
                                j=j
                                #print(f"El día {dias_semana[dia_destino_index]} está vacío.")
            # Se verifica si el día cumple con las horas máximas después de mover o intercambiar clases
            # 1. Calcular el desbalance del día
            horas_dia = calcular_horas_de_clase_dia(grupo[dia])
            desbalance = horas_dia - horas_maximas
           # print(f"Día {dia}: Desbalance {desbalance}")

            # 2. Verificar si el día se puede ajustar con la hora de inicio
            if desbalance <= 0:  # No hay exceso de horas
                continue

        #print(f"Horario reparado del grupo {grupo_index + 1}: {grupo}")

    return horario

def calcular_horas_de_clase_dia(clases_dia):
    """Calcula las horas totales de clase en un día, considerando la hora de inicio.

    Args:
        clases_dia: Una lista que representa las clases de un día.

    Returns:
        El número total de horas de clase en el día.
    """
    return sum(int(c) % 10 for c in clases_dia[1:]) + clases_dia[0]  # Sumar la hora de inicio


def cruce_alternado_dos_cromosomas(padre1_A, padre1_B, padre2_A, padre2_B):
  """
  Realiza el cruce alternado entre dos pares de cromosomas.

  Args:
      padre1_A: Cromosoma A del primer padre.
      padre1_B: Cromosoma B del primer padre.
      padre2_A: Cromosoma A del segundo padre.
      padre2_B: Cromosoma B del segundo padre.

  Returns:
      Una tupla con cuatro elementos: hijo1_A, hijo2_A, hijo1_B, hijo2_B.
  """

  # 1. Realizar el cruce entre padre1_A y padre2_A
  hijo1_A, hijo2_A = cruce_alternado(padre1_A, padre2_A)  # ¡Reutilizamos la función original!

  # 2. Realizar el cruce entre padre1_B y padre2_B
  hijo1_B, hijo2_B = cruce_alternado(padre1_B, padre2_B)  # ¡Reutilizamos la función original!

  return hijo1_A, hijo2_A, hijo1_B, hijo2_B

def generar_hijos_dos_cromosomas(parejas_cruce, horas_maximas, opcion_A, opcion_B, semestre):
    """
    Genera hijos a partir de parejas de padres con dos cromosomas.

    Args:
        parejas_cruce: Lista de tuplas con las parejas de padres.
        horas_maximas: Número máximo de horas por día.
        opcion_A: Diccionario con la información de la Opción A.
        opcion_B: Diccionario con la información de la Opción B.
        semestre: El semestre actual (ej. "Semestre1").

    Returns:
        Una lista con los hijos generados y reparados.
    """
    hijos = []
    for (padre1_A, padre1_B), (padre2_A, padre2_B) in parejas_cruce:
        # Realizamos el cruce
        hijo1_A, hijo2_A, hijo1_B, hijo2_B = cruce_alternado_dos_cromosomas(
            padre1_A, padre1_B, padre2_A, padre2_B
        )

        # Reparamos los hijos
        hijo1_A = reparar_horario(hijo1_A, horas_maximas, padre1_A, padre2_A, opcion_A, semestre)
        hijo2_A = reparar_horario(hijo2_A, horas_maximas, padre2_A, padre1_A, opcion_A, semestre)
        hijo1_B = reparar_horario(hijo1_B, horas_maximas, padre1_B, padre2_B, opcion_B, semestre)
        hijo2_B = reparar_horario(hijo2_B, horas_maximas, padre2_B, padre1_B, opcion_B, semestre)

        # Agregamos los hijos reparados a la lista
        hijos.append((hijo1_A, hijo1_B))
        hijos.append((hijo2_A, hijo2_B))

    return hijos




import csv
import os 

def exportar_horarios_csv(poblacion, mejores_aptitudes, aptitudes_poblacion, horas_maximas, semestre, nombre_archivo="horarios.csv"):
    """Exporta el mejor horario de la población a un archivo CSV y a Google Drive."""
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    mejor_individuo_index = aptitudes_poblacion.index(min(aptitudes_poblacion))  # Encontrar el índice del mejor individuo de la población actual
    mejor_individuo = poblacion[mejor_individuo_index]

    # ----> Guardar en Google Drive <----
    
    # Obtener la ruta de la carpeta Descargas
    ruta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
    ruta_archivo_descargas = os.path.join(ruta_descargas, nombre_archivo)


    ruta_archivo_drive = '/content/drive/My Drive/' + nombre_archivo

    with open(ruta_archivo_descargas, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=';')


        # Escribir información del mejor individuo
        escritor_csv.writerow([f"Mejor Individuo:", f"Individuo {mejor_individuo_index + 1}"])
        escritor_csv.writerow([f"Aptitud:", aptitudes_poblacion[mejor_individuo_index]])  # Usa la aptitud del mejor individuo

        # ----> Calcular choques por asignatura del mejor individuo <----
        choques_por_asignatura = calcular_choques_asignaturas(mejor_individuo[0], mejor_individuo[1], horas_maximas)

        # ---->  Imprimir choques por asignatura  <----
        for nombre_materia, choques in choques_por_asignatura.items():
            escritor_csv.writerow([f"{nombre_materia}: {choques}"])

        escritor_csv.writerow([])

        # ---->  Resto del código (sin cambios) <----
        for cromosoma, opcion_str in zip(mejor_individuo, ["Opcion A", "Opcion B"]):
            escritor_csv.writerow([f"Cromosoma: {opcion_str}"])

            # Obtener el diccionario correcto
            opcion = OpcionA if opcion_str == "Opcion A" else OpcionB

            # Validación del cromosoma
            es_valido = individuo_valido(cromosoma, horas_maximas, opcion, semestre)
            escritor_csv.writerow([f"Validación: {'Válido' if es_valido else 'Inválido'}"])

            escritor_csv.writerow(["Grupo"] + dias_semana * sizeGruposMatutinos)

            # ----> Crear matrices de horario para cada grupo <----
            matrices_grupo = [generar_matriz_horario(grupo, horas_maximas) for grupo in cromosoma]

            # ----> Escribir las matrices de horario <----
            for hora in range(horas_maximas):
                fila = [f"Hora {hora + 1}"]
                for matriz in matrices_grupo:
                    for dia_index, dia in enumerate(dias_semana):
                        materia_id = matriz[hora][dia_index]
                        if materia_id:
                            # Eliminar la multiplicación por 10
                            fila.append(materia_id)
                        else:
                            fila.append("")
                escritor_csv.writerow(fila)

            # ---->  Escribir los genes <----
            for j in range(sizeGruposMatutinos):
                fila_genes = [f"Gen Grupo {j + 1}"]
                # Agregar cada código de clase del vector como un elemento separado
                for dia in dias_semana:
                    for codigo_clase in cromosoma[j][dia]:
                        fila_genes.append(codigo_clase)
                escritor_csv.writerow(fila_genes)

            escritor_csv.writerow([])

        # ----> Escribir aptitudes de la población <----
        escritor_csv.writerow(["Aptitudes Generaciones"] + mejores_aptitudes)
        escritor_csv.writerow(["Aptitudes Poblacion"] + aptitudes_poblacion)

def imprimir_cromosomas_csv(poblacion, nombre_archivo="cromosomas.csv"):
    """Imprime los dos primeros cromosomas de cada individuo en un archivo CSV.

    Args:
        poblacion: Lista de tuplas con los cromosomas de la población.
        nombre_archivo:  Nombre del archivo CSV de salida.
    """
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(["Individuo", "Cromosoma A", "Cromosoma B"])

        for i, (cromosoma_A, cromosoma_B) in enumerate(poblacion):
            escritor_csv.writerow([i + 1, cromosoma_A, cromosoma_B])  # Imprimimos los dos primeros


def calcular_choques_asignaturas(cromosoma_A, cromosoma_B, horas_maximas):
    """Calcula la cantidad de asignaturas que chocan en cada cromosoma."""
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    num_materias = len(materias)+1

    # Inicializar el vector de choques
    choques_por_asignatura = {nombre_materia: [0] * (len(cromosoma_A) + len(cromosoma_B)) for nombre_materia in materias.keys()}

    # ----> Crear matrices para cada asignatura y grupo <----
    matrices_asignaturas = {}
    # Crear la relación entre los códigos de clase y el nombre de la materia
    relacion_codigos_materias = {}
    for nombre_materia in materias.keys():
        for codigo_clase in materias[nombre_materia]["Clases"]:
            relacion_codigos_materias[codigo_clase // 10] = nombre_materia

    # Crear las matrices de horario para cada grupo
    #print("Crear las matrices de horario para cada grupo")
    matrices_horario = []
    for cromosoma in [cromosoma_A, cromosoma_B]:
        for grupo_idx, grupo in enumerate(cromosoma):
            matriz_horario = generar_matriz_horario(grupo, horas_maximas)
            # Dividir los códigos de clase por 10 y tomar la parte entera
            for hora in range(horas_maximas):
                for dia in range(5):
                    if matriz_horario[hora][dia] != '':
                        matriz_horario[hora][dia] = matriz_horario[hora][dia] // 10
            matrices_horario.append(matriz_horario)

    #print("MATRICES")
    #print(horas_maximas,  matrices_horario)
    # ---->  Comparar matrices para detectar choques  <----
    for i in range(len(matrices_horario) - 1):
        # Inicializar el vector de choques para la materia i
        vector_choques_materia = [0] * num_materias  # Vector para contar choques de la materia i
        for j in range(i + 1, len(matrices_horario)):
            vector_choques_materia = [0] * num_materias  # Vector para contar choques de la materia i
            # Recorrer las horas y los días
            for hora in range(horas_maximas):
                for dia in range(5):
                    # Verificar si hay un choque en la misma hora y día
                    if matrices_horario[i][hora][dia] != '' and matrices_horario[j][hora][dia] != '' and matrices_horario[i][hora][dia] == matrices_horario[j][hora][dia]:
                        # Marcar el choque
                        vector_choques_materia[matrices_horario[i][hora][dia]] = 1


            # Actualizar los choques_por_asignatura al final de la comparación con todos los grupos
            #print(i,j,vector_choques_materia,matrices_horario[i],matrices_horario[j])
            #print(cromosoma_A, cromosoma_B)

            for k in range(len(vector_choques_materia)):
                if vector_choques_materia[k] == 1:

                    nombre_materia = relacion_codigos_materias[k]  # Obtener el nombre de la materia
                    choques_por_asignatura[nombre_materia][i] += 1  # Incrementar el contador de choques
                    choques_por_asignatura[nombre_materia][j] += 1

    #print("CHOQUES")
    #print(choques_por_asignatura)
    return choques_por_asignatura

def calcular_penalizacion_preferencias(cromosoma_A, cromosoma_B, horas_maximas):
    """Calcula la penalización por clases fuera de las horas preferidas."""
    penalizacion = 0
    turno = "Matutino" if horas_maximas == 7 else "Vespertino"
    turno = "Vespertino"

    for cromosoma in [cromosoma_A, cromosoma_B]:
        for grupo in cromosoma:
            for dia in grupo:
                clases_dia = grupo[dia]
                hora_actual = clases_dia[0]  # Hora de inicio
                for i in range(1, len(clases_dia)):
                    clase = clases_dia[i]
                    materia_id = clase // 10
                    nombre_materia = list(materias.keys())[materia_id - 1]

                    # Calcular la hora actual sumando las horas de la clase anterior
                    for _ in range(clase % 10):
                        # Verificar si la hora está penalizada en las preferencias
                        penalizacion += preferencias[nombre_materia][turno][hora_actual]
                        hora_actual = (hora_actual + 1) % horas_maximas

    return penalizacion

def calcular_penalizacion_primera_ultima_hora(horario, semestre):
    """Calcula la penalización por clases que no son la primera o última del día.

    Args:
        horario: Un horario (cromosoma).
        semestre: El semestre actual.

    Returns:
        La cantidad de veces que la materia no se da en la primera o última hora del día.
    """
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    penalizacion = 0

    for nombre_materia in primera_ultima_hora[semestre]:  # Recorre las materias para el semestre
        for grupo in horario:  # Recorre cada grupo
            for dia in dias_semana:
                codigos_clase_dia = grupo[dia]
                for codigo_clase in codigos_clase_dia:  # Recorre los códigos de la clase en el día
                    if codigo_clase // 10 in [c // 10 for c in materias[nombre_materia]["Clases"]]:  # Verifica si es la misma materia
                        # Busca la posición de la clase en el día
                        indice_clase = codigos_clase_dia.index(codigo_clase)
                        if indice_clase != 1 and indice_clase != len(codigos_clase_dia) - 1:  # Verifica si no es la primera ni la última
                            penalizacion += 1

    return penalizacion

def calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas,semestre):
    """Calcula la aptitud de un individuo..."""
    num_materias = len(materias)

    choques_por_asignatura = calcular_choques_asignaturas(cromosoma_A, cromosoma_B,  horas_maximas)
    penalizacion_preferencias = calcular_penalizacion_preferencias(cromosoma_A, cromosoma_B, horas_maximas)

    # Calcular la penalización por primera o última hora
    penalizacion_primera_ultima = calcular_penalizacion_primera_ultima_hora(cromosoma_A, semestre)
    penalizacion_primera_ultima += calcular_penalizacion_primera_ultima_hora(cromosoma_B, semestre)

    # ---->  Calcular la penalización de horas mínimas  <----
    penalizacion_horas_minimas = calcular_penalizacion_horas_minimas(cromosoma_A, cromosoma_B)

    # ---->  Calcular la suma de cuadrados de los choques <----
    choques_asignaturas = sum(sum(choque ** 2 for choque in choques_materia) for choques_materia in choques_por_asignatura.values())

    # ----> Calcular penalización por exceder la capacidad por hora <----
    penalizacion_exceso_capacidad = calcular_penalizacion_exceso_capacidad(cromosoma_A, cromosoma_B, horas_maximas)

    # Calcular la penalización por incumplir la separación mínima
    penalizacion_separacion = calcular_penalizacion_separacion(cromosoma_A, cromosoma_B, semestre)

    # ----> Calcular penalización por no cumplir la regla de primera o última hora <----
    penalizacion_primera_ultima_posicion = calcular_penalizacion_primera_ultima(cromosoma_A, cromosoma_B, semestre)


    aptitud = (
            (penalizacion_primera_ultima * 100000000000000)
            + (choques_asignaturas * 1000)
            + penalizacion_preferencias
            + (penalizacion_horas_minimas * 100)
            + penalizacion_exceso_capacidad *  110000000000000
            + (penalizacion_separacion * 900000000000)
            + (penalizacion_primera_ultima_posicion * 1000000000000000000)
            
        )


    #print(f"Choques : {choques_por_asignatura}")
    #print(f"Aptitud del individuo: {aptitud}" )

    return aptitud

def calcular_penalizacion_horas_minimas(cromosoma_A, cromosoma_B):
    """
    Calcula la penalización por no cumplir con las horas mínimas en todos los grupos de los dos cromosomas.

    Args:
        cromosoma_A: El cromosoma A del individuo.
        cromosoma_B: El cromosoma B del individuo.

    Returns:
        La penalización total por no cumplir con las horas mínimas.
    """
    penalizacion_total = 0
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    for cromosoma in [cromosoma_A, cromosoma_B]:
        for grupo in cromosoma:
            for dia in dias_semana:
                penalizacion_total += calcular_penalizacion_horas_minimas_grupo(grupo[dia])

    return penalizacion_total

def calcular_penalizacion_horas_minimas_grupo(grupo):
    """
    Calcula la penalización por no cumplir con las horas mínimas en un solo grupo (un día de la semana).

    Args:
        grupo: Un diccionario que representa un grupo (un día en la semana).

    Returns:
        La penalización del grupo.
    """
    horas_totales = sum(clase % 10 for clase in grupo[1:])  # Suma las horas de las clases (ignora la hora de inicio)
    penalizacion = 0
    if horas_totales < horas_minimas:
        penalizacion = (horas_minimas - horas_totales) * 10
        if horas_totales == 0:
          penalizacion = 0
        if horas_totales == 1:
          penalizacion = 2000
        if horas_totales == 2:
          penalizacion = 800
        penalizacion = penalizacion ** 2  # Eleva al cuadrado
    return penalizacion

import random

def es_hijo_valido(hijo_A, hijo_B, opcion_A, opcion_B, semestre):
    """
    Verifica si un hijo es válido.

    Args:
        hijo_A: Cromosoma A del hijo.
        hijo_B: Cromosoma B del hijo.
        opcion_A: Diccionario con la información de la Opción A.
        opcion_B: Diccionario con la información de la Opción B.
        semestre: El semestre actual (ej. "Semestre1").

    Returns:
        True si el hijo es válido, False si el hijo es inválido.
    """
    # ---->  Crear matrices de referencia para las opciones  <----
    matrices_referencia_A = crear_matrices_referencia(opcion_A, semestre)
    matrices_referencia_B = crear_matrices_referencia(opcion_B, semestre)

    #print("matrices_referencia_A")
    #print(matrices_referencia_A)
    #print("matrices_referencia_B")
    #print(matrices_referencia_B)


    # ---->  Crear matrices de conteo para el hijo  <----
    matrices_conteo_A = crear_matrices_conteo(hijo_A, semestre, matrices_referencia_A)
    matrices_conteo_B = crear_matrices_conteo(hijo_B, semestre, matrices_referencia_B)

    #print("matrices_conteo_A")
    #print(matrices_conteo_A)
    #print("matrices_conteo_B")
    #print(matrices_conteo_B)

    # ---->  Verificar validez de matrices_conteo_A  <----
    for i, fila in enumerate(matrices_conteo_A):
        # Obtener la segunda frecuencia
        segunda_frecuencia = fila[1]  # En Python, la columna 2 es el índice 1

        # Verificar si hay algún valor diferente a la segunda frecuencia después de la segunda columna
        if any(frecuencia != segunda_frecuencia for frecuencia in fila[2:]):
            # Obtener el código de clase
            codigo_clase = fila[0]

            # Buscar el grupo donde se encuentra la clase
            grupo_index = None
            for grupo_idx, grupo in enumerate(hijo_A):
                # Verificar si la clase está presente en el grupo
                if any(codigo_clase in grupo[dia] for dia in grupo):
                    grupo_index = grupo_idx
                    break

            if grupo_index is not None:
               #print(f"ERROR NO VALIDO: La clase {codigo_clase} tiene frecuencias incorrectas en Opcion A.")
                #print(f"Grupo {grupo_index + 1}: {hijo_A[grupo_index]}")
                return False
            else:
               # print(f"ERROR NO VALIDO: La clase {codigo_clase} tiene frecuencias incorrectas en Opcion A.")
                #print("No se encontró el grupo para la clase.")
                return False

    # ---->  Verificar validez de matrices_conteo_B  <----
    for i, fila in enumerate(matrices_conteo_B):
        # Obtener la segunda frecuencia
        segunda_frecuencia = fila[1]

        # Verificar si hay algún valor diferente a la segunda frecuencia después de la segunda columna
        if any(frecuencia != segunda_frecuencia for frecuencia in fila[2:]):
            # Obtener el código de clase
            codigo_clase = fila[0]

            # Buscar el grupo donde se encuentra la clase
            grupo_index = None
            for grupo_idx, grupo in enumerate(hijo_B):
                # Verificar si la clase está presente en el grupo
                if any(codigo_clase in grupo[dia] for dia in grupo):
                    grupo_index = grupo_idx
                    break

            if grupo_index is not None:
               #print(f"ERROR NO VALIDO: La clase {codigo_clase} tiene frecuencias incorrectas en Opcion B.")
               # print(f"Grupo {grupo_index + 1}: {hijo_B[grupo_index]}")
                return False
            else:
               # print(f"ERROR NO VALIDO: La clase {codigo_clase} tiene frecuencias incorrectas en Opcion B.")
               # print("No se encontró el grupo para la clase.")
                return False

    # Si se ha llegado a este punto, significa que no hay diferencias, el hijo es válido
    return True

def crear_matrices_referencia(opcion, semestre):
    """Crea una matriz de referencia con todos los códigos de clase y sus frecuencias, considerando el semestre y la opción."""
    codigos_clase_unicos = []
    frecuencias_codigos = []

    # Obtener las materias del semestre y la opción
    materias_semestre = opcion[semestre]

    # Agregar todas las clases al diccionario de frecuencias
    for nombre_materia in materias.keys():
        codigos_clase_materia = materias[nombre_materia]["Clases"]
        for codigo_clase in codigos_clase_materia:
            if codigo_clase not in codigos_clase_unicos:
                codigos_clase_unicos.append(codigo_clase)
                frecuencias_codigos.append(0)  # Inicializar frecuencia en 0

    # Contar las frecuencias solo para las materias del semestre
    for nombre_materia in materias_semestre:
        codigos_clase_materia = materias[nombre_materia]["Clases"]
        for codigo_clase in codigos_clase_materia:
            frecuencias_codigos[codigos_clase_unicos.index(codigo_clase)] += 1

    # Crear la matriz de referencia
    matriz_referencia = [[codigo_clase, frecuencia] for codigo_clase, frecuencia in zip(codigos_clase_unicos, frecuencias_codigos)]

    #print("REFERENCIA")
    #print(matriz_referencia)
    return matriz_referencia

def crear_matrices_conteo(hijo, semestre, matrices_referencia):
    """
    Crea matrices de conteo para un hijo dado y las agrega a las matrices de referencia.

    Args:
        hijo: Un hijo de la población (lista de diccionarios).
        semestre: El semestre actual (ej. "Semestre1").
        matrices_referencia: La matriz de referencia a la que se agregarán las columnas de conteo.

    Returns:
        La matriz de referencia con las columnas de conteo agregadas.
    """
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    # Crear la lista de conteo
    num_grupos = len(hijo)
    matriz_conteo = [[] for _ in range(num_grupos)]  # Lista: grupos

    # Rellenar la lista de conteo
    for grupo_idx, grupo in enumerate(hijo):
        vector_codigos_clase = []

        for dia_idx, dia in enumerate(dias_semana):
            vector_codigos_clase.extend(grupo[dia])  # Extender el vector con la lista de clases del día
        matriz_conteo[grupo_idx] = vector_codigos_clase  # Asignar el vector al grupo correspondiente

    # Crear la matriz auxiliar para la referencia
    matrices_referencia_aux = [[0 for _ in range(len(matrices_referencia[0]) + num_grupos)] for _ in range(len(matrices_referencia))]

    # Copiar los valores de la matrices_referencia original a la auxiliar
    for i, fila in enumerate(matrices_referencia):
        for j, valor in enumerate(fila):
            matrices_referencia_aux[i][j] = valor

    # Agregar las columnas de conteo a la matriz de referencia auxiliar
    for i, fila in enumerate(matrices_referencia_aux):
        # Obtener el código de clase
        codigo_clase = fila[0]

        # Recorrer los grupos
        for grupo_idx in range(num_grupos):
            # Calcular la frecuencia del código de clase en el grupo actual
            frecuencia = 0
            for clase in matriz_conteo[grupo_idx]:
                if clase == codigo_clase:
                    frecuencia += 1

            # Asignar la frecuencia a la matriz auxiliar
            matrices_referencia_aux[i][len(matrices_referencia[0]) + grupo_idx] = frecuencia

    #print("CONTEO")
    #print(matriz_conteo)

    #print("REFERENCIA")
    #print(matrices_referencia)
    #print("REFERENCIA aux")
    #print(matrices_referencia_aux)

    #print("HIJO")
    #print(hijo)

    #print(f"Cantidad de grupos en el hijo: {num_grupos}")

    return matrices_referencia_aux

def eliminar_hijos_invalidos2(hijos, opcion_A, opcion_B, semestre):
    """
    Elimina los hijos inválidos de la lista de hijos.
    """
    hijos_validos = []
    for hijo in hijos:
        # Validar ambos cromosomas
        if es_hijo_valido(hijo[0], hijo[1], opcion_A, opcion_B, semestre):
            # Verificar si hay algún grupo que excede las horas máximas
            for grupo_idx, grupo in enumerate(hijo[0]):  # Verificar el cromosoma A
                horas_dia = sum(clase % 10 for clase in grupo["Lunes"][1:]) + grupo["Lunes"][0]
                if horas_dia > horas_maximas:
                    #print(f"ERROR NO VALIDO: Grupo {grupo_idx + 1} de Opcion A excede las horas máximas.")
                    #print(f"Horas del día: {horas_dia}")
                    #print(f"grupo: {grupo['Lunes']}")
                    break  # Salir del bucle del grupo si se encuentra un grupo inválido
                else:
                    # Verificar si hay asignaturas repetidas en el mismo día
                    for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
                        # Crear un vector para contar la frecuencia de las materias en el día actual
                        materias_dia = [0] * (len(materias) + 1)
                        for clase in grupo[dia]:
                            if clase != 0:
                                materia_id = clase // 10
                                materias_dia[materia_id] += 1

                        # Verificar si hay una materia con frecuencia mayor a 1
                        if max(materias_dia) > 1:
                            #print(f"ERROR NO VALIDO: Se repite una asignatura en el día {dia}.")
                           # print(grupo)
                            break
                    else:
                        # Si se ha llegado al final del bucle del día sin encontrar asignaturas repetidas, continuar con el siguiente grupo
                        continue
            else:
                # Si se ha llegado al final del bucle del grupo sin encontrar un grupo inválido, continuar con el cromosoma B
                for grupo_idx, grupo in enumerate(hijo[1]):  # Verificar el cromosoma B
                    horas_dia = sum(clase % 10 for clase in grupo["Lunes"][1:]) + grupo["Lunes"][0]
                    if horas_dia > horas_maximas:
                        #print(f"ERROR NO VALIDO: Grupo {grupo_idx + 1} de Opcion B excede las horas máximas.")
                        #print(f"Horas del día: {horas_dia}")
                        #print(f"grupo: {grupo['Lunes']}")
                        break  # Salir del bucle del grupo si se encuentra un grupo inválido
                    else:
                        # Verificar si hay asignaturas repetidas en el mismo día
                        for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
                            # Crear un vector para contar la frecuencia de las materias en el día actual
                            materias_dia = [0] * (len(materias) + 1)
                            for clase in grupo[dia]:
                                if clase != 0:
                                    materia_id = clase // 10
                                    materias_dia[materia_id] += 1

                            # Verificar si hay una materia con frecuencia mayor a 1
                            if max(materias_dia) > 1:
                                #print(f"ERROR NO VALIDO: Se repite una asignatura en el día {dia}.")
                                #print(grupo)
                                break
                        else:
                            # Si se ha llegado al final del bucle del día sin encontrar asignaturas repetidas, agregar el hijo a la lista de hijos válidos
                            hijos_validos.append(hijo)
        else:
            print("ERROR NO VALIDO")

    #print("size",len(hijos_validos))
    return hijos_validos


def generar_matriz_horario(grupo, horas_maximas):
    """
    Genera la matriz de horario para un grupo, considerando la hora de inicio y la duración de las clases.

    Args:
        grupo: Un diccionario que contiene la información de las clases para cada día de la semana.
        horas_maximas: Número máximo de horas en el horario.

    Returns:
        Una matriz que representa el horario del grupo.
    """
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    # Inicializar la matriz de horario con ceros
    matriz_horario = [['' for _ in range(len(dias_semana))] for _ in range(horas_maximas)]

    # Rellenar la matriz de horario
    for dia_idx, dia in enumerate(dias_semana):
        hora_inicio = grupo[dia][0]  # Obtener la hora de inicio
        hora_actual = hora_inicio  # Inicializar la hora actual
        for codigo_clase in grupo[dia][1:]:  # Iterar por los códigos de clase del día
            duracion_clase = codigo_clase % 10  # Obtener la duración de la clase
            for _ in range(duracion_clase):
                if hora_actual < horas_maximas:  # Verificar que hora_actual esté dentro del rango
                    matriz_horario[hora_actual][dia_idx] = codigo_clase  # Asignar el código de clase a la celda
                hora_actual += 1

    #print("MATRIZ")
    #print(matriz_horario)

    return matriz_horario

def ajustar_hora_inicio2(horario, horas_maximas):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    for grupo_index, grupo in enumerate(horario):
        for dia in dias_semana:
            # Calcular las horas totales del día, incluyendo la hora de inicio
            horas_dia = sum(c % 10 for c in grupo[dia][1:]) + grupo[dia][0]

            # Verificar si se excede el límite de horas
            if horas_dia > horas_maximas:
                # Ajustar la hora de inicio a 0
                grupo[dia][0] = 0

    return horario

def eliminar_hijos_invalidos(hijos, opcion_A, opcion_B, semestre, horas_maximas):
    """
    Elimina los hijos inválidos de la lista de hijos.
    """
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    i = 0
    while i < len(hijos):
        hijo = hijos[i]
        # Validar ambos cromosomas
        if es_hijo_valido(hijo[0], hijo[1], opcion_A, opcion_B, semestre):
            # Verificar si hay algún grupo que excede las horas máximas en el cromosoma A
            for grupo_idx, grupo in enumerate(hijo[0]):
                horas_dia = sum(clase % 10 for clase in grupo["Lunes"][1:]) + grupo["Lunes"][0]
                if horas_dia > horas_maximas:
                    print(f"ERROR NO VALIDO: Grupo {grupo_idx + 1} de Opcion A excede las horas máximas.")
                    print(f"Horas del día: {horas_dia}")
                    print(f"grupo: {grupo}")
                    del hijos[i]
                    break  # Salir del bucle del grupo si se encuentra un grupo inválido
            else:
                # Verificar si hay algún grupo que excede las horas máximas en el cromosoma B
                for grupo_idx, grupo in enumerate(hijo[1]):
                    horas_dia = sum(clase % 10 for clase in grupo["Lunes"][1:]) + grupo["Lunes"][0]
                    if horas_dia > horas_maximas:
                        print(f"ERROR NO VALIDO: Grupo {grupo_idx + 1} de Opcion B excede las horas máximas.")
                        print(f"Horas del día: {horas_dia}")
                        print(f"grupo: {grupo}")
                        del hijos[i]
                        break  # Salir del bucle del grupo si se encuentra un grupo inválido
                # Verificar si hay asignaturas repetidas en el mismo día en el cromosoma A
                for grupo in hijo[0]:
                    for dia in dias_semana:
                        # Crear un vector para contar la frecuencia de las materias en el día actual
                        materias_dia = [0] * (len(materias) + 1)
                        for clase in grupo[dia]:
                            if clase != 0:
                                materia_id = clase // 10
                                materias_dia[materia_id] += 1

                        # Verificar si hay una materia con frecuencia mayor a 1
                        if max(materias_dia) > 1:
                            print(f"ERROR NO VALIDO: Se repite una asignatura en el día {dia} en Opcion A.")
                            print(grupo)
                            del hijos[i]
                            break
                    else:
                        continue  # Continuar al siguiente día si no se encontró una materia repetida
                    break # Salir del bucle de grupos si se encontró una materia repetida
                else:
                    # Verificar si hay asignaturas repetidas en el mismo día en el cromosoma B
                    for grupo in hijo[1]:
                        for dia in dias_semana:
                            # Crear un vector para contar la frecuencia de las materias en el día actual
                            materias_dia = [0] * (len(materias) + 1)
                            for clase in grupo[dia]:
                                if clase != 0:
                                    materia_id = clase // 10
                                    materias_dia[materia_id] += 1

                            # Verificar si hay una materia con frecuencia mayor a 1
                            if max(materias_dia) > 1:
                                print(f"ERROR NO VALIDO: Se repite una asignatura en el día {dia} en Opcion B.")
                                print(grupo)
                                del hijos[i]
                                break
                        else:
                            continue  # Continuar al siguiente día si no se encontró una materia repetida
                        break # Salir del bucle de grupos si se encontró una materia repetida
                    else:
                        # Si no se encontraron materias repetidas en ningún día en el cromosoma B, se incrementa i
                        i += 1
        else:
            print("ERROR NO VALIDO: Hijo no válido según es_hijo_valido")
            print(hijos[i])
            del hijos[i]

    #print("size",len(hijos))
    return hijos

def movimiento_mejora(individuo, horas_maximas,semestre,aptitud_ultimo_elite):
    """
    Realiza un movimiento de mejora en un individuo.

    Args:
        individuo: Una tupla con los dos cromosomas del individuo (Opción A y Opción B).
        horas_maximas: Número máximo de horas en el horario.

    Returns:
        El individuo modificado.
    """
    cromosoma_A, cromosoma_B = individuo
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    aptitud_anterior = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas,semestre)  # Calcular la aptitud inicial

    if aptitud_anterior >= aptitud_ultimo_elite:  # Si la aptitud no es mejor, no se realizan cambios
        return individuo

    aptitud_primera = aptitud_anterior
    mejora_encontrada = False

    # ----> Recorrer el cromosoma A <----
    for grupo_idx, grupo in enumerate(cromosoma_A):
        for dia_idx, dia in enumerate(dias_semana):
            if len(grupo[dia]) >= 3:  # Verificar si hay al menos 2 materias en el día
                for i in range(1, len(grupo[dia]) - 1):
                    for j in range(i + 1, len(grupo[dia])):
                        # Intercambiar las clases
                        grupo[dia][i], grupo[dia][j] = grupo[dia][j], grupo[dia][i]

                        # Calcular la aptitud del individuo
                        aptitud_actual = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas,semestre)

                        # Deshacer el intercambio si la aptitud no mejora
                        if aptitud_actual > aptitud_anterior:
                            grupo[dia][i], grupo[dia][j] = grupo[dia][j], grupo[dia][i]
                        else:
                            aptitud_anterior = aptitud_actual  # Actualizar la aptitud anterior si mejora
                            mejora_encontrada = True
                            break  # Salir del bucle si se encontró una mejora
                    if mejora_encontrada:
                        break  # Salir del bucle de 'i' si se encontró una mejora
                if mejora_encontrada:
                    break  # Salir del bucle de 'dia' si se encontró una mejora
        if mejora_encontrada:
            break  # Salir del bucle de 'grupo' si se encontró una mejora

    # ----> Recorrer el cromosoma B si no se encontró una mejora en el cromosoma A <----
    if not mejora_encontrada:
        for grupo_idx, grupo in enumerate(cromosoma_B):
            for dia_idx, dia in enumerate(dias_semana):
                if len(grupo[dia]) >= 3:  # Verificar si hay al menos 2 materias en el día
                    for i in range(1, len(grupo[dia]) - 1):
                        for j in range(i + 1, len(grupo[dia])):
                            # Intercambiar las clases
                            grupo[dia][i], grupo[dia][j] = grupo[dia][j], grupo[dia][i]

                            # Calcular la aptitud del individuo
                            aptitud_actual = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas,semestre)

                            # Deshacer el intercambio si la aptitud no mejora
                            if aptitud_actual > aptitud_anterior:
                                grupo[dia][i], grupo[dia][j] = grupo[dia][j], grupo[dia][i]
                            else:
                                aptitud_anterior = aptitud_actual  # Actualizar la aptitud anterior si mejora
                                mejora_encontrada = True
                                break  # Salir del bucle si se encontró una mejora
                        if mejora_encontrada:
                            break  # Salir del bucle de 'i' si se encontró una mejora
                    if mejora_encontrada:
                        break  # Salir del bucle de 'dia' si se encontró una mejora
                if mejora_encontrada:
                    break  # Salir del bucle de 'grupo' si se encontró una mejora

    return cromosoma_A, cromosoma_B


def aplicar_movimiento_mejora_poblacion(poblacion, horas_maximas,semestre,aptitud_ultimo_elite):
    """
    Aplica el movimiento de mejora a cada individuo de la población.

    Args:
        poblacion: Una lista de individuos.
        horas_maximas: Número máximo de horas en el horario.

    Returns:
        La población modificada.
    """
    poblacion_modificada = []
    for individuo in poblacion:
        individuo_modificado = movimiento_mejora(individuo, horas_maximas,semestre,aptitud_ultimo_elite)
        poblacion_modificada.append(individuo_modificado)

    return poblacion_modificada


def aplicar_movimiento_hora_inicio(poblacion, horas_maximas,semestre,aptitud_ultimo_elite):
    """
    Aplica el movimiento de mejora a cada individuo de la población.

    Args:
        poblacion: Una lista de individuos.
        horas_maximas: Número máximo de horas en el horario.

    Returns:
        La población modificada.
    """
    poblacion_modificada = []
    for individuo in poblacion:
        individuo_modificado = movimiento_hora_inicio(individuo, horas_maximas,semestre,aptitud_ultimo_elite)
        poblacion_modificada.append(individuo_modificado)

    return poblacion_modificada

def movimiento_hora_inicio(individuo, horas_maximas,semestre,aptitud_ultimo_elite):
    """
    Realiza un movimiento de mejora en un individuo.

    Args:
        individuo: Una tupla con los dos cromosomas del individuo (Opción A y Opción B).
        horas_maximas: Número máximo de horas en el horario.

    Returns:
        El individuo modificado.
    """
    cromosoma_A, cromosoma_B = individuo
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    aptitud_anterior = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas,semestre)  # Calcular la aptitud inicial
    mejora_encontrada = False

    if aptitud_anterior >= aptitud_ultimo_elite:  # Si la aptitud no es mejor, no se realizan cambios
        return individuo
    
    # ----> Recorrer el cromosoma A <----
    indices_grupos = list(range(len(cromosoma_A)))
    random.shuffle(indices_grupos)


    for i in indices_grupos:  # Recorrer en orden permutado
        grupo = cromosoma_A[i] 
        for dia_idx, dia in enumerate(dias_semana):
            # Calcular el desbalance del día
            horas_dia = sum(c % 10 for c in grupo[dia][1:])  # Eliminar grupo[dia][0]
            desbalance = horas_dia - horas_maximas
            if desbalance > 0:  # Verificar si hay un desbalance
                hora_inicio_original = grupo[dia][0]  # Guardar la hora de inicio original
                for hora_inicio_prueba in range(desbalance):
                    if hora_inicio_prueba != hora_inicio_original:  # Verificar que la nueva hora sea diferente
                        grupo[dia][0] = hora_inicio_prueba  # Probar una nueva hora de inicio
                        aptitud_actual = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas,semestre)
                        if aptitud_actual < aptitud_anterior:

                            mejora_encontrada = True
                            break
                    if mejora_encontrada:
                        break
                if not mejora_encontrada:
                    grupo[dia][0] = hora_inicio_original  # Restaurar la hora de inicio original
                if mejora_encontrada:
                    break
        if mejora_encontrada:
            break

    # ----> Recorrer el cromosoma B si no se encontró una mejora en el cromosoma A <----
    if not mejora_encontrada:
        indices_grupos = list(range(len(cromosoma_B)))
        random.shuffle(indices_grupos)


        for i in indices_grupos:  # Recorrer en orden permutado
            grupo = cromosoma_B[i]
            for dia_idx, dia in enumerate(dias_semana):
                # Calcular el desbalance del día
                horas_dia = sum(c % 10 for c in grupo[dia][1:])  # Eliminar grupo[dia][0]
                desbalance =  horas_maximas - horas_dia

                if desbalance > 0:  # Verificar si hay un desbalance
                    hora_inicio_original = grupo[dia][0]  # Guardar la hora de inicio original
                    for hora_inicio_prueba in range(desbalance):
                        if hora_inicio_prueba != hora_inicio_original:  # Verificar que la nueva hora sea diferente
                            grupo[dia][0] = hora_inicio_prueba  # Probar una nueva hora de inicio
                            aptitud_actual = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas,semestre)

                            if aptitud_actual < aptitud_anterior:

                                mejora_encontrada = True
                                break
                        if mejora_encontrada:
                            break
                    if not mejora_encontrada:
                        grupo[dia][0] = hora_inicio_original  # Restaurar la hora de inicio original
                    if mejora_encontrada:
                        break
            if mejora_encontrada:
                break
    
    return cromosoma_A, cromosoma_B

def mover_individuos_misma_aptitud(poblacion_ordenada):
    """
    Mueve los individuos con la misma aptitud al final de la lista.

    Args:
        poblacion_ordenada: Una lista de tuplas (aptitud, individuo) ordenada por aptitud.

    Returns:
        La lista modificada con los individuos con la misma aptitud al final.
    """
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    n = len(poblacion_ordenada)
    for i in range(n - 1, 0, -1):  # Iterar en orden inverso
        #print(i, poblacion_ordenada[i][0], poblacion_ordenada[i - 1][0])
        if poblacion_ordenada[i][0] == poblacion_ordenada[i - 1][0]:
            # Mover el elemento i al final de la lista
            elemento_a_mover = poblacion_ordenada.pop(i)  # Eliminar el elemento y guardarlo
            poblacion_ordenada.append(elemento_a_mover) # Añadir el elemento al final de la lista

    return poblacion_ordenada


def aplicar_movimiento_mejora_dia(poblacion, horas_maximas, semestre, aptitud_ultimo_elite):
    """
    Aplica el movimiento de mejora a cada individuo de la población,
    intentando mejorar el horario de un día a la vez.

    Args:
        poblacion: Una lista de individuos.
        horas_maximas: Número máximo de horas en el horario.
        semestre: El semestre actual.
        aptitud_ultimo_elite: Aptitud del último individuo del grupo elite.

    Returns:
        La población modificada.
    """
    poblacion_modificada = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    for individuo in poblacion:
        cromosoma_A, cromosoma_B = individuo
        aptitud_anterior = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas, semestre)
        
        # Verificar si la aptitud actual es mejor que la del último elite
        if aptitud_anterior >= aptitud_ultimo_elite:
            poblacion_modificada.append((cromosoma_A, cromosoma_B))  # Agregar el individuo sin cambios
            continue  # Pasar al siguiente individuo

        mejora_encontrada = False

        # Recorrer el cromosoma A

        indices_grupos = list(range(len(cromosoma_A)))
        random.shuffle(indices_grupos)

        for i in indices_grupos:  
            grupo = cromosoma_A[i]
            for dia_idx, dia in enumerate(dias_semana):
                # Verificar si hay al menos 2 materias en el día
                if len(grupo[dia]) >= 3:
                    for i in range(1, len(grupo[dia]) - 1):
                        for j in range(i + 1, len(grupo[dia])):
                            # Intercambiar las clases
                            grupo[dia][i], grupo[dia][j] = grupo[dia][j], grupo[dia][i]

                            # Calcular la aptitud del individuo (solo si se hizo un cambio)
                            aptitud_actual = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas, semestre)

                            # Deshacer el intercambio si la aptitud no mejora
                            if aptitud_actual > aptitud_anterior:
                                grupo[dia][i], grupo[dia][j] = grupo[dia][j], grupo[dia][i]
                            else:
                                aptitud_anterior = aptitud_actual
                                mejora_encontrada = True
                                break  # Salir del bucle si se encontró una mejora
                        if mejora_encontrada:
                            break  # Salir del bucle de 'i' si se encontró una mejora
                    if mejora_encontrada:
                        break  # Salir del bucle de 'dia' si se encontró una mejora
            if mejora_encontrada:
                break  # Salir del bucle de 'grupo' si se encontró una mejora

        # Recorrer el cromosoma B
        if not mejora_encontrada:
            indices_grupos = list(range(len(cromosoma_B)))
            random.shuffle(indices_grupos)

            for i in indices_grupos:  
                grupo = cromosoma_B[i]
                for dia_idx, dia in enumerate(dias_semana):
                    # Verificar si hay al menos 2 materias en el día
                    if len(grupo[dia]) >= 3:
                        for i in range(1, len(grupo[dia]) - 1):
                            for j in range(i + 1, len(grupo[dia])):
                                # Intercambiar las clases
                                grupo[dia][i], grupo[dia][j] = grupo[dia][j], grupo[dia][i]

                                # Calcular la aptitud del individuo (solo si se hizo un cambio)
                                aptitud_actual = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas, semestre)

                                # Deshacer el intercambio si la aptitud no mejora
                                if aptitud_actual > aptitud_anterior:
                                    grupo[dia][i], grupo[dia][j] = grupo[dia][j], grupo[dia][i]
                                else:
                                    aptitud_anterior = aptitud_actual
                                    mejora_encontrada = True
                                    break  # Salir del bucle si se encontró una mejora
                            if mejora_encontrada:
                                break  # Salir del bucle de 'i' si se encontró una mejora
                        if mejora_encontrada:
                            break  # Salir del bucle de 'dia' si se encontró una mejora
                if mejora_encontrada:
                    break  # Salir del bucle de 'grupo' si se encontró una mejora

        poblacion_modificada.append((cromosoma_A, cromosoma_B))
    
    return poblacion_modificada

def aplicar_movimiento_mejora_clase(poblacion, horas_maximas, semestre):
    """
    Aplica un movimiento de mejora para la materia Dibujo I en cada individuo de la población,
    moviendo las clases al inicio o al final del día según corresponda.

    Args:
        poblacion: Una lista de individuos.
        horas_maximas: Número máximo de horas en el horario.
        semestre: El semestre actual.

    Returns:
        La población modificada.
    """
    poblacion_modificada = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    for individuo in poblacion:
        cromosoma_A, cromosoma_B = individuo
        mejora_encontrada = False

        # Recorrer cada cromosoma
        for cromosoma in [cromosoma_A, cromosoma_B]:
            for grupo_idx, grupo in enumerate(cromosoma):
                for dia_idx, dia in enumerate(dias_semana):
                    # Verificar si hay al menos 2 materias en el día
                    if len(grupo[dia]) >= 3:
                        for materia in primera_ultima_hora[semestre]:  # Iterar sobre las materias del semestre
                            for i, clase in enumerate(grupo[dia]):
                                if clase // 10 in [c // 10 for c in materias[materia]["Clases"]]:
                                    # Mover la clase al inicio o al final del día
                                    if i != 1 and i != len(grupo[dia]) - 1:
                                        # Mover al inicio o al final, lo que esté más cerca
                                        if abs(i - 1) < abs(i - (len(grupo[dia]) - 1)):
                                            grupo[dia].insert(1, grupo[dia].pop(i))
                                        else:
                                            grupo[dia].append(grupo[dia].pop(i))


                                        mejora_encontrada = True
                                        break
                            if mejora_encontrada:
                                break  # Salir del bucle de 'dia' si se encontró una mejora
                if mejora_encontrada:
                    break  # Salir del bucle de 'grupo' si se encontró una mejora
            if mejora_encontrada:
                break  # Salir del bucle de 'cromosoma' si se encontró una mejora

        poblacion_modificada.append((cromosoma_A, cromosoma_B))

    return poblacion_modificada


# Ejemplo de uso:

# 22 grupos A // 22 grupos B  mañana y 22 grupos A y 22 grupos B tarde
sizeGruposMatutinos = 11
sizePoblacion = 120
horas_maximas=6
# *** Definir el número de generaciones ***
num_generaciones = 50000
# *** Definir el porcentaje de elitismo ***
porcentaje_elitismo = 0.70  # 30% de elitismo
aptitud_ultimo_elite = 0
# *** Definir el porcentaje de soluciones aleatorias ***
porcentaje_aleatorias = 0.0  # 10% de soluciones aleatorias

# *** Definir el semestre ***
semestre = "Semestre2"

# *** Inicializar la población ***
poblacion = []
for _ in range(sizePoblacion):
    # Creamos el cromosoma para la Opcion A
    grupos_opcion_A = []
    for _ in range(sizeGruposMatutinos):
        grupo = crear_horario(OpcionA, semestre, horas_maximas)
        grupos_opcion_A.append(grupo)

    # Creamos el cromosoma para la Opcion B
    grupos_opcion_B = []
    for _ in range(sizeGruposMatutinos):
        grupo = crear_horario(OpcionB, semestre, horas_maximas)
        grupos_opcion_B.append(grupo)

    # Agregamos la tupla de cromosomas a la población
    poblacion.append((grupos_opcion_A, grupos_opcion_B))

# *** Inicializar el vector para las mejores aptitudes ***
mejores_aptitudes = []
#print("Población inicial:")
contador_estancamiento = 1
iteraciones = 1
# *** Bucle principal para las generaciones ***
for generacion in range(num_generaciones):
    print(f"\nGeneración {generacion + 1}")

    # *** Cambio en la verificación de validez ***
    #print("Validez de los individuos en la población inicial:")
    #for cromosoma_A, cromosoma_B in poblacion:
        #valido_A = individuo_valido(cromosoma_A, horas_maximas, opcion=OpcionA, semestre="Semestre1")
        #valido_B = individuo_valido(cromosoma_B, horas_maximas, opcion=OpcionB, semestre="Semestre1")
        #print(f"Cromosoma A: {'Válido' if valido_A else 'Inválido'}")
        #print(f"Cromosoma B: {'Válido' if valido_B else 'Inválido'}")

    # *** Cálculo de la aptitud para cada individuo ***
    aptitudes_poblacion = []
    
    for cromosoma_A, cromosoma_B in poblacion:
        aptitud = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas,semestre)
        aptitudes_poblacion.append(aptitud)

    print("Aptitudes de la población:", aptitudes_poblacion)

    # *** Encontrar el mejor individuo de la generación actual ***
    mejor_aptitud = min(aptitudes_poblacion)
    mejor_individuo = poblacion[aptitudes_poblacion.index(mejor_aptitud)]

    # *** Guardar la aptitud del mejor individuo ***
    mejores_aptitudes.append(mejor_aptitud)

    # *** Selección de parejas para el cruce ***
    parejas_cruce = seleccion_por_permutacion(poblacion, sizePoblacion)
 
        
    parejas_cruce2 = seleccion_por_permutacion(poblacion, sizePoblacion)
    parejas_cruce = parejas_cruce + parejas_cruce2
    parejas_cruce2 = seleccion_por_permutacion(poblacion, sizePoblacion)
    parejas_cruce = parejas_cruce + parejas_cruce2
    parejas_cruce2 = seleccion_por_permutacion(poblacion, sizePoblacion)
    parejas_cruce = parejas_cruce + parejas_cruce2
 #    parejas_cruce2 = seleccion_por_permutacion(poblacion, sizePoblacion)
 #    parejas_cruce = parejas_cruce + parejas_cruce2
   

    # *** Generación de hijos  ***
    nueva_generacion = generar_hijos_dos_cromosomas(
        parejas_cruce, horas_maximas, opcion_A=OpcionA, opcion_B=OpcionB, semestre="Semestre1"
    )

    # *** Aplicar movimiento de mejora a la nueva generación ***
    
    if generacion > 15:
      ultimo = 10 
      aptitud_ultimo_elite = poblacion_ordenada_padres[9][0]+ (poblacion_ordenada_padres[40][0]-poblacion_ordenada_padres[0][0])*(contador_estancamiento)/10
      if generacion > 16:
          # nueva_generacion = aplicar_movimiento_mejora_clase(nueva_generacion, horas_maximas, semestre)
        if mejores_aptitudes[-1] == mejores_aptitudes[-2]:
            contador_estancamiento += 1
        else:
            contador_estancamiento = 1
            iteraciones=1
            
        if contador_estancamiento > 2:
            iteraciones = 2
            if contador_estancamiento > 4:
                iteraciones = 4

                if contador_estancamiento > 15:
                    iteraciones = 2
                    if contador_estancamiento > 30:
                        iteraciones = 2
                        if contador_estancamiento > 50:
                            iteraciones = 3
                            if contador_estancamiento > 60:
                                iteraciones = 4
                                if contador_estancamiento > 70:
                                    iteraciones = 6
                        
        
        print("contador: ",contador_estancamiento,"  aptitud corte",aptitud_ultimo_elite,"iter", iteraciones)
        # Inicializar vector para almacenar las aptitudes ya mejoradas
        valores_aptitudes_mejoradas = []
        
        # Selección de hijos que deberían mejorarse
        nueva_generacion_mejores = []
        for i, hijo in enumerate(nueva_generacion):
            aptitud = calcular_aptitud_individuo(hijo[0], hijo[1], horas_maximas, semestre)
        
            # Comprobar si la aptitud es menor que la del último en el grupo de élite y si no ha sido mejorada antes
            if aptitud < aptitud_ultimo_elite and aptitud not in valores_aptitudes_mejoradas:
                # Añadir la aptitud al vector de aptitudes mejoradas
                valores_aptitudes_mejoradas.append(aptitud)
        
                # Añadir el hijo a la lista de los que serán mejorados
                nueva_generacion_mejores.append(hijo)
        
                # Añadir la aptitud del hijo mejorado a la lista de aptitudes de la nueva generación
                aptitudes_nueva_generacion.append(aptitud)
        
                # Eliminar el hijo de nueva_generacion para evitar duplicación
                del nueva_generacion[i]
        
        
        for i in range(iteraciones):  
             nueva_generacion_mejores = aplicar_movimiento_mejora_poblacion(nueva_generacion_mejores, horas_maximas,semestre,aptitud_ultimo_elite)
             nueva_generacion_mejores = aplicar_movimiento_hora_inicio(nueva_generacion_mejores, horas_maximas,semestre,aptitud_ultimo_elite)
             nueva_generacion_mejores = aplicar_movimiento_mejora_dia(nueva_generacion_mejores, horas_maximas, semestre,aptitud_ultimo_elite)
             nueva_generacion_mejores = aplicar_movimiento_intercambio_dias(nueva_generacion_mejores , horas_maximas, semestre, aptitud_ultimo_elite)
             nueva_generacion_mejores = aplicar_movimiento_clase_a_otro_dia(nueva_generacion_mejores , horas_maximas, semestre, aptitud_ultimo_elite)
             nueva_generacion_mejores = aplicar_movimiento_cambio_dia(nueva_generacion_mejores , horas_maximas, semestre, aptitud_ultimo_elite)
             nueva_generacion_mejores = aplicar_movimiento_espejo_dia(nueva_generacion_mejores , horas_maximas, semestre, aptitud_ultimo_elite)
             
             if generacion < 40:
                 nueva_generacion_mejores = aplicar_movimiento_cambio_dia(nueva_generacion_mejores, horas_maximas, semestre, aptitud_ultimo_elite)
                 nueva_generacion_mejores = aplicar_movimiento_espejo_dia(nueva_generacion_mejores, horas_maximas, semestre, aptitud_ultimo_elite)
            
        nueva_generacion.extend(nueva_generacion_mejores)
        

    else:
      nueva_generacion = aplicar_movimiento_mejora_clase(nueva_generacion, horas_maximas, semestre)
      nueva_generacion = aplicar_movimiento_mejora_clase(nueva_generacion, horas_maximas, semestre)


    # *** Eliminar hijos inválidos ***
    vieja = len (nueva_generacion)
    nueva_generacion = eliminar_hijos_invalidos(nueva_generacion, OpcionA, OpcionB, "Semestre1", horas_maximas)
    print("tamaño nueva: ",len (nueva_generacion), "  tamaño vieja:  ",vieja)

    # *** Implementar el elitismo y la selección de soluciones aleatorias ***

    # 1. Ordenar la población por aptitud
    aptitudes_nueva_generacion = []
    for cromosoma_A, cromosoma_B in nueva_generacion:
        aptitud = calcular_aptitud_individuo(cromosoma_A, cromosoma_B, horas_maximas,semestre)
        aptitudes_nueva_generacion.append(aptitud)

    poblacion_ordenada_hijos = sorted(zip(aptitudes_nueva_generacion, nueva_generacion), key=lambda x: x[0])
    poblacion_ordenada_padres = sorted(zip(aptitudes_poblacion, poblacion), key=lambda x: x[0])

    poblacion_ordenada_hijos = mover_individuos_misma_aptitud(poblacion_ordenada_hijos)
    print("Aptitudes de los hijos después de mover:")
    for i, (aptitud, _) in enumerate(poblacion_ordenada_hijos):
         print(f"Hijo {i+1}: {aptitud}")




    # 2. Seleccionar los mejores individuos (padres)
    num_elite = int(sizePoblacion * porcentaje_elitismo)
    mejores_individuos = poblacion_ordenada_padres[:num_elite]
    aptitud_ultimo_elite = poblacion_ordenada_padres[num_elite-1][0]

    # ----> Detener el bucle si el último elite es igual al primero <----
    if aptitud_ultimo_elite == poblacion_ordenada_padres[0][0]:
        print(f"Algoritmo detenido en la generación {generacion + 1}. Todos los individuos tienen la misma aptitud.")
        break  # Salir del bucle for generacion

    # 3. Seleccionar los mejores hijos, evitando repeticiones excesivas de aptitud
    num_mejores_hijos = int(sizePoblacion * (1 - porcentaje_elitismo - porcentaje_aleatorias))
    mejores_hijos = []
    
    # Obtener las aptitudes de los padres seleccionados
    aptitudes_padres = [aptitud for aptitud, _ in mejores_individuos]
    
    for aptitud, hijo in poblacion_ordenada_hijos:
        # Contar cuántas veces la aptitud está presente en los padres
        if aptitudes_padres.count(aptitud) < 4:
            mejores_hijos.append(hijo)
        if len(mejores_hijos) == num_mejores_hijos:
            break
    
    # Si no hay suficientes hijos, añadir más padres (que iban a ser sustituidos) para completar la nueva generación
    faltantes = num_mejores_hijos - len(mejores_hijos)
    if faltantes > 0:
        padres_a_reemplazar = poblacion_ordenada_padres[num_elite:num_elite + faltantes]
        mejores_hijos += [individuo for _, individuo in padres_a_reemplazar]
    
    # 4. Seleccionar individuos aleatorios de los hijos no seleccionados
    hijos_no_seleccionados = poblacion_ordenada_hijos[num_mejores_hijos:]
    num_aleatorios = int(sizePoblacion * porcentaje_aleatorias)
    individuos_aleatorios = random.sample(hijos_no_seleccionados, num_aleatorios)
    
    # 5. Combinar los individuos seleccionados en la nueva generación
    nueva_generacion = [individuo for _, individuo in mejores_individuos] + individuos_aleatorios + mejores_hijos

    # *** Actualizar la población con la nueva generación ***
    poblacion = nueva_generacion

    # ---->  Exportar los horarios cada 50 generaciones <----
    if (generacion + 1) % 5 == 0:  # Verificar si la generación es múltiplo de 50
        nombre_archivo = f"horarios_finales_spider_{generacion + 1}.csv"
        exportar_horarios_csv(poblacion, mejores_aptitudes, aptitudes_poblacion, horas_maximas, semestre, nombre_archivo)
    # *** Opcional: Imprimir los cromosomas en un archivo CSV ***
    #imprimir_cromosomas_csv(poblacion)



exportar_horarios_csv(poblacion, mejores_aptitudes, aptitudes_poblacion, horas_maximas, semestre, "horarios_finales.csv")
# *** Mostrar las aptitudes del mejor individuo de cada generación ***
print("\nAptitudes del mejor individuo en cada generación:")
for i, aptitud in enumerate(mejores_aptitudes):
    print(f"Generación {i + 1}: {aptitud}")
