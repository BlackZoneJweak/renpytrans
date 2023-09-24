# -*- coding: utf-8 -*-
"""
1) Verificar caracteres especiales \033[32m||\033[0m \033[31m檢查特殊字元\033[0m  
2) Copiar todos archivos .rpy que esta en esp a la carpeta projzv3 traducir \033[32m||\033[0m \033[31m拷貝esp裡的所有.rpy\033[0m
3) Copiar todos archivos .rpy que esta en chino a la carpeta projzv3 traducir \033[32m||\033[0m \033[31m拷貝chino裡的所有.rpy\033[0m 
4) Eliminar completo .bak en toda las carpetas \033[32m||\033[0m \033[31m移除所有資料夾.bak\033[0m
5) Renombrar .rpy a .bak solo una carpeta \033[32m||\033[0m \033[31m只備份單一資料夾.rpy到.bak\033[0m
6) Hacer copia .rpy a .bak todas las carpetas \033[32m||\033[0m \033[31m備份所有資料夾.rpy到.bak\033[0m
7) Page down 200sec \033[32m||\033[0m \033[31m自動page down 200sec\033[0m
8) Copiar todos archivos .rpy a antigua que esta en esp a la carpeta projzv3 traducir \033[32m||\033[0m \033[31m 拷貝esp裡的所有.rpy到antigua\033[0m
9) Copiar todos archivos .rpy a antigua que esta en chino a la carpeta projzv3 traducir \033[32m||\033[0m \033[31m 拷貝chino裡的所有.rpy到antigua\033[0m
10) buscar [] {} ()
11) Reemplazar commam ESP 
12) Reemplazar commam CHT 
13) Separar el .rpy en varios archivos
14) Buscar dirección de google drives
15) Reemplazar screens ESP
16) Reemplazar screens CHT
17) Nada aun 
18) Nada aun
19) Nada aun
20) Nada aun1
"""
# imprimimos el menú en pantalla
print("\033[36m")

print("""
1) Verificar caracteres especiales \033[32m||\033[0m \033[31m檢查特殊字元\033[0m  
2) Copiar todos archivos .rpy que esta en esp a la carpeta projzv3 traducir \033[32m||\033[0m \033[31m拷貝esp裡的所有.rpy\033[0m
3) Copiar todos archivos .rpy que esta en chino a la carpeta projzv3 traducir \033[32m||\033[0m \033[31m拷貝chino裡的所有.rpy\033[0m 
4) Eliminar completo .bak en toda las carpetas \033[32m||\033[0m \033[31m移除所有資料夾.bak\033[0m
5) Renombrar .rpy a .bak solo una carpeta \033[32m||\033[0m \033[31m只備份單一資料夾.rpy到.bak\033[0m
6) Hacer copia .rpy a .bak todas las carpetas \033[32m||\033[0m \033[31m備份所有資料夾.rpy到.bak\033[0m
7) Page down 200sec \033[32m||\033[0m \033[31m自動page down 200sec\033[0m
8) Copiar todos archivos .rpy a antigua que esta en esp a la carpeta projzv3 traducir \033[32m||\033[0m \033[31m 拷貝esp裡的所有.rpy到antigua\033[0m
9) Copiar todos archivos .rpy a antigua que esta en chino a la carpeta projzv3 traducir \033[32m||\033[0m \033[31m 拷貝chino裡的所有.rpy到antigua\033[0m
10) buscar [] {} ()
11) Reemplazar commam ESP 
12) Reemplazar commam CHT 
13) Separar el .rpy en varios archivos
14) Buscar dirección de google drives
15) Reemplazar screens ESP
16) Reemplazar screens CHT
17) Nada aun 
18) Nada aun
19) Nada aun
20) Nada aun
""")
print("\033[0m")

# Leemos lo que ingresa el usuario
eleg = input("Seleccionar el ejercicio que desea ejecutar: ")

