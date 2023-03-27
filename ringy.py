function main() {
	turtle->setPenColor(red)
	turtle->setPenSize(500)
	turtle->nEck(10,20)
	turtle->setPenColor(yellow)
	turtle->setPenSize(100)
	turtle->nEck(5,20)
	turtle->setPenSize(40)
	turtle->penUp()
	turtle->setPenColor(green)
	turtle->back(350)
	turtle->penDown()
	turtle->back(300)
}
turtle->learnWord->nEck(laenge,ecken) {
	for(var i < ecken) {
		turtle->forward(laenge)
		turtle->leftTurn(360/ecken)
	}
}
