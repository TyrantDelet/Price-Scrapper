# Projeto: Rastreador de preços de produtos 

### Autor: Arthur Kayky Carvalho Silva

### Data de Revisão: 22/07/2026

## Visão geral e objetivo

**O problema:** Atualmente usuários tem grande dificuldade para buscar o melhor preço para determinado produto, ficando propícios a propagandas falsas e abusivas, ou não conseguindo localizar a melhor oferta possível naquele momento devido a diferentes fontes de dados.  

**A solução:** Um programa em python que faz a indexação de produtos gerais em diversos marketplaces para facilitar a busca pela melhor oferta para o usuário. Se o preço cair abaixo de um limite pré-estabelecido o sistema cria um alerta de preço.

## Casos de uso (User Stories)

**História 01:** Como usuário eu quero fornecer o SKU (ou URL/ID única de um marketplace), junto de um preço máximo que eu aceito pagar, para que o sistema possa me alertar.

**História 02:** Como usuário eu quero acessar o histórico de preços de um determinado produto com a exibição de dados de um marketplace responsável ou código promocional.

**História 03:** Como usuário eu quero comparar preços atuais de produtos juntamente com seus históricos para que eu exerça a melhor tomada de decisão em custo benefício.


## Escopo do MVP (Produto Mínimo Viável)

O que é **ESTRITAMENTE** necessário para versão 1.0:

- Definir o arquivo `.env` com variáveis para deploy do aplicativo
- Definir `requirements.txt` travado com versionamento para `Python 3.12`
- Definir o esquema de dados SQL inicial que a aplicação vai utilizar
- Definir queries SQL não bloqueantes de inserção, atualização e exclusão de dados garantindo a integridade 
- Estruturação de queries que são utilizadas para dispor dados aos usuários

## Critérios de aceitação (Definition of done)

O projeto será considerado concluido na versão 1.0 quando: 
- [ ] O projeto execute o setup sem nenhum erro de dependência ou de sintaxe.
- [ ] O programa conseguir tratar conversões de dados diferentes (TypeCasting) para inserção no banco de dados ignorando caracteres como símbolos monetários etc.
- [ ] O schema SQL estiver aceitando dados abstraídos consolidados para suportar múltiplas fontes.
- [ ] Estruturação de queries para dados a usuários com sanitização contra SQL injection.
- [ ] Execução de teste de entrega de dados atendendo a história dos usuários.

