# import subprocess
# import time
# import pyautogui
# from playwright.sync_api import sync_playwright



# pyautogui.PAUSE = 0.3 # a cada comando demora 3 milisegundos


# pyautogui.press("win")
# pyautogui.write("chrome")

# time.sleep(2)
# pyautogui.press("enter")
# time.sleep(2)

# # ACESSO MINHA OUTRA CONTA - JO.IA
# pyautogui.click(x=767, y=565)

# pyautogui.write("https://www.esocial.gov.br/portal/")
# pyautogui.press("enter")

# # ENTRANDO NO ESOCIAL E CLICAR NO BOTÃO LOGIN
# time.sleep(3)
# pyautogui.click(x=-580, y=343)
# time.sleep(5)

# # CLICANDO NO BOTA ̃O CERTIFICADO
# pyautogui.click(x=-588, y=666)

# # HABILITANDO O CERTIFICADO
# time.sleep(3)
# pyautogui.click(x=-841, y=365)


# v2

# import time
# import time
# import subprocess
# import requests
# import pyautogui
# from playwright.sync_api import sync_playwright

# pyautogui.PAUSE = 0.3

# # 🔥 CAMINHO DO CHROME
# chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# # 🔥 COMANDO PARA ABRIR COM DEBUG
# cmd = [
#     chrome_path,
#     "--remote-debugging-port=9222",
#     "--user-data-dir=C:\\chrome-debug"
# ]

# # 🔥 ABRE O CHROME (MUITO MELHOR QUE PYautogui)
# subprocess.Popen(cmd)

# print("Abrindo Chrome com debug...")

# # 🔥 ESPERA O DEBUG FICAR DISPONÍVEL
# for i in range(15):
#     try:
#         requests.get("http://127.0.0.1:9222/json")
#         print("✅ Chrome pronto para conexão!")
#         break
#     except:
#         time.sleep(1)
# else:
#     raise Exception("❌ Chrome não abriu com debug na porta 9222")

# # 🔥 AGORA USA PYAUTOGUI PARA NAVEGAR (SE PRECISAR)
# time.sleep(2)

# # abre nova aba
# pyautogui.hotkey("ctrl", "l")
# pyautogui.write("https://www.esocial.gov.br/portal/")
# pyautogui.press("enter")

# print("Abrindo eSocial...")

# time.sleep(6)

# # 🔥 LOGIN (AJUSTE COORDENADAS!)
# print("Realizando login manual com certificado...")

# pyautogui.click(x=1356, y=333)  # botão entrar
# time.sleep(5)

# pyautogui.click(x=1348, y=650)  # selecionar certificado
# time.sleep(6)

# pyautogui.click(x=1079, y=349)  # confirmar certificado
# time.sleep(3)


# print("Login concluído!")

# # 🔥 CONECTA COM PLAYWRIGHT
# with sync_playwright() as p:
#     print("Conectando ao Chrome via CDP...")

#     browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")

#     context = browser.contexts[0]
#     pages = context.pages

#     print(f"Total de abas abertas: {len(pages)}")

#     # 🔥 ENCONTRA ABA DO ESOCIAL
#     page = None
#     for p_ in pages:
#         print("Aba encontrada:", p_.url)
#         if "esocial" in p_.url:
#             page = p_
#             break

#     if page is None:
#         page = pages[-1]

#     # 🔥 ESPERA CARREGAR COMPLETAMENTE
#     page.wait_for_load_state("networkidle")

#     print("✅ Página conectada:", page.url)

#     # 🔥 NAVEGA NA PÁGIN
#     page.locator('xpath=//*[@id="menuFolhaPagamento"]').click() # MENU GESTÆO FOLHA
#     time.sleep(0.5)
#     page.locator('xpath=//*[@id="menuGestaoFolha"]').click() # submenu
#     time.sleep(2)
#     page.locator('xpath=//*[@id="conteudo-pagina"]/div[3]/div[1]/div[5]/a').click() # ano 2025
#     time.sleep(1) 
#     page.locator('xpath=//*[@id="conteudo-pagina"]/div[3]/div[2]/div[3]/a').click() # clica no mes
#     time.sleep(2)
#     page.locator('xpath=//*[@id="ui-accordion-1-panel-0"]/div/div/ul/li[1]/a').click() # clica em trabalhadores
#     time.sleep(2)
#     page.locator('xpath=//*[@id="ui-accordion-1-panel-0"]/div/div/ul/li[1]/ul/li[2]/a').click( )# clica em pagamento


   
#############################################################################S


# v3

import time
import subprocess
import requests
import pyautogui
from playwright.sync_api import sync_playwright
from clicar_exe import executar_assinador

pyautogui.PAUSE = 0.3

# 🔥 CAMINHO DO CHROME
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# 🔥 ABRE CHROME COM DEBUG
cmd = [
    chrome_path,
    "--remote-debugging-port=9222",
    "--user-data-dir=C:\\chrome-debug"
]

subprocess.Popen(cmd)
print("Abrindo Chrome com debug...")

