def criar_perfil(nome, idade, cidade):
    print(f"{nome}, {idade}, {cidade}")

criar_perfil(cidade="Curitiba", nome="Test", idade=25)
#Test, 25, Curitiba
#quando é chamado a função, a sequencia sempre vai ser definidada pela funçao

criar_perfil("TestSequencia", 25, "Curitiba")
#TestSequencia, 25, Curitiba