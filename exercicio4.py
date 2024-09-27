

SP= 67836.43
RJ= 36678.66
MG =29229.88
ES = 27165.48
outros=19849.53
somav = SP+RJ+MG+ES+outros
PercentualSp = int((SP/somav)*100)
Percentualrj= int((RJ/somav)*100)
PercentualMg = int((MG/somav)*100)
PercentualEs = int((ES/somav)*100)
PercentualOutros = int((outros/somav)*100)
print("O estado do Rio de janeiro representa "+str(Percentualrj)+ "% do valor mensal da distribuidora")
print("O estado de São paulo representa "+str(PercentualSp)+ "% do valor mensal da distribuidora" )
print("O estado de Minas gerais representa "+ str(PercentualMg)+ "% do valor mensal da distribuidora")
print("O estado de Es pirito santo representa "+ str(PercentualEs)+ "% do valor mensal da distribuidora" )
print("Os outros estados representam "+str(PercentualOutros)+ "% do valor mensal da distribuidora")


