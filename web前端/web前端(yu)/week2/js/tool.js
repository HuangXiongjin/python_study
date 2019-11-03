function randomColor(a=1){
	red = parseInt(Math.random()*255)
	green = parseInt(Math.random()*255)
	blue = parseInt(Math.random()*255)
	return 'rgba('+red+','+green+','+blue+','+a+')'
}
