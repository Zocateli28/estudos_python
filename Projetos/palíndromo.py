##Analisa de a palavra é um palíndromo
palavra = input("Insira uma palavra: ")
palindromo = palavra[::-1]

if palavra == palindromo:
    print( "A palavra", palavra ,"é um palíndromo")
else:
    print( "A palavra",palavra, "não é um palíndromo")