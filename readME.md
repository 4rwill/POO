Claro. Com base na análise de todos os laboratórios fornecidos, elaborei uma avaliação no mesmo formato, projetada para abranger todos os principais conceitos de Programação Orientada a Objetos que foram apresentados: definição de classes, interação entre objetos, herança, polimorfismo, tratamento de exceções e o gerenciamento de coleções.

---

### **Prova de Laboratório: Programação Orientada a Objetos**

**Instruções Gerais:**

* Esta prova consiste em 4 atividades. Cada classe deve ser implementada em seu próprio arquivo Python.
* O programa principal de teste deve ser implementado em um arquivo separado chamado `main.py`.
* Siga as boas práticas de design de classes, como o uso de atributos privados e métodos de acesso/modificadores, alta coesão e baixo acoplamento.
* Avaliações que não seguirem a padronização de arquivos e as boas práticas de design não serão consideradas.

---

### **Contexto: Sistema de Gerenciamento de Ativos de TI**

Você foi encarregado de desenvolver um sistema simples para gerenciar os ativos de TI de uma empresa. O sistema precisa catalogar diferentes tipos de equipamentos, como Computadores e Impressoras.

---

### **Atividade 1: Classe Base `Equipamento`**

Nesta atividade, você criará a superclasse que servirá de base para todos os tipos de equipamentos.

1.  **Crie a classe `Equipamento` no arquivo `equipamento.py`.**
2.  **Atributos:** A classe deve ter os seguintes atributos privados:
    * `_codigo_patrimonio` (string): um identificador único para o equipamento.
    * `_fabricante` (string): o nome do fabricante.
    * `_ativo` (booleano): um flag para indicar se o equipamento está em uso (ativo) ou não.
3.  **Construtor:** O construtor deve inicializar `_codigo_patrimonio` e `_fabricante` através de parâmetros. O atributo `_ativo` deve ser inicializado como `True` por padrão.
4.  **Métodos:**
    * Implemente os métodos de acesso (`get`) e modificadores (`set`) para todos os atributos.
    * Crie um método `imprime(self)` que exiba de forma organizada todas as informações do equipamento.
    * Crie um método abstrato (conceitualmente) chamado `calcular_depreciacao(self)` que não fará nada na superclasse, mas deverá ser implementado obrigatoriamente pelas subclasses.

[cite_start]*(Esta atividade avalia a definição de classes, construtores, atributos privados e métodos de acesso/modificadores, conforme visto nos Labs 01, 02 e 08)*[cite: 2267, 2268, 2269, 2334].

---

### **Atividade 2: Subclasses `Computador` e `Impressora`**

Agora, você criará classes especializadas que herdam de `Equipamento`.

1.  **Crie a classe `Computador` no arquivo `computador.py`.**
    * [cite_start]Ela deve ser uma subclasse de `Equipamento`[cite: 42, 49].
    * Adicione os seguintes atributos privados: `_processador` (string) e `_memoria_ram` (string, ex: "16GB").
    * [cite_start]Implemente um construtor que receba os parâmetros necessários para inicializar tanto os atributos da superclasse `Equipamento` quanto os seus próprios[cite: 1652, 1658].
    * Forneça métodos `get` e `set` para os novos atributos.
    * [cite_start]**Sobrescreva** o método `imprime(self)` para exibir também as informações específicas do computador[cite: 2341].
    * [cite_start]**Implemente** o método `calcular_depreciacao(self)`, que simplesmente imprime a mensagem: "Depreciação de 15% ao ano para Computador."[cite: 2342].

2.  **Crie a classe `Impressora` no arquivo `impressora.py`.**
    * Ela deve ser uma subclasse de `Equipamento`.
    * Adicione o seguinte atributo privado: `_tipo_impressao` (string, ex: "Jato de Tinta", "Laser").
    * Implemente seu construtor, métodos de acesso e modificadores, de forma semelhante à classe `Computador`.
    * [cite_start]**Sobrescreva** o método `imprime(self)` para incluir o tipo de impressão[cite: 2341].
    * [cite_start]**Implemente** o método `calcular_depreciacao(self)`, que imprime a mensagem: "Depreciação de 10% ao ano para Impressora."[cite: 2342].

