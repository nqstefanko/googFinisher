
{% block script %}

function ChangeColorOfIndex(index)
{
	$("#" + index.toString()).css('color', 'red');
    $('#userInput').val("");
    $("#answer").text("Got One!");
}

var success = 0;

function showAnswers()
{
	for(var i = 0;i <= 5;i++)
	{
		console.log(i);
		ChangeColorOfIndex(i);
	}
	$("#answer").text("Click Reset!");
}

$(document).ready(function(){
	var AutoCompleteWords = [];

	var AlreadyGot = []

	var i = 1;
	
	{% for word in words[1:6] %}
		$("#" + i.toString()).text("{{word}}")
		AutoCompleteWords.push("{{word}}");
		i++;
	{% endfor %}

	console.log(AutoCompleteWords);

  $("#userInput").keyup(function(event) {
      if (event.keyCode === 13) {
		if(success >= 5)
      		{
				console.log("WE IN");
				location.href = "/index";
      		}
      	if ((AutoCompleteWords.indexOf($('#userInput').val()) >= 0) && (AlreadyGot.indexOf($('#userInput').val()) < 0))
      	{

      		var index = AutoCompleteWords.indexOf($('#userInput').val());//Get Index of Correct Answer!
      		index++;
      		
      		AlreadyGot.push($('#userInput').val());//Add it to array of already typed in Correctly

      		ChangeColorOfIndex(index);
      		success++;
      		
      		if(success >= 5)
      		{
      			$("#answer").text("Got them All! Hit Enter to Reset!");
      		}

      	} else {  
      		if(success < 5)
      		{		
        		$("#answer").text("Try Again!");
			}
        }
      }
})});
{%endblock%}