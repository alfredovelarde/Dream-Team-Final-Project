function testmodel(){
function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

var server = "http://127.0.0.1:5000/test";

var button = d3.select('#button1');
	button.on("click",function(event){
		hotel=d3.select('#hotel').property('value');
		sweekend=getRandomInt(51);
		sweek=getRandomInt(19);
		adults = d3.select('#adults').property('value');
		children = d3.select('#children').property('value');
		babies = 0;
		meal=getRandomInt(5);
		marketsegment= getRandomInt(8);
		distchannel=getRandomInt(5);
		isrepetguest=getRandomInt(2);
		previus_cancel=getRandomInt(28);
		previus_not_cancel =getRandomInt(28);
		reserved_room_type=getRandomInt(10);
		assigned_room_type =getRandomInt(12);
		booking_change = getRandomInt(22);
		dtype=d3.select('#deposittype').property('value');
		agent=getRandomInt(2);
		company=getRandomInt(2);
		ctype=d3.select('#customertype').property('value');
		car_spaces=getRandomInt(5);
		special_request=getRandomInt(6);

		

if (adults === "" ) {
    window.alert("You need to put one adult");

  } 
 else {
 	    if (children === "") {
    	children=0;
    	data={'data':[parseInt(hotel),sweekend,sweek,parseInt(adults),parseInt(children),babies,meal,marketsegment,distchannel,isrepetguest,previus_cancel,previus_not_cancel,reserved_room_type,assigned_room_type,booking_change,parseInt(dtype),agent,company,parseInt(ctype),car_spaces,special_request]};
    	console.log(data)
d3.json(server, {
      method:"POST",
      body: JSON.stringify(data),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
    .then(function(json) {
   console.log(json.result[0]);
     if (json.result[0] === "0") {
   document.getElementById("model1").style.visibility = "visible";
   document.getElementById("model2").style.visibility = "hidden";
   }else{
   document.getElementById("model1").style.visibility = "hidden";
   document.getElementById("model2").style.visibility = "visible";

   }
    });


    }
    else{
    	data={'data':[parseInt(hotel),sweekend,sweek,parseInt(adults),parseInt(children),babies,meal,marketsegment,distchannel,isrepetguest,previus_cancel,previus_not_cancel,reserved_room_type,assigned_room_type,booking_change,parseInt(dtype),agent,company,parseInt(ctype),car_spaces,special_request]};
d3.json(server, {
      method:"POST",
      body: JSON.stringify(data),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
    .then(function(json) {
   console.log(json.result[0]);
   if (json.result[0] === "0") {
   document.getElementById("model1").style.visibility = "visible";
   document.getElementById("model2").style.visibility = "hidden";
   }else{
   document.getElementById("model1").style.visibility = "hidden";
   document.getElementById("model2").style.visibility = "visible";

   }
    });

    }


 }
	
	});

}

testmodel();