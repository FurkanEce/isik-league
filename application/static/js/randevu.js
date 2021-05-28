$(function () 
{
    var secilen_saat = null;
    document.querySelector("#kaydet-btn").addEventListener("click", kaydet, false);
    for(var i=0;i<24;i++){
        document.querySelector("#saat-" + i).addEventListener("click", saat_kaydet, false);
    }
    
    
    $('#tarih').datepicker({
        format: "yyyy-mm-dd",
        maxViewMode: 0,
        todayBtn: "linked",
        language: "tr",
        todayHighlight: true
    });

    function saat_kaydet(){
        secilen_saat = $(this).text();
    }

    function kaydet(){
        var input_time = $('#tarih').datepicker('getFormattedDate');
        $.post("http://127.0.0.1:5000/randevu/kaydet",
        {
            tarih: input_time,
            saat: secilen_saat,
            saha: $("#saha :selected").val()
        },
        function(data, status){
            window.location.href = 'http://127.0.0.1:5000/profile'
        });
    }

    $('#tarih').on('changeDate', function() {
        var secilen_saha = $("#saha :selected").val();
        var input_time = $('#tarih').datepicker('getFormattedDate');
        window.location.href = 'http://127.0.0.1:5000/randevu/'+ secilen_saha + '/' + input_time;
    });

  });