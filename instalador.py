import os
import sys

print("=========================================")
print("🤖 KSP AI FACTORY - INSTALADOR UNIVERSAL")
print("=========================================\n")

def encontrar_ksp_em_qualquer_lado():
    # 1. Caminhos mais comuns (Steam, Hydra, Alternativos)
    caminhos_comuns = [
        "C:/Program Files (x86)/Steam/steamapps/common/Kerbal Space Program",
        "C:/Games/Kerbal Space Program",
        "D:/Games/Kerbal Space Program",
        "C:/Hydra Games/Kerbal Space Program",
        "D:/Hydra Games/Kerbal Space Program"
    ]
    
    # Verifica primeiro os caminhos mais fáceis
    for caminho in caminhos_comuns:
        if os.path.exists(os.path.join(caminho, "GameData")):
            return caminho

    # 2. Se não encontrou, faz uma busca automática rápida nos discos principais
    print("🔍 A fazer varrimento inteligente no sistema para detetar o KSP...")
    for disco in ["C:\\", "D:\\"]:
        if os.path.exists(disco):
            # Procura pastas comuns de jogos piratas ou alternativos
            for pasta_raiz in ["Games", "Program Files (x86)", "Program Files", "Hydra Games"]:
                caminho_teste = os.path.join(disco, pasta_raiz, "Kerbal Space Program")
                if os.path.exists(os.path.join(caminho_teste, "GameData")):
                    return caminho_teste
                    
    return None

# Executa a busca universal
KSP_PATH = encontrar_ksp_em_qualquer_lado()

if KSP_PATH:
    print(f"✅ [Sucesso] Jogo detetado em: {KSP_PATH}")
    GAMEDATA_PATH = os.path.join(KSP_PATH, "GameData")
    
    # Cria a pasta do Mod sem restrições
    pasta_mod = os.path.join(GAMEDATA_PATH, "AIBeyondLimits")
    if not os.path.exists(pasta_mod):
        os.makedirs(pasta_mod)
    
    # Escreve o cérebro da IA na pasta correta
    ia_file_path = os.path.join(pasta_mod, "ksp_ai_core.py")
    
    codigo_da_ia = f"""# Código universal configurado para este PC
import os
KSP_DIR = "{KSP_PATH.replace('\\', '/')}"
print("🤖 IA CORE EM EXECUÇÃO NO KSP EM: " + KSP_DIR)
"""
    
    with open(ia_file_path, "w", encoding="utf-8") as f:
        f.write(codigo_da_ia)
        
    print(f"✅ CONEXÃO CONCLUÍDA: O cérebro da IA foi injetado!")
else:
    print("❌ Não consegui encontrar o KSP automaticamente no teu sistema.")
    print("💡 Dica: Corre este instalador diretamente dentro da pasta principal do teu KSP!")

input("\nInstalação concluída. Prime ENTER para fechar...");
