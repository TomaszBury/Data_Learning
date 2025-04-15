pokemons = matrix(c(120, 100, 40, 50, 80, 36, 40, 10, 25, 30,3, 1, 1, 1, 2), nrow=5, ncol=3)


dimnames(pokemons) <- list(c("Blastoise", "Moltres", "Pikachu", "Pidgey",'Charmeleon'),c("HP", "Level", "Stage"))
pokemons

dragonite <- matrix(c(150,50,3),nrow=1,ncol=3,dimnames = list(c('Dragonite'),c("HP", "Level", "Stage")))


full_pokemons = rbind(dragonite,pokemons)

full_pokemons
