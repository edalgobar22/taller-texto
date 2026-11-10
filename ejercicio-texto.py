ruta_arch = "C:\\Campuslands\\archivos_texto\\mbox.txt"

with open(ruta_arch, "r", encoding="utf-8") as arch:
    lst_emails = []
    for linea in arch:
        if linea.startswith("From:"):
            emails = (linea.split(" ")[1])
            if emails not in lst_emails:
                lst_emails.append(emails)

lst_emails.reverse()
    
for emails in lst_emails:
    print(f"{emails.strip()} Enviado [ok]")

ruta_arch = "C:\\Campuslands\\archivos_texto\\mbox.txt"
ruta_dest = "C:\\Campuslands\\archivos_texto\\correos_enviados.txt"

with open(ruta_dest, "w", encoding="utf-8") as dest:
    for emails in lst_emails:
        dest.writelines(f"{emails.strip()} Enviado [ok] \n")
    
    