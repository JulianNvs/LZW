
"""
COMPACTAÇÃO LZW

Código de 3 bytes

1. No início o dicionário contém todas as raízes possíveis e I é vazio;
2. c <= próximo caractere da sequência de entrada;
3. A string I+c existe no dicionário?
	a. se sim,
		i. I <= I+c;
	b. se não,
		i. coloque a palavra código correspondente a I na sequência codificada;
		ii. adicione a string I+c ao dicionário;
		iii. I <= c;
4. Existem mais caracteres na sequência de entrada ?
	a. se sim,
		i. volte ao passo 2;
	b. se não,
		ii. coloque a palavra código correspondente a I na sequência codificada;
		iii. FIM.
"""
import copy
from itertools import product
from queue import deque


def compactar_lzw(data, codeSize):
	def index_to_codeword(p, codesize):
		for k,i in enumerate(product(range(256), repeat=codesize)):
			if k == p:
				return list(i)
			

	dict = {}

	for i in range(256):
		dict[i] = chr(i)

	
	data = [chr(i) for i in data]
	print("Tamanho original:",len(data),"bytes.")
	compressed = ""

	I = ""

	index = 0

	codewordIndex = 256

	tam = len(data)
	
	while index < tam:
		c = copy.copy(data[index])
		if I+c in dict.values():
			I = copy.copy(I+c)

		else:
			for i,j in dict.items():
				if j == I:
					compressed += " ".join([str(p) for p in index_to_codeword(i, codeSize)])+" "
					break
			dict[codewordIndex] = copy.copy(I+c)
			codewordIndex += 1
			I = copy.copy(c)
			
			#print(int(index*100/tam))
		index += 1

	for i,j in dict.items():
		if j == I:
			compressed +=  " ".join([str(p) for p in index_to_codeword(i, codeSize)])
			break
	#print(compressed)
	#input()
	finalFile = ""
	compressed = compressed.split(" ")
	for i in compressed:
		finalFile += chr(int(i))
	return finalFile
			
  


"""
	DESCOMPACTAÇÃO LZW
	
	1. No início o dicionário contém todas as raízes possíveis;
	2. cW <= primeira palavra-código na sequência codificada (sempre é uma raiz);
	3. Coloque a string(cW) na sequência de saída;
	4. pW <= cW;
	5. cW <= próxima palavra código da sequência codificada;
	6. A string(cW) existe no dicionário ?
		a. se sim,
			i. coloque a string(cW) na sequência de saída;
			ii. P <= string(pW);
			iii. C <= primeiro caracter da string(cW);
			iv. adicione a string P+C ao dicionário;
		b. se não,
			i. P <= string(pW);
			ii. C <= primeiro caracter da string(pW);
			iii. coloque a string P+C na sequência de saída e adicione-a ao dicionário;
	7. Existem mais palavras código na sequência codificada ?
		a. se sim,
			i. volte ao passo 4;
		b. se não,
			i. FIM.
"""


def descompactar_lzw(compressed, codeSize):
	def codeword_to_index(code, codesize):
		code = [ord(i) for i in code]
		code = tuple(code)
	
		for k,i in enumerate(product(range(256), repeat=codesize)):
			if i == code:
				return k
	   
		  
	#compressed = deque([chr(i) for i in compressed])
	compressed = list(compressed)
	#print(compressed)
   

	decompressed = ""
	dict = {}

	for i in range(256):
		dict[i] = chr(i)

	cW = []
	for i in range(codeSize):
		cW.append(compressed.pop(0))


	decompressed += dict[codeword_to_index(cW, codeSize)]
	 

	while compressed:
		pW = codeword_to_index(cW, codeSize)
		cW = []
		for i in range(codeSize):
			cW.append(compressed.pop(0))
		
		index = codeword_to_index(cW, codeSize)
		
		
		if index in dict:
			decompressed += dict[index]
			P = copy.copy(dict[pW])
			C = copy.copy(dict[index][0])
			nextIndex = len(dict)
			dict[nextIndex] = copy.copy(P+C)
		else:
			P = copy.copy(dict[pW])
			C = copy.copy(dict[pW][0])
			decompressed += copy.copy(P+C)
			nextIndex = len(dict)
			dict[nextIndex] = copy.copy(P+C)
			
		
			
	return decompressed

		


while True:
	print("-"*60)
	print("Compactador de Arquivos - LZW")
	print("Escolha uma opção:")
	print("1-Compactar")
	print("2-Descompactar")
	opc = input(">")
	if opc=='1':
		nome = input("Nome do arquivo com a extensão:")
		

		#path = os.path.join(url,file).decode("utf8")
		file = open(nome, "rb").read()
		
		print("Compactando...")
		tempOut = compactar_lzw(file, 3)
		
		output = open("COMPACTADO-"+nome,"w")
		
		for i in tempOut:
			output.write(i)
		
		output.close()
		
		print("Tamanho compactado:", len(tempOut), "bytes.")
	elif opc=='2':
		nome = input("Nome do arquivo com a extensão:")
		
		file = open(nome, "r").read()
		
		print("Descompactando...")
		tempOut = descompactar_lzw(file, 3)
		
		output = open("DESCOMPACTADO-"+nome,"w")
		
		for i in tempOut:
			output.write(i)
		
		output.close()
		
		print("Tamanho descompactado:", len(tempOut), "bytes.")
		

		