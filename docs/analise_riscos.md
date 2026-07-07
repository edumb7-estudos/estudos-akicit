# Análise de Riscos

## Projeto

Micro-API REST para gerenciamento de tarefas desenvolvida com FastAPI e SQLite.

## Objetivo

Identificar os principais riscos técnicos do projeto, avaliar seus impactos e definir estratégias para reduzir a probabilidade de ocorrência e seus efeitos.

## Matriz de Riscos

| Risco | Probabilidade | Impacto | Estratégia de Resposta |
|-------|:-------------:|:-------:|------------------------|
| Entrada de dados inválidos na API | Média | Alto | Utilizar validação com Pydantic e testes automatizados. |
| Alterações no código causarem regressões | Média | Alto | Executar testes automatizados antes de cada atualização. |
| Falta de documentação dificultar manutenção | Média | Médio | Manter README e documentação técnica sempre atualizados. |
| Crescimento da aplicação exceder limitações do SQLite | Baixa | Médio | Planejar migração para um banco de dados mais robusto em futuras versões. |
| Falhas durante alterações no banco de dados | Baixa | Alto | Realizar backups e validar mudanças em ambiente de desenvolvimento antes da implantação. |

## Estratégia Prioritária

A principal estratégia adotada foi a utilização de testes automatizados para reduzir o risco de regressões e aumentar a confiabilidade das alterações realizadas durante o desenvolvimento.

## Uso da Inteligência Artificial Generativa

A IA Generativa foi utilizada para auxiliar na identificação dos riscos, sugerir estratégias de mitigação e apoiar a elaboração da documentação do projeto. Todas as sugestões foram revisadas e adaptadas ao contexto da aplicação antes de serem incorporadas.

## Conclusão

A análise de riscos permitiu identificar os principais pontos de atenção do projeto e definir ações preventivas para aumentar sua qualidade, confiabilidade e facilidade de manutenção.
