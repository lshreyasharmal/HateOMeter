(function(console){

    console.save = function(data, filename){

        if(!data) {
            console.error('Console.save: No data')
            return;
        }

        if(!filename) filename = 'console.json'

        if(typeof data === "object"){
            data = JSON.stringify(data, undefined, 4)
        }

        var blob = new Blob([data], {type: 'text/json'}),
            e    = document.createEvent('MouseEvents'),
            a    = document.createElement('a')

        a.download = filename
        a.href = window.URL.createObjectURL(blob)
        a.dataset.downloadurl =  ['text/json', a.download, a.href].join(':')
        e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
        a.dispatchEvent(e)
    }
})(console)

$(document).ready(function() {
  if( document.getElementsByClassName("commentarea") !== null ) {
    var elements = $(".usertext-body").find("p").clone();
    var finalStr = ""
    var object={
    	table :[]
    };
    var ind=0;
      $(elements).each(function() {

        console.log(this.innerHTML);
      	var str1 = this.innerHTML;
          object.table.push({
          	id:ind, 
          	message:str1
          });
      	ind=ind+1;
      });
      var temp = JSON.stringify(object);
      console.log(temp);
      // console.save(JSON.stringify(object),"mybest.json");
 		  // sessionStorage.setItem


      // var xhr = new XMLHttpRequest();
      // var url = "http://localhost:8000/data/";
      // xhr.open("POST", url, true);
      // xhr.setRequestHeader("Content-type", "application/json");
      // xhr.onreadystatechange = function () {
      //     if (xhr.readyState === 4 && xhr.status === 200) {
      //         var json = JSON.parse(xhr.responseText);
      //         console.log(json);
      //     }
      // };
      // var data = temp;
      // xhr.send(data);
      $.ajax({
      	type: 'POST',
      	url: 'https://localhost:8000/data/',
      	data: temp,
      	dataType: "json",
        contentType: "application/json; charset=utf-8",
        crossDomain: true,
      	success: function(data){
      		alert(data);
      	},
      	error: function(data){
      		alert("Sorry");
      	}

      });

     
/*          chrome.runtime.sendMessage({
            method: 'POST',
            data: temp,
            dataType: "json",
            url: "http://127.0.0.1:8000/data/",
            success: function(data){
            	alert("It worked");
            },
            error: function(data){
            	alert("Sorry");
            }
            
          });*/
    }
});

/**/