# Según lo que ingresó, código diferente
if eleg == "1":
    import os
    import re
    import time
    import progressbar
    # folder = 'G:/TamaraExposedTheBeginning10esp/tetbesp_v1.0'
    folder = os.path.dirname(os.path.abspath(__file__))
    print("Comenzando procesamiento de archivos .rpy...")
    start_time = time.time()

    total_archivos = len(os.listdir(folder))
    # bar = progressbar.ProgressBar(maxval=100)
    bar = progressbar.ProgressBar(maxval=total_archivos)
    bar.start()
    contador = 0

    for filename in os.listdir(folder):
        if filename.endswith('.bak'):
            os.remove(os.path.join(folder, filename))
            print("\n")
            print(f"Eliminando archivo {filename}")

    for filename in os.listdir(folder):
        if filename.endswith('.rpy'):
            with open(os.path.join(folder, filename), 'r', encoding="utf-8") as f:
                text = f.read()

                cleaned = re.sub(
                    r'</font><font style="vertical-align: inherit;">', '', text)
                cleaned = re.sub(
                    r'<font style="vertical-align: inherit;">', '', cleaned)
                cleaned = re.sub(r'？', '?', cleaned)
                cleaned = re.sub(r'。', '.', cleaned)
                cleaned = re.sub(r'！', '!', cleaned)
                cleaned = re.sub(r'“', '"', cleaned)
                cleaned = re.sub(r'”', '"', cleaned)
                cleaned = re.sub(r'：', ':', cleaned)
                cleaned = re.sub(r'，', ',', cleaned)
                cleaned = re.sub(r'（', '(', cleaned)
                cleaned = re.sub(r'）', ')', cleaned)
                cleaned = re.sub(r'</font>', '', cleaned)
                cleaned = re.sub(r'<td>', '', cleaned)
                cleaned = re.sub(r'</td>', '', cleaned)
                cleaned = re.sub(r'<tr>', '', cleaned)
                cleaned = re.sub(r'</tr>', '', cleaned)
                # cleaned = re.sub(r'{i}', '', cleaned)
                # cleaned = re.sub(r'{/i}', '', cleaned)
                cleaned = re.sub(r'@@', '', cleaned)

                patron = r'\\.+?"'
                resultados = re.findall(patron, cleaned)
                for resultado in resultados:
                    cleaned = cleaned.replace(resultado, '@^' + resultado)

                time.sleep(0.5)
                contador += 1
                bar.update(contador)

            with open(os.path.join(folder, 'cleaned_'+filename), 'w', encoding="utf-8") as f:
                f.write(cleaned)
    print("\n")
    for filename in os.listdir(folder):
        if filename.endswith('.rpy') and not filename.startswith('cleaned_'):
            os.rename(os.path.join(folder, filename),
                      os.path.join(folder, filename.split('.')[0] + '.rpy.bak'))
            print(f"Procesando archivo {filename}")
    print("\n")
    for filename in os.listdir(folder):
        if filename.startswith('cleaned_'):
            cleaned_name = filename
            original_name = filename.replace('cleaned_', '')
            os.rename(os.path.join(folder, cleaned_name),
                      os.path.join(folder, original_name))
            print(f"cambiando nombre de archivo {filename}")

    end_time = time.time()
    print(f"Tiempo de ejecución: {round(end_time - start_time, 2)} segundos")
    print("Procesamiento de archivos .rpy finalizado")
elif eleg == "2":
    import os
    import shutil
    import time
    from tqdm import tqdm

    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_folder = os.path.join(script_dir, 'game', 'tl', 'esp')
    destination_folder = 'd:\\projzv3\\traducir'

    if not os.path.exists(source_folder):
        print("Carpeta origen no encontrada")

    if os.path.exists(destination_folder):
        print(
            f"La carpeta {destination_folder} no está vacía. ¿Desea borrar el contenido antes de copiar? (s/n)")
        if input().lower() != "s":
            print("Copia cancelada")
            exit()
        shutil.rmtree(destination_folder)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    total_files = 0
    copied_files = 0

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.rpy'):
                total_files += 1  # Incrementar el contador de archivos
                source_path = os.path.join(root, file)
                destination_path = os.path.join(
                    destination_folder, os.path.relpath(root, source_folder), file)

                # Crear el directorio de destino si no existe
                destination_dir = os.path.dirname(destination_path)
                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)

                print(f'Copying {file}')
                try:
                    shutil.copy2(source_path, destination_path)
                except Exception as e:
                    print("Error copiando archivo:", e)
                copied_files += 1

    with tqdm(total=total_files, desc="Copying files", unit="file") as pbar:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if file.endswith('.rpy'):
                    source_path = os.path.join(root, file)
                    destination_path = os.path.join(
                        destination_folder, os.path.relpath(root, source_folder), file)
                    try:
                        shutil.copy2(source_path, destination_path)
                    except Exception as e:
                        print("Error copiando archivo:", e)
                    copied_files += 1
                    pbar.update(1)

    print("Proceso de copia completado")