[cite_start]*(Esta atividade avalia Herança, sobrescrita de métodos e Polimorfismo, conforme visto nos Labs 07 e 08)*[cite: 29, 2326].

---

### **Atividade 3: Classe de Gerenciamento `Inventario`**

Esta classe será responsável por agrupar e gerenciar todos os equipamentos.

1.  **Crie a classe `Inventario` no arquivo `inventario.py`.**
2.  [cite_start]**Atributo:** A classe deve ter um único atributo privado: `_equipamentos`, que deve ser uma `list` inicializada como vazia no construtor[cite: 59, 60, 2296].
3.  **Métodos:**
    * `adicionar_item(self, item)`: Adiciona um equipamento à lista. [cite_start]Antes de adicionar, verifique se o `item` é uma instância da classe `Equipamento` usando `isinstance()`[cite: 32, 2360].
    * `remover_item(self, codigo_patrimonio)`: Remove um equipamento da lista com base no seu código de patrimônio.
    * [cite_start]`listar_todos_itens(self)`: Percorre a lista de equipamentos e chama o método `imprime()` de cada um para exibir suas informações[cite: 65, 1576]. Este método demonstrará o comportamento polimórfico.
    * `buscar_item(self, codigo_patrimonio)`: Procura por um equipamento pelo código de patrimônio e, se encontrar, retorna o objeto. Caso contrário, retorna `None`.
    * [cite_start]`listar_computadores(self)`: Percorre a lista e imprime as informações apenas dos objetos que são instâncias da classe `Computador`[cite: 65, 2366].

[cite_start]*(Esta atividade avalia o agrupamento de objetos em coleções, iteração, design de classes e o uso de `isinstance` para polimorfismo, conforme visto nos Labs 05, 06, 07 e 09)*[cite: 2289, 1547, 32, 2355].

---

### **Atividade 4: Tratamento de Exceções e Programa Principal**

Nesta etapa final, você implementará o tratamento de erros e o programa de teste.

1.  **Modifique a classe `Inventario`:**
    * Crie uma exceção customizada chamada `ItemJaExisteError` que herda de `Exception`.
    * No método `adicionar_item`, antes de adicionar um novo equipamento, verifique se já existe um item com o mesmo `_codigo_patrimonio` na lista. [cite_start]Se existir, lance a exceção `ItemJaExisteError` com uma mensagem apropriada[cite: 17].
    * [cite_start]No método `remover_item`, se o código de patrimônio fornecido não for encontrado na lista, lance a exceção `ValueError` com a mensagem "Equipamento não encontrado no inventário."[cite: 17].

2.  [cite_start]**Crie o programa principal `main.py`:** [cite: 6]
    * Crie uma instância da classe `Inventario`.
    * Crie pelo menos duas instâncias de `Computador` e duas de `Impressora` com dados diferentes.
    * Teste todos os métodos da classe `Inventario`.
    * [cite_start]Use blocos `try...except` para testar os casos de exceção[cite: 22, 23]:
        * Tente adicionar um equipamento com um código de patrimônio que já existe e capture a exceção `ItemJaExisteError`, exibindo uma mensagem de erro amigável para o usuário.
        * Tente remover um equipamento com um código que não existe e capture a exceção `ValueError`.
    * [cite_start]Demonstre uma tentativa de recuperação de erro: ao tentar remover um item e receber o `ValueError`, use um laço para perguntar ao usuário "Equipamento não encontrado. Deseja tentar novamente com outro código? (s/n)"[cite: 23].

[cite_start]*(Esta atividade avalia o tratamento de exceções, a criação de exceções customizadas e a implementação de um programa de teste robusto, conforme visto no Lab 10)*[cite: 4, 17, 23].