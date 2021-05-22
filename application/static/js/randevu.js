$(function () 
{
    document.querySelector("#kaydet-btn").addEventListener("click", kaydet, false);
    
    $('#sandbox-container').datepicker({
        maxViewMode: 0,
        todayBtn: "linked",
        clearBtn: true,
        language: "tr",
        todayHighlight: true
    });

    function kaydet(){
        var input_time = $('#time-input').val();
        $.post("http://127.0.0.1:5000/randevu/kaydet",
        {
            time: input_time,
        },
        function(data, status){
            alert("Data: " + data + "\nStatus: " + status);
        });     
     }
  });