elif eleg == "3":
    import os
    import shutil
    import time
    from tqdm import tqdm

    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_folder = os.path.join(script_dir, 'game', 'tl', 'chino')
    destination_folder = 'd:\\projzv3\\traducir'

    if not os.path.exists(source_folder):
        print("Carpeta origen no encontrada")

    if os.path.exists(destination_folder):
        print(
            f"La carpeta {destination_folder} no está vacía. ¿Desea borrar el contenido antes de copiar? (s/n)")
        if input().lower() != "s":
            print("Copia cancelada")
            exit()
        shutil.rmtree(destination_folder)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    total_files = 0
    copied_files = 0

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.rpy'):
                total_files += 1  # Incrementar el contador de archivos
                source_path = os.path.join(root, file)
                destination_path = os.path.join(
                    destination_folder, os.path.relpath(root, source_folder), file)

                # Crear el directorio de destino si no existe
                destination_dir = os.path.dirname(destination_path)
                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)

                print(f'Copying {file}')
                try:
                    shutil.copy2(source_path, destination_path)
                except Exception as e:
                    print("Error copiando archivo:", e)
                copied_files += 1

    with tqdm(total=total_files, desc="Copying files", unit="file") as pbar:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if file.endswith('.rpy'):
                    source_path = os.path.join(root, file)
                    destination_path = os.path.join(
                        destination_folder, os.path.relpath(root, source_folder), file)
                    try:
                        shutil.copy2(source_path, destination_path)
                    except Exception as e:
                        print("Error copiando archivo:", e)
                    copied_files += 1
                    pbar.update(1)

    print("Proceso de copia completado")
elif eleg == "4":
    import os
    import re
    import time
    import shutil
    import progressbar
    # folder = 'G:/TamaraExposedTheBeginning10esp/tetbesp_v1.0'
    folder = os.path.dirname(os.path.abspath(__file__))
    print("Comenzando procesamiento de eliminar .bak...")
    start_time = time.time()

    total_archivos = len(os.listdir(folder))
    bar = progressbar.ProgressBar(maxval=100)
    bar.start()
    contador = 0

    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.bak'):
                filepath = os.path.join(dirpath, filename)
                os.remove(filepath)
                print(f"Eliminando archivo {filename}")

    contador += 1
    porcentaje = int(contador / total_archivos * 100)

    end_time = time.time()
    print(f"Tiempo de ejecución: {round(end_time - start_time, 2)} segundos")
    # print("Procesamiento de archivos .rpy finalizado")
    print("Archivos .bak eliminados")
    bar.update(porcentaje)
elif eleg == "5":
    import os
    import shutil
    import time

    folder = os.path.dirname(os.path.abspath(__file__))

    print("Comenzando procesamiento de archivos .rpy a .bak...")
    start_time = time.time()

    for file in os.listdir(folder):
        if file.endswith('.rpy'):
            src = os.path.join(folder, file)
            dst = src + '.bak'
            shutil.move(src, dst)
            print(f'Renombrado {src} a {dst}')

    end_time = time.time()
    print(f"Tiempo de ejecución: {round(end_time - start_time, 2)} segundos")
    print("Procesamiento de archivos .rpy finalizado")
