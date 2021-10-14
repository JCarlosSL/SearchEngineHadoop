
$(document).ready(function() {
    
    $('input[type=image]').click(function() {

        $('#pages div').empty();

        $.ajax({ 
                url: '/search',
                data: JSON.stringify({ "words" : $('#words').val() } ),
                type: 'POST',
                contentType: "application/json; charset=utf-8",
                dataType: "json"
            }).done(function(data) {
                console.log("paginas :",data)
            
                var size = data.length

                console.log(size)

                if (size) {
                    for(var i=0; i<size ;i++) {
                    	var text_data=""
                    	
                        var rawFile = new XMLHttpRequest();
                        rawFile.open("GET", '/static/corpus/'+data[i][0], false);
                        rawFile.onreadystatechange = function (){
				if(rawFile.readyState === 4){
				    if(rawFile.status === 200 || rawFile.status == 0){
					var allText = rawFile.responseText;
					var data_list=allText.split(" ");
					for(var k=0 in data_list ){
						if( data[i][1][1].toLowerCase().localeCompare(data_list[k].toLowerCase()) === 0){
							for(var j=k;j<5+k;j++){
								text_data += data_list[j]+" ";
							}
							break;
						}
					}
				    }
				}
			}
			rawFile.send(null);
                        var div = $('<div> </div>', {});
			var p = $("<p>" + data[i][0] + "<span id='url_link'><a target='_blank' href=\"/static/corpus/" +data[i][0] + "\">" +  data[i][0]+ "</a></span></p><p>ggg</p>",{});
                        //var p = $('<p>'+data[i][1][1]+' - PageRank: '+data[i][1][0]+' -URL: <a href="/static/corpus/'+data[i][0]+'" target="_blank">'+data[i][0]+'</a></p>',{});
                        text_data="";
                        div.append(p)
                        div.appendTo($('#pages'));     
                        
                    }
                }
                else {
                    var div = $('<div> </div>', {});
            
                    var p = $('<p> No se encontraron resultados!</p>',{});

                    div.append(p)

                    div.appendTo($('#pages'));     
                }
             
            }).fail(function() {
                console.log('Failed');
        });        
    });    
});
