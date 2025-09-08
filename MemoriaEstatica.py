calificaciones=[0]*5
for i in range(5):
    calificacion=int(input(f"Captura calificacion{i+1}: "))
    calificaciones[i]=calificacion

print("Las calificaciones capturadas fueron: ")
for i, c in enumerate(calificaciones, start=1):
    print(f"Calificación {i}: {c}")