elif eleg == "6":
    import os
    import re
    import shutil
    import time
    import progressbar
    # folder = 'G:/TamaraExposedTheBeginning10esp/tetbesp_v1.0'
    folder = os.path.dirname(os.path.abspath(__file__))
    print("Comenzando procesamiento de archivos .rpy a .bak...")
    start_time = time.time()

    total_archivos = len(os.listdir(folder))
    bar = progressbar.ProgressBar(maxval=100)
    bar.start()
    contador = 0

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.rpy'):
                src = os.path.join(root, file)
                dst = src + '.bak'
                shutil.copy2(src, dst)
                print(f'Backed up {src} to {dst}')

    contador += 1
    porcentaje = int(contador / total_archivos * 100)

    end_time = time.time()
    print(f"Tiempo de ejecución: {round(end_time - start_time, 2)} segundos")
    print("Procesamiento de archivos .rpy finalizado")
    bar.update(porcentaje)
elif eleg == "7":
    import curses
    import time
    import keyboard

    stdscr = curses.initscr()
    curses.noecho()
    stdscr.nodelay(True)

    total = 100

    width = stdscr.getmaxyx()[1] - 20

    stdscr.addstr(0, 0, 'Progreso: ')

    for i in range(total):

        if keyboard.is_pressed('q') or keyboard.is_pressed('esc'):
            break

        keyboard.press('pagedown')
        time.sleep(3)
        keyboard.press('pagedown')
        time.sleep(3)

        percent_done = (i + 1) * 100 / total

        stdscr.addstr(1, 0, '[' + '=' * int(percent_done) +
                      '>' + '-' * (100 - int(percent_done)) + ']')

        contador = f'{int(percent_done)}%'

        stdscr.addstr(4, 0, contador)

        stdscr.refresh()
        time.sleep(0.1)

    stdscr.addstr(1, 0, 'Completado!' + ' ' * (width - 12))
    curses.endwin()

elif eleg == "8":
    import os
    import shutil
    import time
    from tqdm import tqdm

    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_folder = os.path.join(script_dir, 'game', 'tl', 'esp')
    destination_folder = 'd:\\projzv3\\antigua'

    if not os.path.exists(source_folder):
        print("Carpeta origen no encontrada")

    if os.path.exists(destination_folder):
        print(
            f"La carpeta {destination_folder} no está vacía. ¿Desea borrar el contenido antes de copiar? (s/n)")
        if input().lower() != "s":
            print("Copia cancelada")
            exit()
        shutil.rmtree(destination_folder)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    total_files = 0
    copied_files = 0

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.rpy'):
                total_files += 1  # Incrementar el contador de archivos
                source_path = os.path.join(root, file)
                destination_path = os.path.join(
                    destination_folder, os.path.relpath(root, source_folder), file)

                # Crear el directorio de destino si no existe
                destination_dir = os.path.dirname(destination_path)
                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)

                print(f'Copying {file}')
                try:
                    shutil.copy2(source_path, destination_path)
                except Exception as e:
                    print("Error copiando archivo:", e)
                copied_files += 1

    with tqdm(total=total_files, desc="Copying files", unit="file") as pbar:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if file.endswith('.rpy'):
                    source_path = os.path.join(root, file)
                    destination_path = os.path.join(
                        destination_folder, os.path.relpath(root, source_folder), file)
                    try:
                        shutil.copy2(source_path, destination_path)
                    except Exception as e:
                        print("Error copiando archivo:", e)
                    copied_files += 1
                    pbar.update(1)

    print("Proceso de copia completado")
