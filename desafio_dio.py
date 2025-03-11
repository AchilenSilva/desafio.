menu = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair 
 
>="""

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
   opcao = input (menu)

   if opcao == "0":
      valor = float(input("informe o valor a ser depositado: "))
      if valor > 0:
         saldo += valor
         extrato += f"Depósito: R$ {valor:.2f}\n"

      else:
         print("Operação falhou, o número informado é inválido")   
   
   
   elif opcao == "1":
     valor = float(input("Informe o valor no saque: "))

     excedeu_saldo = valor > saldo

     excedeu_limite = valor > limite

     excedeu_saques = numero_saques >= LIMITE_SAQUES

     if excedeu_saldo:
      print("Operação falhou! Você não tem saldo sulficiente.")

     elif excedeu_limite:
      print("Operação falhou! O valor do saque excedeu o limite")

     elif excedeu_saques:
      print("Operação falhou! Numero máximo de saques excedido")      

     elif valor > 0:
      saldo -= valor
      extrato += f"saque: R$ {valor:.2F}\n"
      numero_saques +=1

     else:
      print("Operação falhou! O número informado é inválido")   

   
   elif opcao == "2":
     print("\n********************EXTRATO********************")
     print("Não foram realizadas movimentações" if not extrato else extrato)
     print(f"\nsaldo: R$ {saldo:.2f}")
     print("*************************************************")

   elif opcao == "3":   
     break
      
   else:
     print("Operação invalida, por favor digite novamente a opção desejada")       

