
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRE_COLCHETE ABRE_PARENTESE ATE ATRIBUICAO DIFERENTE DIVISAO DOIS_PONTOS ENTAO ESCREVA E_LOGICO FECHA_COLCHETE FECHA_PARENTESE FIM FLUTUANTE ID IGUAL INTEIRO LEIA MAIOR MAIOR_IGUAL MAIS MENOR MENOR_IGUAL MENOS MULT NEGACAO NUM_FLUT NUM_INT NUM_NOTACAO OU_LOGICO REPITA RETORNA SE SENAO VIRGULAprograma : lista_declaracoeslista_declaracoes : lista_declaracoes declaracao\n                         | declaracaodeclaracao : declaracao_variaveis\n                  | inicializacao_variaveis\n                  | declaracao_funcaodeclaracao_variaveis : tipo DOIS_PONTOS lista_variaveisdeclaracao_variaveis : tipo DOIS_PONTOS errordeclaracao_variaveis : error DOIS_PONTOS lista_variaveisinicializacao_variaveis : atribuicaolista_variaveis : lista_variaveis VIRGULA var\n                       | varvar : id \n           | id indiceindice : indice ABRE_COLCHETE expressao FECHA_COLCHETE\n              | ABRE_COLCHETE expressao FECHA_COLCHETEtipo : INTEIRO\n            | FLUTUANTEdeclaracao_funcao : tipo cabecalho\n                         | cabecalhodeclaracao_funcao : error cabecalhocabecalho : id ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIMcabecalho : error ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIMcabecalho : id ABRE_PARENTESE error FECHA_PARENTESE corpo FIMlista_parametros : lista_parametros VIRGULA parametro\n                        | parametro\n                        | emptyparametro : tipo DOIS_PONTOS id\n                 | parametro ABRE_COLCHETE FECHA_COLCHETEcorpo : corpo acao\n             | emptyacao : expressao\n            | declaracao_variaveis\n            | se\n            | repita\n            | leia\n            | escreva\n            | retornase : SE expressao ENTAO corpo FIM\n          | SE expressao ENTAO corpo SENAO corpo FIMrepita : REPITA corpo ATE expressaoatribuicao : var ATRIBUICAO expressaoleia : LEIA ABRE_PARENTESE var FECHA_PARENTESEescreva : ESCREVA ABRE_PARENTESE expressao FECHA_PARENTESEretorna : RETORNA ABRE_PARENTESE expressao FECHA_PARENTESEexpressao : expressao_logica\n                 | atribuicaoexpressao_logica : expressao_simples\n                        | expressao_logica operador_logico expressao_simplesexpressao_simples : expressao_aditiva\n                         | expressao_simples operador_relacional expressao_aditivaexpressao_aditiva : expressao_multiplicativa\n                         | expressao_aditiva operador_soma expressao_multiplicativaexpressao_multiplicativa : expressao_unaria\n                                | expressao_multiplicativa operador_multiplicacao expressao_unariaexpressao_unaria : fator\n                        | operador_soma fator\n                        | operador_negacao fatoroperador_relacional : MENOR\n                           | MAIOR\n                           | IGUAL\n                           | DIFERENTE\n                           | MENOR_IGUAL\n                           | MAIOR_IGUALoperador_soma : MAIS\n                     | MENOSoperador_logico : E_LOGICO\n                       | OU_LOGICOoperador_negacao : NEGACAOoperador_multiplicacao : MULT\n                              | DIVISAOfator : ABRE_PARENTESE expressao FECHA_PARENTESE\n             | var\n             | chamada_funcao\n             | numeronumero : num_int\n              | num_flut\n              | num_notacaochamada_funcao : id ABRE_PARENTESE lista_argumentos FECHA_PARENTESElista_argumentos : lista_argumentos VIRGULA expressao\n                        | expressao\n                        | empty id : IDnum_int : NUM_INTnum_flut : NUM_FLUTnum_notacao : NUM_NOTACAOempty :'
    
