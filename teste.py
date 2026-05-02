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




import time
import time
import subprocess
import requests
import pyautogui
from playwright.sync_api import sync_playwright

pyautogui.PAUSE = 0.3

# 🔥 CAMINHO DO CHROME
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# 🔥 COMANDO PARA ABRIR COM DEBUG
cmd = [
    chrome_path,
    "--remote-debugging-port=9222",
    "--user-data-dir=C:\\chrome-debug"
]

# 🔥 ABRE O CHROME (MUITO MELHOR QUE PYautogui)
subprocess.Popen(cmd)

print("Abrindo Chrome com debug...")

# 🔥 ESPERA O DEBUG FICAR DISPONÍVEL
for i in range(15):
    try:
        requests.get("http://127.0.0.1:9222/json")
        print("✅ Chrome pronto para conexão!")
        break
    except:
        time.sleep(1)
else:
    raise Exception("❌ Chrome não abriu com debug na porta 9222")

# 🔥 AGORA USA PYAUTOGUI PARA NAVEGAR (SE PRECISAR)
time.sleep(2)

# abre nova aba
pyautogui.hotkey("ctrl", "l")
pyautogui.write("https://www.esocial.gov.br/portal/")
pyautogui.press("enter")

print("Abrindo eSocial...")

time.sleep(6)

# 🔥 LOGIN (AJUSTE COORDENADAS!)
print("Realizando login manual com certificado...")

pyautogui.click(x=1356, y=333)  # botão entrar
time.sleep(5)

pyautogui.click(x=1348, y=650)  # selecionar certificado
time.sleep(6)

pyautogui.click(x=1079, y=349)  # confirmar certificado
time.sleep(3)


print("Login concluído!")

# 🔥 CONECTA COM PLAYWRIGHT
with sync_playwright() as p:
    print("Conectando ao Chrome via CDP...")

    browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")

    context = browser.contexts[0]
    pages = context.pages

    print(f"Total de abas abertas: {len(pages)}")

    # 🔥 ENCONTRA ABA DO ESOCIAL
    page = None
    for p_ in pages:
        print("Aba encontrada:", p_.url)
        if "esocial" in p_.url:
            page = p_
            break

    if page is None:
        page = pages[-1]

    # 🔥 ESPERA CARREGAR COMPLETAMENTE
    page.wait_for_load_state("networkidle")

    print("✅ Página conectada:", page.url)

    # 🔥 NAVEGA NA PÁGIN
    page.locator('xpath=//*[@id="menuFolhaPagamento"]').click() # MENU GESTÆO FOLHA
    time.sleep(0.5)
    page.locator('xpath=//*[@id="menuGestaoFolha"]').click() # submenu
    time.sleep(2)
    page.locator('xpath=//*[@id="conteudo-pagina"]/div[3]/div[1]/div[5]/a').click() # ano 2025
    time.sleep(1) 
    page.locator('xpath=//*[@id="conteudo-pagina"]/div[3]/div[2]/div[3]/a').click() # clica no mes
    time.sleep(2)
    page.locator('xpath=//*[@id="ui-accordion-1-panel-0"]/div/div/ul/li[1]/a').click() # clica em trabalhadores
    time.sleep(2)
    page.locator('xpath=//*[@id="ui-accordion-1-panel-0"]/div/div/ul/li[1]/ul/li[2]/a').click( )# clica em pagamento


   

# while True:
#     print("🔍 Verificando página atual...")

#     # espera tabela carregar
#     page.wait_for_selector("tbody tr")

#     rows = page.locator("tbody tr")
#     total = rows.count()

#     print(f"Total de linhas: {total}")

#     for i in range(total):
#         row = rows.nth(i)

#         texto = row.inner_text()

#         print(f"Linha {i}: {texto}")

#         if "Ver pagamentos" in texto:
#             print("✅ Encontrado!")

#             # clica no botão/link dentro da linha
#             try:
#                 row.locator("text=Ver pagamentos").click()
#             except:
#                 # fallback se for botão
#                 row.locator("button:has-text('Ver pagamentos')").click()

#             found = True
#             break

#     if found:
#         break

#     print("➡️ Não encontrou, indo para próxima página...")

#     # tenta clicar no botão próximo
#     next_button = page.locator("text=Próximo")

#     if next_button.count() == 0:
#         print("❌ Não existe botão Próximo. Finalizando.")
#         break

#     # verifica se está desabilitado
#     if "disabled" in next_button.get_attribute("class", ""):
#         print("❌ Próximo desabilitado. Finalizando.")
#         break

#     next_button.click()

#     # espera recarregar a tabela
#     page.wait_for_timeout(2000)

#     input("Pressione ENTER para sair...")