elif eleg == "9":
    import os
    import shutil
    import time
    from tqdm import tqdm

    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_folder = os.path.join(script_dir, 'game', 'tl', 'chino')
    destination_folder = 'd:\\projzv3\\antigua'

    if not os.path.exists(source_folder):
        print("Carpeta origen no encontrada")

    if os.path.exists(destination_folder):
        print(
            f"La carpeta {destination_folder} no está vacía. ¿Desea borrar el contenido antes de copiar? (s/n)")
        if input().lower() != "s":
            print("Copia cancelada")
            exit()
        shutil.rmtree(destination_folder)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    total_files = 0
    copied_files = 0

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.rpy'):
                total_files += 1  # Incrementar el contador de archivos
                source_path = os.path.join(root, file)
                destination_path = os.path.join(
                    destination_folder, os.path.relpath(root, source_folder), file)

                # Crear el directorio de destino si no existe
                destination_dir = os.path.dirname(destination_path)
                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)

                print(f'Copying {file}')
                try:
                    shutil.copy2(source_path, destination_path)
                except Exception as e:
                    print("Error copiando archivo:", e)
                copied_files += 1

    with tqdm(total=total_files, desc="Copying files", unit="file") as pbar:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if file.endswith('.rpy'):
                    source_path = os.path.join(root, file)
                    destination_path = os.path.join(
                        destination_folder, os.path.relpath(root, source_folder), file)
                    try:
                        shutil.copy2(source_path, destination_path)
                    except Exception as e:
                        print("Error copiando archivo:", e)
                    copied_files += 1
                    pbar.update(1)

    print("Proceso de copia completado")
elif eleg == "10":
    import os
    import re

    def find_matches(pattern, suffix):
        file_count = 0
        for filename in os.listdir('.'):
            if filename.endswith('.rpy'):
                file_count += 1

        processed_files = 0
        for filename in os.listdir('.'):
            if filename.endswith('.rpy'):
                matches_by_line = {}
                total_matches = 0

                with open(filename, encoding="utf-8") as f:
                    for i, line in enumerate(f):
                        matches = re.findall(pattern, line)
                        if matches:
                            matches_by_line[i+1] = matches

                result_filename = filename + suffix
                with open(result_filename, 'w', encoding="utf-8") as f:
                    for line, matches in matches_by_line.items():
                        for match in matches:
                            f.write(f'Encontrado en la línea {line} {match}\n')
                            total_matches += 1
                            print(f'Encontrado en la línea {line} {match} \n')

                processed_files += 1
                progress = processed_files / file_count * 100
                print(f'Progreso: {progress:.2f}%')

                print(
                    f'Resultados para {filename} guardados en {result_filename}')
                print(f'Total de matches []: {total_matches}')

    find_matches(r'\[.*?\]', 'resulcomi.txt')
    find_matches(r'\{.*?\}', 'resulllave.txt')
    find_matches(r'\(.*?\)', 'resulllave1.txt')
elif eleg == "11":
    import re

    archivo = "common.rpy"

    cambios = {
        r"\[texto\]": "[text]",
        r"\[índice\]": "[index]",
        r"\[recuento\]": "[count]",
        r"\[problema\]": "[problem]",
        r"\[nombre\]": "[name]",
        r"\[tipo\]": "[kind]",
        r'new "{#weekday_short}Sol"': 'new "{#weekday_short}Dom"',
        r'new "{#month}August"': 'new "{#month}Agosto"',
        r'new "{#month_short}abr"': 'new "{#month_short}Abr"',
        r'new "{#month_short}Mayo"': 'new "{#month_short}May"',
        r'new "{#month_short}ago"': 'new "{#month_short}Ago"',
    }

    lineas = []
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            for buscar, reemplazar in cambios.items():
                linea = re.sub(buscar, reemplazar, linea)
            lineas.append(linea)
            print(linea)

    with open(archivo, "w", encoding="utf-8") as f:
        for l in lineas:
            f.write(l)