_lr_action_items = {'$end':([1,2,5,6,7,8,11,12,13,16,20,22,25,28,29,30,31,33,34,36,37,38,41,42,44,45,47,48,50,51,52,53,54,55,62,64,66,67,70,85,93,94,98,99,100,101,102,111,115,128,129,],[-1,-10,-4,-6,-5,-83,-20,-3,0,-2,-19,-14,-21,-7,-8,-13,-12,-47,-85,-50,-13,-84,-54,-46,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,-9,-42,-58,-73,-16,-57,-11,-53,-49,-51,-72,-55,-15,-79,-22,-24,-23,]),'DOIS_PONTOS':([3,9,10,15,58,112,126,],[17,24,-18,-17,89,17,24,]),'NEGACAO':([8,21,22,27,28,29,30,31,33,34,35,36,37,38,41,42,43,44,45,46,47,48,50,51,52,53,54,55,56,62,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,84,85,88,90,92,93,94,98,99,100,101,102,104,105,107,109,110,111,114,116,118,119,121,122,123,124,125,127,131,134,135,138,140,141,142,143,144,145,146,147,148,149,],[-83,40,-14,40,-7,-8,-13,-12,-47,-85,-66,-50,-13,-84,-54,-46,-65,-75,-48,40,-56,-52,-76,-78,-86,-77,-73,-74,40,-9,-42,-58,-73,40,40,-16,-68,40,-67,40,-63,-61,-64,-60,-62,-59,-71,-70,40,-57,-87,-87,-87,-11,-53,-49,-51,-72,-55,-15,-31,40,40,40,40,-79,-30,-32,40,-37,-38,-33,-34,-87,-36,-35,40,40,40,-87,40,-45,-43,40,-44,-41,-39,-87,40,-40,]),'MENOS':([8,21,22,27,28,29,30,31,33,34,35,36,37,38,41,42,43,44,45,46,47,48,50,51,52,53,54,55,56,62,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,84,85,88,90,92,93,94,98,99,100,101,102,104,105,107,109,110,111,114,116,118,119,121,122,123,124,125,127,131,134,135,138,140,141,142,143,144,145,146,147,148,149,],[-83,35,-14,35,-7,-8,-13,-12,-47,-85,-66,35,-13,-84,-54,-46,-65,-75,-48,35,-56,-52,-76,-78,-86,-77,-73,-74,35,-9,-42,-58,-73,35,35,-16,-68,35,-67,35,-63,-61,-64,-60,-62,-59,-71,-70,35,-57,-87,-87,-87,-11,-53,-49,35,-72,-55,-15,-31,35,35,35,35,-79,-30,-32,35,-37,-38,-33,-34,-87,-36,-35,35,35,35,-87,35,-45,-43,35,-44,-41,-39,-87,35,-40,]),'FECHA_PARENTESE':([8,22,23,26,30,33,34,36,37,38,41,42,44,45,47,48,50,51,52,53,54,55,57,59,60,61,63,64,66,67,69,70,81,85,94,95,96,97,98,99,100,101,102,103,106,108,111,130,136,137,139,],[-83,-14,-87,-87,-13,-47,-85,-50,-13,-84,-54,-46,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,88,90,-26,-27,92,-42,-58,-73,-87,-16,100,-57,-53,-82,111,-81,-49,-51,-72,-55,-15,-25,-28,-29,-79,-80,141,142,144,]),'IGUAL':([8,22,34,36,37,38,41,44,45,47,48,50,51,52,53,54,55,66,67,70,85,94,98,99,100,101,102,111,],[-83,-14,-85,-50,-13,-84,-54,-75,76,-56,-52,-76,-78,-86,-77,-73,-74,-58,-73,-16,-57,-53,76,-51,-72,-55,-15,-79,]),'FIM':([8,22,28,29,30,31,33,34,36,37,38,41,42,44,45,47,48,50,51,52,53,54,55,62,64,66,67,70,85,88,90,92,93,94,98,99,100,101,102,104,105,107,109,111,114,116,119,121,122,123,125,127,138,141,142,143,144,145,146,147,148,149,],[-83,-14,-7,-8,-13,-12,-47,-85,-50,-13,-84,-54,-46,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,-9,-42,-58,-73,-16,-57,-87,-87,-87,-11,-53,-49,-51,-72,-55,-15,-31,115,128,129,-79,-30,-32,-37,-38,-33,-34,-36,-35,-87,-45,-43,146,-44,-41,-39,-87,149,-40,]),'NUM_INT':([8,21,22,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,62,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,84,85,88,90,92,93,94,98,99,100,101,102,104,105,107,109,110,111,114,116,118,119,121,122,123,124,125,127,131,134,135,138,140,141,142,143,144,145,146,147,148,149,],[-83,38,-14,38,-7,-8,-13,-12,38,-47,-85,-66,-50,-13,-84,-69,-54,-46,-65,-75,-48,38,-56,-52,38,-76,-78,-86,-77,-73,-74,38,-9,-42,-58,-73,38,38,-16,-68,38,-67,38,-63,-61,-64,-60,-62,-59,-71,-70,38,-57,-87,-87,-87,-11,-53,-49,-51,-72,-55,-15,-31,38,38,38,38,-79,-30,-32,38,-37,-38,-33,-34,-87,-36,-35,38,38,38,-87,38,-45,-43,38,-44,-41,-39,-87,38,-40,]),'MENOR_IGUAL':([8,22,34,36,37,38,41,44,45,47,48,50,51,52,53,54,55,66,67,70,85,94,98,99,100,101,102,111,],[-83,-14,-85,-50,-13,-84,-54,-75,75,-56,-52,-76,-78,-86,-77,-73,-74,-58,-73,-16,-57,-53,75,-51,-72,-55,-15,-79,]),'ABRE_COLCHETE':([4,8,22,30,37,60,70,102,103,106,108,],[21,-83,56,21,21,91,-16,-15,91,-28,-29,]),'LEIA':([8,22,28,29,30,31,33,34,36,37,38,41,42,44,45,47,48,50,51,52,53,54,55,62,64,66,67,70,85,88,90,92,93,94,98,99,100,101,102,104,105,107,109,111,114,116,119,121,122,123,124,125,127,135,138,141,142,143,144,145,146,147,148,149,],[-83,-14,-7,-8,-13,-12,-47,-85,-50,-13,-84,-54,-46,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,-9,-42,-58,-73,-16,-57,-87,-87,-87,-11,-53,-49,-51,-72,-55,-15,-31,117,117,117,-79,-30,-32,-37,-38,-33,-34,-87,-36,-35,117,-87,-45,-43,117,-44,-41,-39,-87,117,-40,]),'REPITA':([8,22,28,29,30,31,33,34,36,37,38,41,42,44,45,47,48,50,51,52,53,54,55,62,64,66,67,70,85,88,90,92,93,94,98,99,100,101,102,104,105,107,109,111,114,116,119,121,122,123,124,125,127,135,138,141,142,143,144,145,146,147,148,149,],[-83,-14,-7,-8,-13,-12,-47,-85,-50,-13,-84,-54,-46,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,-9,-42,-58,-73,-16,-57,-87,-87,-87,-11,-53,-49,-51,-72,-55,-15,-31,124,124,124,-79,-30,-32,-37,-38,-33,-34,-87,-36,-35,124,-87,-45,-43,124,-44,-41,-39,-87,124,-40,]),'DIVISAO':([8,22,34,37,38,41,44,47,48,50,51,52,53,54,55,66,67,70,85,94,100,101,102,111,],[-83,-14,-85,-13,-84,-54,-75,-56,82,-76,-78,-86,-77,-73,-74,-58,-73,-16,-57,82,-72,-55,-15,-79,]),'MAIOR':([8,22,34,36,37,38,41,44,45,47,48,50,51,52,53,54,55,66,67,70,85,94,98,99,100,101,102,111,],[-83,-14,-85,-50,-13,-84,-54,-75,78,-56,-52,-76,-78,-86,-77,-73,-74,-58,-73,-16,-57,-53,78,-51,-72,-55,-15,-79,]),'NUM_FLUT':([8,21,22,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,62,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,84,85,88,90,92,93,94,98,99,100,101,102,104,105,107,109,110,111,114,116,118,119,121,122,123,124,125,127,131,134,135,138,140,141,142,143,144,145,146,147,148,149,],[-83,34,-14,34,-7,-8,-13,-12,34,-47,-85,-66,-50,-13,-84,-69,-54,-46,-65,-75,-48,34,-56,-52,34,-76,-78,-86,-77,-73,-74,34,-9,-42,-58,-73,34,34,-16,-68,34,-67,34,-63,-61,-64,-60,-62,-59,-71,-70,34,-57,-87,-87,-87,-11,-53,-49,-51,-72,-55,-15,-31,34,34,34,34,-79,-30,-32,34,-37,-38,-33,-34,-87,-36,-35,34,34,34,-87,34,-45,-43,34,-44,-41,-39,-87,34,-40,]),'RETORNA':([8,22,28,29,30,31,33,34,36,37,38,41,42,44,45,47,48,50,51,52,53,54,55,62,64,66,67,70,85,88,90,92,93,94,98,99,100,101,102,104,105,107,109,111,114,116,119,121,122,123,124,125,127,135,138,141,142,143,144,145,146,147,148,149,],[-83,-14,-7,-8,-13,-12,-47,-85,-50,-13,-84,-54,-46,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,-9,-42,-58,-73,-16,-57,-87,-87,-87,-11,-53,-49,-51,-72,-55,-15,-31,113,113,113,-79,-30,-32,-37,-38,-33,-34,-87,-36,-35,113,-87,-45,-43,113,-44,-41,-39,-87,113,-40,]),'ATRIBUICAO':([4,8,14,22,37,54,70,102,],[-13,-83,27,-14,-13,27,-16,-15,]),'ESCREVA':([8,22,28,29,30,31,33,34,36,37,38,41,42,44,45,47,48,50,51,52,53,54,55,62,64,66,67,70,85,88,90,92,93,94,98,99,100,101,102,104,105,107,109,111,114,116,119,121,122,123,124,125,127,135,138,141,142,143,144,145,146,147,148,149,],[-83,-14,-7,-8,-13,-12,-47,-85,-50,-13,-84,-54,-46,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,-9,-42,-58,-73,-16,-57,-87,-87,-87,-11,-53,-49,-51,-72,-55,-15,-31,120,120,120,-79,-30,-32,-37,-38,-33,-34,-87,-36,-35,120,-87,-45,-43,120,-44,-41,-39,-87,120,-40,]),'FECHA_COLCHETE':([8,22,33,34,36,37,38,39,41,42,44,45,47,48,50,51,52,53,54,55,64,66,67,70,85,86,91,94,98,99,100,101,102,111,],[-83,-14,-47,-85,-50,-13,-84,70,-54,-46,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,-42,-58,-73,-16,-57,102,108,-53,-49,-51,-72,-55,-15,-79,]),'ID':([0,1,2,3,5,6,7,8,9,10,11,12,15,16,17,20,21,22,24,25,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,84,85,88,89,90,92,93,94,98,99,100,101,102,104,105,107,109,110,111,114,115,116,118,119,121,122,123,124,125,127,128,129,131,132,134,135,138,140,141,142,143,144,145,146,147,148,149,],[8,8,-10,8,-4,-6,-5,-83,8,-18,-20,-3,-17,-2,8,-19,8,-14,8,-21,8,-7,-8,-13,-12,8,-47,-85,-66,-50,-13,-84,-69,-54,-46,-65,-75,-48,8,-56,-52,8,-76,-78,-86,-77,-73,-74,8,-9,-42,8,-58,-73,8,8,-16,-68,8,-67,8,-63,-61,-64,-60,-62,-59,-71,-70,8,-57,-87,8,-87,-87,-11,-53,-49,-51,-72,-55,-15,-31,8,8,8,8,-79,-30,-22,-32,8,-37,-38,-33,-34,-87,-36,-35,-24,-23,8,8,8,8,-87,8,-45,-43,8,-44,-41,-39,-87,8,-40,]),'SE':([8,22,28,29,30,31,33,34,36,37,38,41,42,44,45,47,48,50,51,52,53,54,55,62,64,66,67,70,85,88,90,92,93,94,98,99,100,101,102,104,105,107,109,111,114,116,119,121,122,123,124,125,127,135,138,141,142,143,144,145,146,147,148,149,],[-83,-14,-7,-8,-13,-12,-47,-85,-50,-13,-84,-54,-46,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,-9,-42,-58,-73,-16,-57,-87,-87,-87,-11,-53,-49,-51,-72,-55,-15,-31,118,118,118,-79,-30,-32,-37,-38,-33,-34,-87,-36,-35,118,-87,-45,-43,118,-44,-41,-39,-87,118,-40,]),'FLUTUANTE':([0,1,2,5,6,7,8,11,12,16,20,22,23,25,26,28,29,30,31,33,34,36,37,38,41,42,44,45,47,48,50,51,52,53,54,55,62,64,66,67,70,85,87,88,90,92,93,94,98,99,100,101,102,104,105,107,109,111,114,115,116,119,121,122,123,124,125,127,128,129,135,138,141,142,143,144,145,146,147,148,149,],[10,10,-10,-4,-6,-5,-83,-20,-3,-2,-19,-14,10,-21,10,-7,-8,-13,-12,-47,-85,-50,-13,-84,-54,-46,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,-9,-42,-58,-73,-16,-57,10,-87,-87,-87,-11,-53,-49,-51,-72,-55,-15,-31,10,10,10,-79,-30,-22,-32,-37,-38,-33,-34,-87,-36,-35,-24,-23,10,-87,-45,-43,10,-44,-41,-39,-87,10,-40,]),'error':([0,1,2,3,5,6,7,8,9,10,11,12,15,16,17,20,22,23,25,28,29,30,31,33,34,36,37,38,41,42,44,45,47,48,50,51,52,53,54,55,62,64,66,67,70,85,88,90,92,93,94,98,99,100,101,102,104,105,107,109,111,114,115,116,119,121,122,123,124,125,127,128,129,135,138,141,142,143,144,145,146,147,148,149,],[9,9,-10,18,-4,-6,-5,-83,18,-18,-20,-3,-17,-2,29,-19,-14,59,-21,-7,-8,-13,-12,-47,-85,-50,-13,-84,-54,-46,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,-9,-42,-58,-73,-16,-57,-87,-87,-87,-11,-53,-49,-51,-72,-55,-15,-31,126,126,126,-79,-30,-22,-32,-37,-38,-33,-34,-87,-36,-35,-24,-23,126,-87,-45,-43,126,-44,-41,-39,-87,126,-40,]),'E_LOGICO':([8,22,34,36,37,38,41,42,44,45,47,48,50,51,52,53,54,55,66,67,70,85,94,98,99,100,101,102,111,],[-83,-14,-85,-50,-13,-84,-54,73,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,-58,-73,-16,-57,-53,-49,-51,-72,-55,-15,-79,]),'DIFERENTE':([8,22,34,36,37,38,41,44,45,47,48,50,51,52,53,54,55,66,67,70,85,94,98,99,100,101,102,111,],[-83,-14,-85,-50,-13,-84,-54,-75,79,-56,-52,-76,-78,-86,-77,-73,-74,-58,-73,-16,-57,-53,79,-51,-72,-55,-15,-79,]),'MENOR':([8,22,34,36,37,38,41,44,45,47,48,50,51,52,53,54,55,66,67,70,85,94,98,99,100,101,102,111,],[-83,-14,-85,-50,-13,-84,-54,-75,80,-56,-52,-76,-78,-86,-77,-73,-74,-58,-73,-16,-57,-53,80,-51,-72,-55,-15,-79,]),'MAIS':([8,21,22,27,28,29,30,31,33,34,35,36,37,38,41,42,43,44,45,46,47,48,50,51,52,53,54,55,56,62,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,84,85,88,90,92,93,94,98,99,100,101,102,104,105,107,109,110,111,114,116,118,119,121,122,123,124,125,127,131,134,135,138,140,141,142,143,144,145,146,147,148,149,],[-83,43,-14,43,-7,-8,-13,-12,-47,-85,-66,43,-13,-84,-54,-46,-65,-75,-48,43,-56,-52,-76,-78,-86,-77,-73,-74,43,-9,-42,-58,-73,43,43,-16,-68,43,-67,43,-63,-61,-64,-60,-62,-59,-71,-70,43,-57,-87,-87,-87,-11,-53,-49,43,-72,-55,-15,-31,43,43,43,43,-79,-30,-32,43,-37,-38,-33,-34,-87,-36,-35,43,43,43,-87,43,-45,-43,43,-44,-41,-39,-87,43,-40,]),'ATE':([8,22,28,29,30,31,33,34,36,37,38,41,42,44,45,47,48,50,51,52,53,54,55,62,64,66,67,70,85,93,94,98,99,100,101,102,104,111,114,116,119,121,122,123,124,125,127,135,141,142,144,145,146,149,],[-83,-14,-7,-8,-13,-12,-47,-85,-50,-13,-84,-54,-46,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,-9,-42,-58,-73,-16,-57,-11,-53,-49,-51,-72,-55,-15,-31,-79,-30,-32,-37,-38,-33,-34,-87,-36,-35,140,-45,-43,-44,-41,-39,-40,]),'VIRGULA':([8,22,23,26,28,30,31,33,34,36,37,38,41,42,44,45,47,48,50,51,52,53,54,55,57,60,61,62,63,64,66,67,69,70,85,93,94,95,96,97,98,99,100,101,102,103,106,108,111,130,],[-83,-14,-87,-87,65,-13,-12,-47,-85,-50,-13,-84,-54,-46,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,87,-26,-27,65,87,-42,-58,-73,-87,-16,-57,-11,-53,-82,110,-81,-49,-51,-72,-55,-15,-25,-28,-29,-79,-80,]),'NUM_NOTACAO':([8,21,22,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,62,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,84,85,88,90,92,93,94,98,99,100,101,102,104,105,107,109,110,111,114,116,118,119,121,122,123,124,125,127,131,134,135,138,140,141,142,143,144,145,146,147,148,149,],[-83,52,-14,52,-7,-8,-13,-12,52,-47,-85,-66,-50,-13,-84,-69,-54,-46,-65,-75,-48,52,-56,-52,52,-76,-78,-86,-77,-73,-74,52,-9,-42,-58,-73,52,52,-16,-68,52,-67,52,-63,-61,-64,-60,-62,-59,-71,-70,52,-57,-87,-87,-87,-11,-53,-49,-51,-72,-55,-15,-31,52,52,52,52,-79,-30,-32,52,-37,-38,-33,-34,-87,-36,-35,52,52,52,-87,52,-45,-43,52,-44,-41,-39,-87,52,-40,]),'MAIOR_IGUAL':([8,22,34,36,37,38,41,44,45,47,48,50,51,52,53,54,55,66,67,70,85,94,98,99,100,101,102,111,],[-83,-14,-85,-50,-13,-84,-54,-75,77,-56,-52,-76,-78,-86,-77,-73,-74,-58,-73,-16,-57,-53,77,-51,-72,-55,-15,-79,]),'ENTAO':([8,22,33,34,36,37,38,41,42,44,45,47,48,50,51,52,53,54,55,64,66,67,70,85,94,98,99,100,101,102,111,133,],[-83,-14,-47,-85,-50,-13,-84,-54,-46,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,-42,-58,-73,-16,-57,-53,-49,-51,-72,-55,-15,-79,138,]),'MULT':([8,22,34,37,38,41,44,47,48,50,51,52,53,54,55,66,67,70,85,94,100,101,102,111,],[-83,-14,-85,-13,-84,-54,-75,-56,83,-76,-78,-86,-77,-73,-74,-58,-73,-16,-57,83,-72,-55,-15,-79,]),'SENAO':([8,22,28,29,30,31,33,34,36,37,38,41,42,44,45,47,48,50,51,52,53,54,55,62,64,66,67,70,85,93,94,98,99,100,101,102,104,111,114,116,119,121,122,123,125,127,138,141,142,143,144,145,146,149,],[-83,-14,-7,-8,-13,-12,-47,-85,-50,-13,-84,-54,-46,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,-9,-42,-58,-73,-16,-57,-11,-53,-49,-51,-72,-55,-15,-31,-79,-30,-32,-37,-38,-33,-34,-36,-35,-87,-45,-43,147,-44,-41,-39,-40,]),'ABRE_PARENTESE':([4,8,9,18,19,21,22,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,62,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,84,85,88,90,92,93,94,98,99,100,101,102,104,105,107,109,110,111,113,114,116,117,118,119,120,121,122,123,124,125,127,131,134,135,138,140,141,142,143,144,145,146,147,148,149,],[23,-83,26,26,23,46,-14,46,-7,-8,-13,-12,46,-47,-85,-66,-50,69,-84,-69,-54,-46,-65,-75,-48,46,-56,-52,46,-76,-78,-86,-77,-73,-74,46,-9,-42,-58,-73,46,46,-16,-68,46,-67,46,-63,-61,-64,-60,-62,-59,-71,-70,46,-57,-87,-87,-87,-11,-53,-49,-51,-72,-55,-15,-31,46,46,46,46,-79,131,-30,-32,132,46,-37,134,-38,-33,-34,-87,-36,-35,46,46,46,-87,46,-45,-43,46,-44,-41,-39,-87,46,-40,]),'OU_LOGICO':([8,22,34,36,37,38,41,42,44,45,47,48,50,51,52,53,54,55,66,67,70,85,94,98,99,100,101,102,111,],[-83,-14,-85,-50,-13,-84,-54,71,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,-58,-73,-16,-57,-53,-49,-51,-72,-55,-15,-79,]),'INTEIRO':([0,1,2,5,6,7,8,11,12,16,20,22,23,25,26,28,29,30,31,33,34,36,37,38,41,42,44,45,47,48,50,51,52,53,54,55,62,64,66,67,70,85,87,88,90,92,93,94,98,99,100,101,102,104,105,107,109,111,114,115,116,119,121,122,123,124,125,127,128,129,135,138,141,142,143,144,145,146,147,148,149,],[15,15,-10,-4,-6,-5,-83,-20,-3,-2,-19,-14,15,-21,15,-7,-8,-13,-12,-47,-85,-50,-13,-84,-54,-46,-75,-48,-56,-52,-76,-78,-86,-77,-73,-74,-9,-42,-58,-73,-16,-57,15,-87,-87,-87,-11,-53,-49,-51,-72,-55,-15,-31,15,15,15,-79,-30,-22,-32,-37,-38,-33,-34,-87,-36,-35,-24,-23,15,-87,-45,-43,15,-44,-41,-39,-87,15,-40,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'lista_declaracoes':([0,],[1,]),'operador_relacional':([45,98,],[74,74,]),'operador_negacao':([21,27,46,56,68,69,72,74,84,105,107,109,110,118,131,134,135,140,143,148,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'atribuicao':([0,1,21,27,46,56,69,105,107,109,110,118,131,134,135,140,143,148,],[2,2,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'tipo':([0,1,23,26,87,105,107,109,135,143,148,],[3,3,58,58,58,112,112,112,112,112,112,]),'expressao_aditiva':([21,27,46,56,69,72,74,105,107,109,110,118,131,134,135,140,143,148,],[36,36,36,36,36,36,99,36,36,36,36,36,36,36,36,36,36,36,]),'parametro':([23,26,87,],[60,60,103,]),'id':([0,1,3,9,17,21,24,27,32,46,49,56,65,68,69,72,74,84,89,105,107,109,110,118,131,132,134,135,140,143,148,],[4,4,19,19,30,37,30,37,37,37,37,37,30,37,37,37,37,37,106,37,37,37,37,37,37,30,37,37,37,37,37,]),'acao':([105,107,109,135,143,148,],[114,114,114,114,114,114,]),'expressao_multiplicativa':([21,27,46,56,68,69,72,74,105,107,109,110,118,131,134,135,140,143,148,],[48,48,48,48,94,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'num_notacao':([21,27,32,46,49,56,68,69,72,74,84,105,107,109,110,118,131,134,135,140,143,148,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'declaracao_funcao':([0,1,],[6,6,]),'expressao_unaria':([21,27,46,56,68,69,72,74,84,105,107,109,110,118,131,134,135,140,143,148,],[41,41,41,41,41,41,41,41,101,41,41,41,41,41,41,41,41,41,41,41,]),'empty':([23,26,69,88,90,92,124,138,147,],[61,61,95,104,104,104,104,104,104,]),'expressao_logica':([21,27,46,56,69,105,107,109,110,118,131,134,135,140,143,148,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'lista_argumentos':([69,],[96,]),'numero':([21,27,32,46,49,56,68,69,72,74,84,105,107,109,110,118,131,134,135,140,143,148,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'expressao_simples':([21,27,46,56,69,72,105,107,109,110,118,131,134,135,140,143,148,],[45,45,45,45,45,98,45,45,45,45,45,45,45,45,45,45,45,]),'declaracao_variaveis':([0,1,105,107,109,135,143,148,],[5,5,122,122,122,122,122,122,]),'inicializacao_variaveis':([0,1,],[7,7,]),'lista_parametros':([23,26,],[57,63,]),'escreva':([105,107,109,135,143,148,],[119,119,119,119,119,119,]),'se':([105,107,109,135,143,148,],[123,123,123,123,123,123,]),'repita':([105,107,109,135,143,148,],[127,127,127,127,127,127,]),'operador_multiplicacao':([48,94,],[84,84,]),'fator':([21,27,32,46,49,56,68,69,72,74,84,105,107,109,110,118,131,134,135,140,143,148,],[47,47,66,47,85,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'programa':([0,],[13,]),'expressao':([21,27,46,56,69,105,107,109,110,118,131,134,135,140,143,148,],[39,64,81,86,97,116,116,116,130,133,136,139,116,145,116,116,]),'operador_soma':([21,27,36,46,56,68,69,72,74,84,99,105,107,109,110,118,131,134,135,140,143,148,],[49,49,68,49,49,49,49,49,49,49,68,49,49,49,49,49,49,49,49,49,49,49,]),'var':([0,1,17,21,24,27,32,46,49,56,65,68,69,72,74,84,105,107,109,110,118,131,132,134,135,140,143,148,],[14,14,31,54,31,54,67,54,67,54,93,67,54,67,67,67,54,54,54,54,54,54,137,54,54,54,54,54,]),'operador_logico':([42,],[72,]),'leia':([105,107,109,135,143,148,],[125,125,125,125,125,125,]),'cabecalho':([0,1,3,9,],[11,11,20,25,]),'lista_variaveis':([17,24,],[28,62,]),'declaracao':([0,1,],[12,16,]),'retorna':([105,107,109,135,143,148,],[121,121,121,121,121,121,]),'indice':([4,30,37,],[22,22,22,]),'corpo':([88,90,92,124,138,147,],[105,107,109,135,143,148,]),'num_flut':([21,27,32,46,49,56,68,69,72,74,84,105,107,109,110,118,131,134,135,140,143,148,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'num_int':([21,27,32,46,49,56,68,69,72,74,84,105,107,109,110,118,131,134,135,140,143,148,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'chamada_funcao':([21,27,32,46,49,56,68,69,72,74,84,105,107,109,110,118,131,134,135,140,143,148,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaracoes','programa',1,'p_programa','parser.py',9),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','parser.py',14),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes','parser.py',15),
  ('declaracao -> declaracao_variaveis','declaracao',1,'p_declaracao','parser.py',20),
  ('declaracao -> inicializacao_variaveis','declaracao',1,'p_declaracao','parser.py',21),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','parser.py',22),
  ('declaracao_variaveis -> tipo DOIS_PONTOS lista_variaveis','declaracao_variaveis',3,'p_declaracao_variaveis','parser.py',27),
  ('declaracao_variaveis -> tipo DOIS_PONTOS error','declaracao_variaveis',3,'p_declaracao_variaveis_error','parser.py',32),
  ('declaracao_variaveis -> error DOIS_PONTOS lista_variaveis','declaracao_variaveis',3,'p_declaracao_variaveis_error2','parser.py',36),
  ('inicializacao_variaveis -> atribuicao','inicializacao_variaveis',1,'p_inicializacao_variaveis','parser.py',40),
  ('lista_variaveis -> lista_variaveis VIRGULA var','lista_variaveis',3,'p_lista_variaveis','parser.py',45),
  ('lista_variaveis -> var','lista_variaveis',1,'p_lista_variaveis','parser.py',46),
  ('var -> id','var',1,'p_var','parser.py',51),
  ('var -> id indice','var',2,'p_var','parser.py',52),
  ('indice -> indice ABRE_COLCHETE expressao FECHA_COLCHETE','indice',4,'p_indice','parser.py',57),
  ('indice -> ABRE_COLCHETE expressao FECHA_COLCHETE','indice',3,'p_indice','parser.py',58),
  ('tipo -> INTEIRO','tipo',1,'p_tipo','parser.py',63),
  ('tipo -> FLUTUANTE','tipo',1,'p_tipo','parser.py',64),
  ('declaracao_funcao -> tipo cabecalho','declaracao_funcao',2,'p_declaracao_funcao','parser.py',69),
  ('declaracao_funcao -> cabecalho','declaracao_funcao',1,'p_declaracao_funcao','parser.py',70),
  ('declaracao_funcao -> error cabecalho','declaracao_funcao',2,'p_declaracao_funcao_error','parser.py',78),
  ('cabecalho -> id ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIM','cabecalho',6,'p_cabecalho','parser.py',82),
  ('cabecalho -> error ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIM','cabecalho',6,'p_cabecalho_error','parser.py',87),
  ('cabecalho -> id ABRE_PARENTESE error FECHA_PARENTESE corpo FIM','cabecalho',6,'p_cabecalho_error2','parser.py',91),
  ('lista_parametros -> lista_parametros VIRGULA parametro','lista_parametros',3,'p_lista_parametros','parser.py',96),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros','parser.py',97),
  ('lista_parametros -> empty','lista_parametros',1,'p_lista_parametros','parser.py',98),
  ('parametro -> tipo DOIS_PONTOS id','parametro',3,'p_parametro','parser.py',105),
  ('parametro -> parametro ABRE_COLCHETE FECHA_COLCHETE','parametro',3,'p_parametro','parser.py',106),
  ('corpo -> corpo acao','corpo',2,'p_corpo','parser.py',111),
  ('corpo -> empty','corpo',1,'p_corpo','parser.py',112),
  ('acao -> expressao','acao',1,'p_acao','parser.py',120),
  ('acao -> declaracao_variaveis','acao',1,'p_acao','parser.py',121),
  ('acao -> se','acao',1,'p_acao','parser.py',122),
  ('acao -> repita','acao',1,'p_acao','parser.py',123),
  ('acao -> leia','acao',1,'p_acao','parser.py',124),
  ('acao -> escreva','acao',1,'p_acao','parser.py',125),
  ('acao -> retorna','acao',1,'p_acao','parser.py',126),
  ('se -> SE expressao ENTAO corpo FIM','se',5,'p_se','parser.py',131),
  ('se -> SE expressao ENTAO corpo SENAO corpo FIM','se',7,'p_se','parser.py',132),
  ('repita -> REPITA corpo ATE expressao','repita',4,'p_repita','parser.py',137),
  ('atribuicao -> var ATRIBUICAO expressao','atribuicao',3,'p_atribuicao','parser.py',142),
  ('leia -> LEIA ABRE_PARENTESE var FECHA_PARENTESE','leia',4,'p_leia','parser.py',147),
  ('escreva -> ESCREVA ABRE_PARENTESE expressao FECHA_PARENTESE','escreva',4,'p_escreva','parser.py',152),
  ('retorna -> RETORNA ABRE_PARENTESE expressao FECHA_PARENTESE','retorna',4,'p_retorna','parser.py',157),
  ('expressao -> expressao_logica','expressao',1,'p_expressao','parser.py',162),
  ('expressao -> atribuicao','expressao',1,'p_expressao','parser.py',163),
  ('expressao_logica -> expressao_simples','expressao_logica',1,'p_expressao_logica','parser.py',168),
  ('expressao_logica -> expressao_logica operador_logico expressao_simples','expressao_logica',3,'p_expressao_logica','parser.py',169),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_expressao_simples','parser.py',174),
  ('expressao_simples -> expressao_simples operador_relacional expressao_aditiva','expressao_simples',3,'p_expressao_simples','parser.py',175),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_expressao_aditiva','parser.py',180),
  ('expressao_aditiva -> expressao_aditiva operador_soma expressao_multiplicativa','expressao_aditiva',3,'p_expressao_aditiva','parser.py',181),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_expressao_multiplicativa','parser.py',186),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_expressao_multiplicativa','parser.py',187),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_expressao_unaria','parser.py',192),
  ('expressao_unaria -> operador_soma fator','expressao_unaria',2,'p_expressao_unaria','parser.py',193),
  ('expressao_unaria -> operador_negacao fator','expressao_unaria',2,'p_expressao_unaria','parser.py',194),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_operador_relacional','parser.py',199),
  ('operador_relacional -> MAIOR','operador_relacional',1,'p_operador_relacional','parser.py',200),
  ('operador_relacional -> IGUAL','operador_relacional',1,'p_operador_relacional','parser.py',201),
  ('operador_relacional -> DIFERENTE','operador_relacional',1,'p_operador_relacional','parser.py',202),
  ('operador_relacional -> MENOR_IGUAL','operador_relacional',1,'p_operador_relacional','parser.py',203),
  ('operador_relacional -> MAIOR_IGUAL','operador_relacional',1,'p_operador_relacional','parser.py',204),
  ('operador_soma -> MAIS','operador_soma',1,'p_operador_soma','parser.py',209),
  ('operador_soma -> MENOS','operador_soma',1,'p_operador_soma','parser.py',210),
  ('operador_logico -> E_LOGICO','operador_logico',1,'p_operador_logico','parser.py',215),
  ('operador_logico -> OU_LOGICO','operador_logico',1,'p_operador_logico','parser.py',216),
  ('operador_negacao -> NEGACAO','operador_negacao',1,'p_operador_negacao','parser.py',221),
  ('operador_multiplicacao -> MULT','operador_multiplicacao',1,'p_operador_multiplicacao','parser.py',226),
  ('operador_multiplicacao -> DIVISAO','operador_multiplicacao',1,'p_operador_multiplicacao','parser.py',227),
  ('fator -> ABRE_PARENTESE expressao FECHA_PARENTESE','fator',3,'p_fator','parser.py',232),
  ('fator -> var','fator',1,'p_fator','parser.py',233),
  ('fator -> chamada_funcao','fator',1,'p_fator','parser.py',234),
  ('fator -> numero','fator',1,'p_fator','parser.py',235),
  ('numero -> num_int','numero',1,'p_numero','parser.py',240),
  ('numero -> num_flut','numero',1,'p_numero','parser.py',241),
  ('numero -> num_notacao','numero',1,'p_numero','parser.py',242),
  ('chamada_funcao -> id ABRE_PARENTESE lista_argumentos FECHA_PARENTESE','chamada_funcao',4,'p_chamada_funcao','parser.py',247),
  ('lista_argumentos -> lista_argumentos VIRGULA expressao','lista_argumentos',3,'p_lista_argumentos','parser.py',252),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_lista_argumentos','parser.py',253),
  ('lista_argumentos -> empty','lista_argumentos',1,'p_lista_argumentos','parser.py',254),
  ('id -> ID','id',1,'p_id','parser.py',262),
  ('num_int -> NUM_INT','num_int',1,'p_num_int','parser.py',267),
  ('num_flut -> NUM_FLUT','num_flut',1,'p_num_flut','parser.py',272),
  ('num_notacao -> NUM_NOTACAO','num_notacao',1,'p_num_notacao','parser.py',277),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',282),
]
