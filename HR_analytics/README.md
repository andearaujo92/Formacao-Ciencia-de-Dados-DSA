# **Projeto de Predição de Insatisfação e Pedido de Demissão de Colaborador**

Nesse Projeto a Companhia precisava entender quais os motivos de insatisfação dos funcionários.
Os Dados coletados pela Companhia possui as seguintes variáveis:

**Variáveis Coletadas**

Age: Idade do funcionário,    
Attrition: Tipo de atrito (demissão voluntária, etc.),    
Business Travel: Frequência de viagens a negócios,    
Department: Departamento de trabalho,    
Distance From Home: Distância de casa ao trabalho,    
Education: Nível de educação,    
Education Field: Área de estudo,    
Environment Satisfaction: Satisfação com o ambiente de trabalho,    
Gender: Gênero do funcionário,    
Job Involvement: Envolvimento no trabalho,    
Job Level: Nível do trabalho,    
Job Role: Função do trabalho,    
Job Satisfaction: Satisfação com o trabalho,    
Marital Status: Estado civil,    
Monthly Income: Renda mensal,        
Num Companies Worked: Número de empresas em que já trabalhou,    
Over 18: Se o funcionário é maior de 18 anos,    
Over Time: Se faz hora extra,      
Percent Salary Hike: Percentual de aumento salarial,        
Performance Rating: Avaliação de desempenho,      
Relationship Satisfaction: Satisfação com os relacionamentos no trabalho,        
Standard Hours: Horas padrão de trabalho      

# **Premissas do Target**
O Target escolhido foram funcionários empregados atualmente e funcionários que pediram demissão.

Funcionários Empregados = 0    
Funcionários que Pediram demissão = 1       

Os funcionários demitidos pela Companhia não foram avaliados como Target, e foram descartados da base de dados.

# **Análise Exploratória**
Foi Plotado alguns Boxplots para entender os outliers e a influência de cada variável no Target.

