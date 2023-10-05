# Beléptetőrendszer

def regisztracio():
    ok_regisztracio = True
    username()
    jelszo_kerese()
    ciklus = 1
    while not jelszo_ellenorzes():
        ciklus += 1
        if ciklus > 3:
            ok_regisztracio = False
            break
    return ok_regisztracio


def username():
    felhasznalo_email = input("Kérem az email címét! ")
    while " " in felhasznalo_email or "@" not in felhasznalo_email or "." not in felhasznalo_email:
        felhasznalo_email = input("A belépési adatok nem ismerhetőek fel. \nBiztos jól írtad be? ")


def jelszo_kerese():
    felhasznalo_jelszo= input("Kérem a jelszavát! (1,a,A, min. 8 karakter)")
    ok_jelszo = True
    while ok_jelszo:
        if len(felhasznalo_jelszo) < 8:
            ok_jelszo = False
        szamjegy = 0
        for i in range(len(felhasznalo_jelszo)):
            if felhasznalo_jelszo[i].isnumeric():
                szamjegy += 1
        if szamjegy == 0:
                ok_jelszo = False
        if not ok_jelszo:
            felhasznalo_jelszo = input("Helytelen karakter formátum! \nA jelszóban legyenek kis- és nagybetűk, valamint számok!")
            ok_jelszo = True
        else:
            ok_jelszo = False


def jelszo_ellenorzes():
    ok_jelszo = True
    return ok_jelszo


def beleptetes():
    pass


# A program itt indul :)
felhasznalo_email = ""
felhasznalo_jelszo = ""
username()
jelszo_kerese()
if regisztracio():
    beleptetes()