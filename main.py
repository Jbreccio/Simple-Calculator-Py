#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Calculadora Simples
Autor: Seu Nome
Data: 2025
Descrição: Uma calculadora básica que realiza operações matemáticas fundamentais
"""

def adicao(a, b):
    """Realiza a adição de dois números"""
    return a + b

def subtracao(a, b):
    """Realiza a subtração de dois números"""
    return a - b

def multiplicacao(a, b):
    """Realiza a multiplicação de dois números"""
    return a * b

def divisao(a, b):
    """Realiza a divisão de dois números"""
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b

def obter_numeros():
    """Obtém dois números do usuário"""
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        return num1, num2
    except ValueError:
        print("❌ Erro: Por favor, digite números válidos!")
        return None, None

def mostrar_menu():
    """Exibe o menu principal"""
    print("\n" + "="*30)
    print("🧮 CALCULADORA SIMPLES")
    print("="*30)
    print("1. ➕ Adição")
    print("2. ➖ Subtração")
    print("3. ✖️  Multiplicação")
    print("4. ➗ Divisão")
    print("5. 🚪 Sair")
    print("="*30)

def obter_operacao():
    """Obtém a operação escolhida pelo usuário"""
    try:
        opcao = int(input("Escolha uma operação (1-5): "))
        if opcao not in [1, 2, 3, 4, 5]:
            print("❌ Opção inválida! Escolha entre 1 e 5.")
            return None
        return opcao
    except ValueError:
        print("❌ Erro: Por favor, digite um número válido!")
        return None

def executar_operacao(opcao, num1, num2):
    """Executa a operação escolhida"""
    operacoes = {
        1: (adicao, "+"),
        2: (subtracao, "-"),
        3: (multiplicacao, "×"),
        4: (divisao, "÷")
    }
    
    funcao, simbolo = operacoes[opcao]
    
    try:
        resultado = funcao(num1, num2)
        print(f"\n✅ Resultado: {num1} {simbolo} {num2} = {resultado}")
        return True
    except ValueError as e:
        print(f"❌ Erro: {e}")
        return False

def main():
    """Função principal"""
    print("🎉 Bem-vindo à Calculadora Simples!")
    
    while True:
        mostrar_menu()
        opcao = obter_operacao()
        
        if opcao is None:
            continue
        
        if opcao == 5:
            print("👋 Obrigado por usar a calculadora! Até logo!")
            break
        
        num1, num2 = obter_numeros()
        
        if num1 is None or num2 is None:
            continue
        
        executar_operacao(opcao, num1, num2)
        
        # Perguntar se quer continuar
        continuar = input("\n🔄 Deseja fazer outro cálculo? (s/n): ").lower().strip()
        if continuar not in ['s', 'sim', 'y', 'yes']:
            print("👋 Obrigado por usar a calculadora! Até logo!")
            break

if __name__ == "__main__":
    main()