![image](https://github.com/user-attachments/assets/5d230d01-17d7-40c8-a4f5-4318dab9313b)

Decidi manter os outliers pois os outliers não eram irreais, mas faziam parte do comportameto das variáveis.

![image](https://github.com/user-attachments/assets/a21781c7-749d-4f72-baec-e0a006b04295)

### **Conclusões**
Algumas conclusões com base nas diferenças mais significativas entre os dois grupos:

1. **Idade:**
   Funcionários que se demitem voluntariamente são significativamente mais jovens (33,93 anos) do que aqueles que permanecem (37,64 anos). Funcionários mais jovens podem estar mais propensos a buscar novas oportunidades.

2. **Distância de Casa (DistanceFromHome):**
   A distância média de casa para o trabalho é maior para aqueles que se demitem (10,55) em comparação com os que permanecem (8,94). Distâncias mais longas podem ser um fator importante na decisão de sair.

3. **Renda Mensal (Monthly Income):**
   Funcionários que permanecem na empresa têm uma renda mensal média significativamente maior (6587,85) em comparação aos que se demitem (5503,74). Isso sugere que uma remuneração mais alta pode ajudar a reter talentos.

4. **Anos na Empresa (Years at Company):**
   Funcionários que se demitem têm, em média, um tempo de trabalho menor (6 anos) em comparação aos funcionários atuais (7,09 anos). Isso indica que funcionários com maior tempo de casa têm mais chances de permanecer.

5. **Nível de Cargo (Job Level):**
   Funcionários que permanecem tendem a ocupar posições mais altas (2,09) em relação aos que se demitem (1,82). Isso sugere que o crescimento na carreira pode desempenhar um papel importante na retenção.

## **Teste Chi-Squared**
Avaliei a relação das variáveis categóricas com Target através do Teste do Qui-Quadrado tirando as seguintes conclusões:

### **Conclusões**:

1. **BusinessTravel x Attrition:**
   Quem viaja com frequência para o trabalho tem mais chance de pedir demissão. Isso pode deixar o funcionário mais cansado e insatisfeito.

2. **Department x Attrition:**
   Funcionários de Recursos Humanos e Vendas tem mais chances de pedir demissão do que os de Pesquisa e Desenvolvimento. Isso pode se dar devido aos salários.

3. **EducationField x Attrition:**
   Pessoas com diploma técnico ou na área de Marketing têm mais chances de sair do que aquelas em Ciências da Vida ou Medicina. Pode ser devido aos salários mais altos para médicos.

4. **Gender x Attrition:**
   O gênero não influencia diretamente a decisão de sair da empresa. O ideal é que o gênero não influencie na demissão pois isso indica que a empresa está com uma política de gênero adequada.

5. **JobRole x Attrition:**
   Técnicos de laboratório e representantes de vendas pedem demissão mais do que os gestores. Isso pode se dar devido aos melhores salários e benefícios de gestores.

6. **MaritalStatus x Attrition:**
   Solteiros têm mais chance de pedir demissão do que casados. Solteiros, normalmente tem menos impedimentos e compromissos com família e localidade.

7. **OverTime x Attrition:**
   Quem faz horas extras frequentemente tem mais chance de sair. Certamente isso se dá devido ao cansaço.

8. **Employee Source x Attrition:**
   Contratados por indicação pedem mais demissão. Amigos podem ter passado uma imagem da empresa e o contratado encontrou outro cenário que não agradou.

# **Modelagem**

## Modelo de Regressão Logística

Precision: 0.63    
Recall: 0.11    
Specificity: 0.98    
Acurracy: 0.85    

![image](https://github.com/user-attachments/assets/2c3c8c82-cc29-44b9-b3db-8b21cc42a495)

![image](https://github.com/user-attachments/assets/a033533f-6cda-4c47-9e17-9720b1085e82)

![image](https://github.com/user-attachments/assets/4dec414f-0857-4d8e-a091-6bf821767031)

Os coeficientes na regressão logística indicam a força e a direção da associação entre cada feature (atributo) e a probabilidade do evento alvo, que neste caso é a demissão voluntária (Attrition). 

Ou seja, a análise dos coeficientes de um modelo de regressão logística nos ajuda a entender a influência de cada atributo na probabilidade do evento de interesse. Coeficientes positivos indicam que, conforme o valor do atributo aumenta, a probabilidade do funcionário se demitir voluntariamente também aumenta.  

Vamos interpretar os 10 coeficientes com os maiores valores:  

**BusinessTravel_Travel_Frequently (0.494839)**  
Funcionários que viajam frequentemente a trabalho têm maior probabilidade de pedir demissão voluntária. Esse coeficiente é bastante significativo, sugerindo que viagens frequentes podem ser fonte de estresse ou insatisfação.  

**EducationField_Technical Degree (0.275768)**  
Funcionários com formação técnica têm maior probabilidade de pedir demissão voluntária em comparação com aqueles de outras áreas educacionais. Isso pode indicar que esses profissionais têm mais oportunidades no mercado de trabalho ou que suas expectativas não estão sendo atendidas.  

**Employee Source_Referral (0.257281)**  
Funcionários contratados por indicação têm maior probabilidade de pedir demissão voluntária. Isso pode sugerir que, apesar de serem recomendados, podem não estar tão alinhados com a empresa quanto outros funcionários.  

**MaritalStatus_Single (0.213240)**  
Funcionários solteiros têm maior probabilidade de pedir demissão voluntária em comparação com casados ou com outros estados civis. Isso pode ser devido a maior flexibilidade e menos responsabilidades pessoais.  

**JobRole_Laboratory Technician (0.213197)**  
Funcionários que atuam como técnicos de laboratório têm maior probabilidade de pedir demissão voluntária. Isso pode refletir insatisfação com o cargo ou o ambiente de trabalho.  

**OverTime_Yes (0.183383)**  
Funcionários que fazem horas extras têm maior probabilidade de pedir demissão voluntária. Isso sugere que o excesso de trabalho pode levar ao desgaste e insatisfação.  

**DistanceFromHome (0.160642)**  
Maior distância de casa para o trabalho está associada a uma maior probabilidade de demissão voluntária. Longos deslocamentos podem gerar cansaço e insatisfação.  

**YearsSinceLastPromotion (0.157113)**  
Funcionários que passaram mais anos desde a última promoção têm maior probabilidade de pedir demissão voluntária. Isso pode indicar insatisfação com as oportunidades de crescimento na empresa.  

**JobRole_Sales Representative (0.126106)**  
Funcionários que trabalham como representantes de vendas têm maior probabilidade de pedir demissão voluntária. Essa função pode envolver alta pressão por resultados ou falta de suporte adequado.  

**YearsAtCompany (0.105078)**  
Quanto mais tempo um funcionário passa na empresa, maior é a probabilidade de ele pedir demissão voluntária. Isso pode indicar que, após um certo período, os funcionários podem sentir estagnação ou buscar novas oportunidades.  

**Conclusão:**  
Coeficientes positivos indicam que esses fatores aumentam a probabilidade de demissão voluntária. Entender esses fatores pode ajudar a empresa a tomar medidas preventivas, como melhorar as condições de trabalho, oferecer oportunidades de crescimento e minimizar as horas extras, para reduzir as taxas de rotatividade voluntária.