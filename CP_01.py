Nome = str(input("Nome do vendedor: "))
salario_fixo = float(input("Sálario fixo: "))


setor_feminino = float(input("Valor total vendido no Setor Feminino: ")) 
setor_masculino = float(input("Valor total vendido no Setor Masculino: "))
setor_infantil = float(input("Valor total vendido no Setor Infantil: "))
setor_beleza = float(input("Valor total vendido no Setor Beleza : "))



comissao_feminino =  setor_feminino * 2/100
comissao_masculino = setor_masculino * 2/100
comissao_infantil = setor_infantil * 4/100
comissao_beleza = setor_beleza * 6/100
comissao_total = comissao_feminino + comissao_masculino + comissao_infantil + comissao_beleza
salario_total = salario_fixo + comissao_total



print("Prezado(a)", Nome,"\nSeu salário fixo é de",salario_fixo, "reais e sua comissão referente o mês vigente foi calculado em",
comissao_total, "reais\nTotal a receber: ", salario_total,"reais")


