{ aluno: Rodrigo Paula 

da Silva}}

10.3
3e10
3 <> 5
3 <= 5
3 >= 5
!(3 >= 5)

inteiro: tamanho
tamanho:= 10
inteiro: array[tamanho]
		
bubbleSort(inteiro: arr[], inteiro: n)
	inteiro: i
	inteiro: j
	inteiro: temp
	i:=0
	j:=0
	repita
		repita
			se arr[j] > arr[j+1] então
				temp := arr[j]
				arr[j] := arr[j+1]
				arr[j+1] := arr[j]
			fim
			j:= j+1
		até j == n-i-1
		i:= i+1
	até i == n-1
fim

inteiro principal()
	inteiro: i
	i:=0
	repita
		leia(array[i])
		i:= i+1
	até  i == tamanho
	escreva(bubbleSort(array, tamanho))
	retorna(0)
fim

				
			
	
