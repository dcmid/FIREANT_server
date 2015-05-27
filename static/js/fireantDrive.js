currentKey = '';
img = document.getElementById("arrows");
function hit(key){
	xmlhttp=new XMLHttpRequest();
	switch(key.keyCode){
		//W or up
		case 87:
		case 38:
			if(currentKey != 'W')
			{
				img.src="static/img/directionUp.png";
				console.log("FORWARD");
				currentKey = 'W';
				xmlhttp.open('GET', '/forward');
				xmlhttp.send();
			}
			break;
		//A or left
		case 65:
		case 37:
			if(currentKey != 'A')
			{
				img.src="static/img/directionLeft.png";
				console.log("LEFT");
				currentKey = 'A';
				xmlhttp.open('GET', '/left');
				xmlhttp.send();
			}
			break;
		//S or down
		case 83:
		case 40:
			if(currentKey != 'S')
			{
				img.src="static/img/directionDown.png";
				console.log("BACKWARD");
				currentKey = 'S';
				xmlhttp.open('GET', '/backward');
				xmlhttp.send();
			}
			break;
		//D
		case 68:
		case 39:
			if(currentKey != 'D')
			{
				img.src="static/img/directionRight.png";
				console.log("RIGHT");
				currentKey = 'D';
				xmlhttp.open('GET', '/right');
				xmlhttp.send();
			}
			break;
		default:
			img.src="static/img/directionalKeys.png";
			currentKey = '';
			xmlhttp.open('GET', '/stop');
			xmlhttp.send();
	}
}

function stop(e){
	img.src="static/img/directionalKeys.png";
	console.log("STOP")
	currentKey = '';
	xmlhttp=new XMLHttpRequest();
	xmlhttp.open('GET', '/stop');
	xmlhttp.send();
}

function hideLoader(){
	document.getElementById("loading").style.visibility="hidden";
}

function errorImage (){
	hideLoader();
	document.getElementById("stream").src="static/img/offline.png";
}

function shutdown(){
	xmlhttp=new XMLHttpRequest();
	xmlhttp.open('GET','/shutdown');
	xmlhttp.send();
}

document.onkeydown = hit;
document.onkeyup = stop;