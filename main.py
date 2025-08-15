# É necessário importar a exceção customizada para poder capturá-la
from itemJaExisteError import ItemJaExisteError
from inventario import Inventario
from computador import Computador
from impressora import Impressora

def main():
    """
    Programa principal para testar de forma abrangente todas as classes e métodos
    do sistema de inventário.
    """
    inventario = Inventario()
    print("--- Iniciando teste do sistema de inventário ---")

    # Criando instâncias de equipamentos (usando strings para códigos, que é mais robusto)
    computador1 = Computador("CP001", "IBM", "I5", "16GB")
    computador2 = Computador("CP002", "Acer", "I7", "32GB")
    impressora1 = Impressora("IM001", "PrintJet", "Colorida")
    impressora2 = Impressora("IM002", "HP", "Preto e Branco")

    # --- TESTE 1: Adicionando itens e listagem polimórfica ---
    print("\n--- TESTE 1: Adicionando itens e listando (Polimorfismo) ---")
    inventario.adicionar_item(computador1)
    inventario.adicionar_item(computador2)
    inventario.adicionar_item(impressora1)
    inventario.adicionar_item(impressora2)
    inventario.listar_itens()
    print("-" * 50)

    # --- TESTE 2: Tentando adicionar item com código duplicado (ItemJaExisteError) ---
    print("\n--- TESTE 2: Tentando adicionar item duplicado (ItemJaExisteError) ---")
    try:
        # Tentando adicionar um novo equipamento com o mesmo código de 'computador1'
        computador_duplicado = Computador("CP001", "Dell", "I9", "64GB")
        print(f"Tentando adicionar item com código que já existe: {computador_duplicado.get_codigo_patrimonio()}")
        inventario.adicionar_item(computador_duplicado)
    except ItemJaExisteError as e:
        print(f"SUCESSO: Exceção capturada como esperado!")
        print(f"  -> Tipo da exceção: {e.__class__.__name__}")
        print(f"  -> Mensagem: {e}")
    print("-" * 50)

    # --- TESTE 3: Testando busca e listagem específica ---
    print("\n--- TESTE 3: Testando busca e listagem específica de computadores ---")
    
    print("\n--> Teste do método listar_computadores():")
    inventario.listar_computadores()

    print("\n--> Teste do método buscar_item() com item existente (CP002):")
    item_encontrado = inventario.buscar_item("CP002")
    if item_encontrado:
        print("Item 'CP002' encontrado com sucesso. Detalhes:")
        item_encontrado.imprime()
    else:
        print("FALHA NO TESTE: O item CP002 deveria ter sido encontrado.")

    print("\n--> Teste do método buscar_item() com item inexistente (CP999):")
    item_nao_encontrado = inventario.buscar_item("CP999")
    if item_nao_encontrado is None:
        print("SUCESSO: O item 'CP999' não foi encontrado, como esperado.")
    else:
        print("FALHA NO TESTE: Nenhum item deveria ter sido encontrado.")
    print("-" * 50)

    # --- TESTE 4: Remoção de item e tratamento de erro (ValueError) com recuperação ---
    print("\n--- TESTE 4: Remoção e tratamento de erro (ValueError) com recuperação ---")
    sucesso_remocao = False
    while not sucesso_remocao:
        try:
            codigo_para_remover = input("\nDigite o código de um item para remover (tente um inexistente primeiro, ex: 'IM999'): ")
            inventario.remover_item(codigo_para_remover)
            print(f"\nSUCESSO: Item '{codigo_para_remover}' removido!")
            sucesso_remocao = True
        except ValueError as e:
            print(f"\nERRO CAPTURADO: {e.__class__.__name__}: {e}")
            tentar_novamente = input("Deseja tentar novamente com outro código? (s/n): ").lower()
            if tentar_novamente != 's':
                print("Operação de remoção cancelada pelo usuário.")
                break
    
    print("\n--- Estado Final do Inventário ---")
    inventario.listar_itens()

if __name__ == "__main__":
    main()