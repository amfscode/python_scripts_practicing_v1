#
import asyncio
from time import sleep

async def tarea(nombre,segundos):
    print(f"Iniciando {nombre}")
    await asyncio.sleep(segundos) # "Mientras espero, ejecuta otras tareas."
    print(f"Finalizando {nombre}")

async def main():
    await asyncio.gather(
        tarea("A", 2),
        tarea("B", 3),
        tarea("C", 1)
    )

asyncio.run(main())



# await - No bloquea el programa completo como haría:
# import time
# time.sleep(segundos)