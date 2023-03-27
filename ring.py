function main() {
	turtle->setPenSize(1000)
	turtle->setSpeed(1000)
	for(var i < 18) {
		turtle->setPenColor(red)
		turtle->nEck(10,20)
		turtle->setPenColor(orange)
		turtle->back(20)
		turtle->leftTurn(20)
		# end
		turtle->setPenColor(yellow)
		turtle->forward(100)
		turtle->setPenColor(green)
		turtle->back(100)
		turtle->nEck(60,20)
		turtle->setPenColor(blue)
		turtle->nEck(57,20)
		turtle->setPenColor(black)
		turtle->nEck(50,20)
		turtle->setPenColor(purple)
		turtle->nEck(45,20)
		turtle->setPenColor(pink)
		turtle->nEck(40,20)
	}
}
turtle->learnWord->nEck(laenge,ecken) {
	for(var j < ecken) {
		turtle->forward(laenge)
		turtle->leftTurn(360/ecken)
	}
}
