# -*- coding: utf-8 -*-
"""
1) Verificar caracteres especiales || 檢查特殊字元  
2) Copiar todos archivos .rpy y renombrar a .bak que esta en esp a la carpeta projzv3 traducir || 拷貝esp裡的所有.rpy跟重新命名.bak
3) Copiar todos archivos .rpy y renombrar a .bak que esta en chino a la carpeta projzv3 traducir || 拷貝chino裡的所有.rpy跟重新命名.bak 
4) Eliminar completo .bak en toda las carpetas || 移除所有資料夾.bak
5) Renombrar .rpy a .bak solo una carpeta || 只備份單一資料夾.rpy到.bak
6) Hacer copia .rpy a .bak todas las carpetas || 備份所有資料夾.rpy到.bak
7) Page down 200sec || 自動page down 200sec
8) Copiar todos archivos .rpy a antigua que esta en esp a la carpeta projzv3 traducir || 拷貝esp裡的所有.rpy到antigua
9) Copiar todos archivos .rpy a antigua que esta en chino a la carpeta projzv3 traducir || 拷貝chino裡的所有.rpy到antigua
10) mejorando el verificar caracteres
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
10) Nada aun
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
                                        
                cleaned = re.sub(r'</font><font style="vertical-align: inherit;">', '', text)
                cleaned = re.sub(r'<font style="vertical-align: inherit;">', '', cleaned)
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
                cleaned = re.sub(r'{i}', '', cleaned)
                cleaned = re.sub(r'{/i}', '', cleaned)
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
            os.rename(os.path.join(folder, cleaned_name), os.path.join(folder, original_name))
            print(f"cambiando nombre de archivo {filename}")
    
    end_time = time.time()
    print(f"Tiempo de ejecución: {round(end_time - start_time, 2)} segundos")
    print("Procesamiento de archivos .rpy finalizado")
elif eleg == "2":
    import os
    import shutil 
    import time

    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_folder = os.path.join(script_dir, 'game', 'tl', 'esp')
    destination_folder = 'g:\\projzv3\\traducir'

    if not os.path.exists(source_folder):
        print("Carpeta origen no encontrada")
        
    if os.path.exists(destination_folder):
        print(f"La carpeta {destination_folder} no está vacía. ¿Desea borrar el contenido antes de copiar? (s/n)")
        if input().lower() != "s":
            print("Copia cancelada")
            exit()
        shutil.rmtree(destination_folder)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    rpy_files = []
    copied_files = 0

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.rpy'):
                rpy_files.append(file)
            
    total_rpy_files = len(rpy_files)  
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.rpy'):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                print(f'Copying {file}')
                try:
                    shutil.copy(source_path, destination_path)
                except Exception as e:
                    print("Error copiando archivo:", e)
                copied_files += 1
                percent_complete = copied_files / total_rpy_files * 100
                percent_remaining = 100 - percent_complete
                print(f'Copied {copied_files}/{total_rpy_files} files ({percent_complete:.2f}% complete, {percent_remaining:.2f}% remaining)')
                time.sleep(0.1)
                
    for filename in os.listdir(source_folder):
        if filename.endswith('.rpy') and not filename.startswith('cleaned_'):
            os.rename(os.path.join(source_folder, filename), 
                    os.path.join(source_folder, filename.split('.')[0] + '.rpy.bak'))
            print(f"Procesando archivo {filename}")
elif eleg == "3":
    import os
    import shutil 
    import time

    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_folder = os.path.join(script_dir, 'game', 'tl', 'chino')
    script_dirs = []
    for dirpath, dirnames, filenames in os.walk(source_folder):
        if any(f.endswith('.rpy') for f in filenames):
            script_dirs.append(dirpath)

        if script_dirs:
            scripts_dir = script_dirs[0] 
        else:
            scripts_dir = source_folder
    destination_folder = 'g:\\projzv3\\traducir'

    if not os.path.exists(source_folder):
        print("Carpeta origen no encontrada")
    
    if os.path.exists(destination_folder):
        print(f"La carpeta {destination_folder} no está vacía. ¿Desea borrar el contenido antes de copiar? (s/n)")
        if input().lower() != "s":
            print("Copia cancelada")
            exit()
        shutil.rmtree(destination_folder)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    rpy_files = []
    copied_files = 0

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.rpy'):
                rpy_files.append(file)
            
    total_rpy_files = len(rpy_files)  
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.rpy'):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                print(f'Copying {file}')
                try:
                    shutil.copy(source_path, destination_path)
                except Exception as e:
                    print("Error copiando archivo:", e)
                copied_files += 1
                percent_complete = copied_files / total_rpy_files * 100
                percent_remaining = 100 - percent_complete
                print(f'Copiando {copied_files}/{total_rpy_files} archivos ({percent_complete:.2f}% completado, {percent_remaining:.2f}% faltan)')
                time.sleep(0.1)
    
    for filename in os.listdir(scripts_dir):
        if filename.endswith('.rpy') and not filename.startswith('cleaned_'):
            os.rename(os.path.join(scripts_dir, filename), os.path.join(scripts_dir, filename.split('.')[0] + '.rpy.bak'))
            print(f"Procesando archivo {filename}")
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

    total = 200

    width = stdscr.getmaxyx()[1] - 20
    
    stdscr.addstr(0, 0, 'Progreso: ') 
    
    for i in range(total):

        keyboard.press('pagedown')
        time.sleep(1.5)
        keyboard.press('pagedown')
        time.sleep(1.5)

        stdscr.addstr(1, 0, '[' + '='*i + '>' + '-'*(total-i) + ']')

        done = i+1
        
        contador = str(done).zfill(len(str(total))) + '/' + str(total)
        
        stdscr.addstr(4, 0, contador)

        stdscr.refresh()
        time.sleep(0.1)

    stdscr.addstr(1, 0, 'Completado!' + ' ' * (width-12))
    curses.endwin()
elif eleg == "8":
    import os
    import shutil 
    import time

    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_folder = os.path.join(script_dir, 'game', 'tl', 'esp')
    destination_folder = 'g:\\projzv3\\antigua'

    if not os.path.exists(source_folder):
        print("Carpeta origen no encontrada")
    
    if os.path.exists(destination_folder):
        print(f"La carpeta {destination_folder} no está vacía. ¿Desea borrar el contenido antes de copiar? (s/n)")
        if input().lower() != "s":
            print("Copia cancelada")
            exit()
        shutil.rmtree(destination_folder)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    rpy_files = []
    copied_files = 0

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.rpy'):
                rpy_files.append(file)
            
    total_rpy_files = len(rpy_files)  
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.rpy'):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                print(f'Copying {file}')
                try:
                    shutil.copy(source_path, destination_path)
                except Exception as e:
                    print("Error copiando archivo:", e)
                copied_files += 1
                percent_complete = copied_files / total_rpy_files * 100
                percent_remaining = 100 - percent_complete
                print(f'Copiando {copied_files}/{total_rpy_files} archivos ({percent_complete:.2f}% completado, {percent_remaining:.2f}% faltan)')
                time.sleep(0.1)
elif eleg == "9":
    import os
    import shutil 
    import time

    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_folder = os.path.join(script_dir, 'game', 'tl', 'chino')
    destination_folder = 'g:\\projzv3\\antigua'

    if not os.path.exists(source_folder):
        print("Carpeta origen no encontrada")
    
    if os.path.exists(destination_folder):
        print(f"La carpeta {destination_folder} no está vacía. ¿Desea borrar el contenido antes de copiar? (s/n)")
        if input().lower() != "s":
            print("Copia cancelada")
            exit()
        shutil.rmtree(destination_folder)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    rpy_files = []
    copied_files = 0

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.rpy'):
                rpy_files.append(file)
            
    total_rpy_files = len(rpy_files)  
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.rpy'):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                print(f'Copying {file}')
                try:
                    shutil.copy(source_path, destination_path)
                except Exception as e:
                    print("Error copiando archivo:", e)
                copied_files += 1
                percent_complete = copied_files / total_rpy_files * 100
                percent_remaining = 100 - percent_complete
                print(f'Copiando {copied_files}/{total_rpy_files} archivos ({percent_complete:.2f}% completado, {percent_remaining:.2f}% faltan)')
                time.sleep(0.1)
elif eleg == "10":
    print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos")
else:
    print("Opción no es valido")
    exec(open("renpytrans.py",encoding="utf-8").read())
