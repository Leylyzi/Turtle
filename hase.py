function main() {
	turtle->setSpeed(5000)
	for(var i < 360) {
		turtle->strichkreis(i)
	}
	turtle->forward(100)
	for(var j < 360) {
		turtle->strichkreis(j)
	}
	turtle->forward(100)
	for(var k < 360) {
		turtle->strichkreis(k)
	}
	turtle->back(300)
	for(var l < 360) {
		turtle->strichkreis(l)
	}
	turtle->leftTurn(90)
	turtle->forward(90)
	turtle->rightTurn(90)
	turtle->forward(20)
	for(var m < 360) {
		turtle->strichkreis(m)
	}
	turtle->forward(100)
	for(var n < 360) {
		turtle->strichkreis(n)
	}
	turtle->forward(100)
	for(var o < 360) {
		turtle->strichkreis(o)
	}
	turtle->forward(100)
	for(var p < 360) {
		turtle->strichkreis(p)
	}
}
turtle->learnWord->strichkreis(colour) {
	turtle->penDown()
	turtle->setPenColor(colour)
	turtle->forward(69)
	turtle->penUp()
	turtle->back(68)
	turtle->rightTurn(1)
}
