def basePowerCallback(pokemon, target, move):
# function (pokemon, target, move) {
# 			if (!pokemon.item) {
# 				this.debug("Power doubled for no item");
# 				return move.basePower * 2;
# 			}
# 			return move.basePower;
# 		}
    if pokemon.item == None:
        #Power doubled for no item
        return move.basePower * 2
    else:
        return move.basePower