elif eleg == "12":
    import re

    archivo = "common.rpy"

    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read()

    cambios = {
        r"\[文本\]": "[text]",
        r"\[计数\]": "[index]",
        r"\[索引\]": "[count]",
        r"\[问题\]": "[problem]",
        r"\[名称\]": "[name]",
        r"\[种类\]": "[kind]",
        r"\[总计\]": "[total]",
        r'"\[控件!s\]"': "'[control!s]'",
        r'new "{#weekday_short}Tue"': 'new "{#weekday_short}週二"',
        r'new "{#weekday_short}Thu"': 'new "{#weekday_short}週四"',
        r'new "{#weekday_short}卫星"': 'new "{#weekday_short}週六"',
        r'new "{#weekday_short}Sun"': 'new "{#weekday_short}週日"',
        r'new "{#month_short}Jan"': 'new "{#month_short}一月"',
        r'new "{#month_short}Mar"': 'new "{#month_short}三月"',
        r'new "{#month_short}Jun"': 'new "{#month_short}六月"',
        r'new "{#month_short}Jul"': 'new "{#month_short}七月"',
        r'new "{#month_short}Sep"': 'new "{#month_short}九月"',
        r'new "{#month_short}Oct"': 'new "{#month_short}十月"',
        r'new "{#month_short}Nov"': 'new "{#month_short}十一月"',
        r'new "{#month_short}Dec"': 'new "{#month_short}十二月"',
        r'"shift\+C"': "'shift+C'",
        r'"alt\+shift\+V"': "'alt+shift+V'",
        r'"v"': "'v'",
        r'"是"': "'是'"
    }

    # Hacer reemplazos en todo el contenido
    for buscar, reemplazar in cambios.items():
        contenido = re.sub(buscar, reemplazar, contenido)

    # Volver a escribir el contenido modificado
    with open(archivo, "w", encoding="utf-8") as f:
        f.write(contenido)
        print(contenido)
elif eleg == "13":
    # ese tiene que cambiar manual el archivo que va separar
    import os

    secuencia = 1
    conteo_lineas = 0
    archivo_salida = open(
        f"secuencia{str(secuencia).zfill(4)}.rpy", "w", encoding="utf-8")

    with open("story.rpy") as archivo:
        for linea in archivo:
            if conteo_lineas == 5000:
                archivo_salida.close()
                secuencia += 1
                conteo_lineas = 0
                archivo_salida = open(
                    f"secuencia{str(secuencia).zfill(4)}.rpy", "w", encoding="utf-8")
                print(linea)

            archivo_salida.write(linea)
            conteo_lineas += 1

    archivo_salida.close()
elif eleg == "14":
    import re

    with open('verificar.txt', "r", encoding="utf-8") as f:
        for line in f:
            match = re.search(r'(href=".*?")', line)
            if match:
                url = match.group(1)
                print(url)
                with open('urls.txt', 'a') as f2:
                    f2.write(url + '\n')

    with open('urls.txt', "r", encoding="utf-8") as f:
        for line in f:
            match = re.search(r'https?://drive\.google\.com/[^"]*', line)
            if match:
                url = match.group(0)

                with open('urlssolo.txt', 'a') as f2:
                    f2.write(url + '\n')
                    print(url)
elif eleg == "15":
    import re

    archivo = "screens.rpy"

    cambios = {
        r'"&lt;"': '"<"',
        r'"&gt;"': '">"',
        # r'new "{#month_short}abr"': 'new "{#month_short}Abr"',
        # r'new "{#month_short}Mayo"': 'new "{#month_short}May"',
        # r'new "{#month_short}ago"': 'new "{#month_short}Ago"',
    }

    lineas = []
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            for buscar, reemplazar in cambios.items():
                linea = re.sub(buscar, reemplazar, linea)
            lineas.append(linea)
            print(linea)

    with open(archivo, "w", encoding="utf-8") as f:
        for l in lineas:
            f.write(l)
elif eleg == "16":
    import re

    archivo = "screens.rpy"

    cambios = {
        r'"&lt;"': '"<"',
        r'"&gt;"': '">"',
        # r'new "{#month_short}abr"': 'new "{#month_short}Abr"',
        # r'new "{#month_short}Mayo"': 'new "{#month_short}May"',
        # r'new "{#month_short}ago"': 'new "{#month_short}Ago"',
    }

    lineas = []
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            for buscar, reemplazar in cambios.items():
                linea = re.sub(buscar, reemplazar, linea)
            lineas.append(linea)
            print(linea)

    with open(archivo, "w", encoding="utf-8") as f:
        for l in lineas:
            f.write(l)
elif eleg == "17":
    print("17 ok")
elif eleg == "18":
    print("ok18")
elif eleg == "19":
    print("ok19")
elif eleg == "20":
    print("ok20")
else:
    print("Opción no es valido")
    exec(open("renpytrans.py", encoding="utf-8").read())