# 🔥 ESPERA CHROME RESPONDER
for i in range(15):
    try:
        requests.get("http://127.0.0.1:9222/json")
        print("✅ Chrome pronto para conexão!")
        break
    except:
        time.sleep(1)
else:
    raise Exception("❌ Chrome não abriu com debug")

# 🔥 ABRE ESOCIAL
time.sleep(2)
pyautogui.hotkey("ctrl", "l")
pyautogui.write("https://www.esocial.gov.br/portal/")
pyautogui.press("enter")

print("Abrindo eSocial...")
time.sleep(6)

# 🔥 LOGIN MANUAL
print("Realizando login manual...")

pyautogui.click(x=1356, y=333)
time.sleep(4)

pyautogui.click(x=1348, y=650)
time.sleep(30)

pyautogui.click(x=1079, y=349)
time.sleep(3)

print("Login concluído!")

# 🔥 PLAYWRIGHT
with sync_playwright() as p:
    print("Conectando ao Chrome via CDP...")

    browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    context = browser.contexts[0]
    pages = context.pages

    print(f"Total de abas abertas: {len(pages)}")

    # 🔥 ACHA ABA DO ESOCIAL
    page = None
    for p_ in pages:
        print("Aba encontrada:", p_.url)
        if "esocial" in p_.url:
            page = p_
            break

    if page is None:
        page = pages[-1]

    page.wait_for_load_state("networkidle")
    print("✅ Página conectada:", page.url)

    # 🔥 AUTO CONFIRMAR ALERTAS (EXCLUIR)
    page.on("dialog", lambda dialog: dialog.accept())

    # 🔥 NAVEGAÇÃO
    page.locator('xpath=//*[@id="menuFolhaPagamento"]').click()
    time.sleep(0.5)

    page.locator('xpath=//*[@id="menuGestaoFolha"]').click()
    time.sleep(2)

    page.locator('xpath=//*[@id="conteudo-pagina"]/div[3]/div[1]/div[5]/a').click()
    time.sleep(1)

    page.locator('xpath=//*[@id="conteudo-pagina"]/div[3]/div[2]/div[3]/a').click()
    time.sleep(2)

    page.locator('xpath=//*[@id="ui-accordion-1-panel-0"]/div/div/ul/li[1]/a').click()
    time.sleep(2)

    page.locator('xpath=//*[@id="ui-accordion-1-panel-0"]/div/div/ul/li[1]/ul/li[2]/a').click()
    time.sleep(3)

    # 🔥 LOOP
    # found = False

    # while True:

    assinador = False
    print("🔍 Verificando página atual...")

    page.wait_for_selector("tbody tr")

    rows = page.locator("tbody tr")
    total = rows.count()

    print(f"Total de linhas: {total}")

    # for i in range(total):
    row = rows.nth(i)

    botao_ver = row.locator("a:has-text('Ver Pagamentos')")

    if botao_ver.count() > 0:
        print("✅ Encontrado! Abrindo menu...")

                # 1️⃣ abre dropdown
        dropdown = row.locator("button.dropdown-toggle")
        dropdown.click()

                # 2️⃣ espera menu aparecer
        menu = row.locator("ul.dropdown-menu")
        menu.wait_for(state="visible")

                # 3️⃣ clica em excluir
        excluir = row.locator("a:has-text('Excluir Pagamentos')")
        excluir.click()

        print("⚠️ Ação executada uma única vez")

        #break  # 🔥 PARA AQUI (não continua nas outras linhas)

                # 🔥 ESPERA MODAL
                #modal = page.locator("div.ui-dialog:visible")
                #modal.wait_for()

                #print("⚠️ Modal apareceu")

                # 🔥 PEGA TODOS OS BOTÕES DO MODAL
                #botoes = modal.locator("div.ui-dialog-buttonset button")

                # 🔥 O SEGUNDO É CONFIRMAR (index 1)
                #confirmar = botoes.nth(1)

                #confirmar.click()

                #print("✅ Confirmou")

                # 🔥 ESPERA SUMIR
                #page.locator("div.ui-widget-overlay").wait_for(state="hidden")
                #modal.wait_for(state="hidden")

                #print("✅ Modal fechado")

                
                # 3 espera botão confirmar
                #confirmar = page.locator("button.btn.btn-primary:has-text('Confirmar')")
                #confirmar.wait_for(state="visible")

                # # 4 clica confirmar
                #confirmar.click()



        #         # 🔥 AGORA executa assinador
        #         executar_assinador(True)

        #         print("🔙 Voltando para lista...")

        #         page.go_back()
        #         page.wait_for_selector("tbody tr")


         


        #found = True
        #         break

        # if found:
        #     print("🎯 Finalizado com sucesso!")
        #     break

        # print("➡️ Não encontrou, indo para próxima página...")

        # next_button = page.locator('xpath=//*[@id="proxima-pagina"]')

        # if next_button.count() == 0:
        #     print("❌ Botão próxima página não encontrado")
        #     break

        # if not next_button.is_visible():
        #     print("❌ Próxima página não visível")
        #     break

        # next_button.click()

        # # espera carregar nova tabela
        # page.wait_for_selector("tbody tr")
