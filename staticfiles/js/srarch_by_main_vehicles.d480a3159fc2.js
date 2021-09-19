

var Choose2 = '<option value="">Choose</option>'
    

$("#id_sub").change(function () {
    var subId = $(this).val();
    var url2 = ("{% url 'ads:load_sub'%}")
    var mainId = 43;
    $("#id_last").html(Choose2);
    if (subId !== "") {
      console.log("55555");
      $.ajax({
        url: url2,
        data: {
          'main': mainId,
          'sub': subId
        },
        success: function (data) {
          $("#id_end").html(data);
        }
      });
    }
    else {
      console.log("4444444");
      $("#id_last").html(Choose2);
      $("#id_end").html(Choose2);
    }
  });
  $("#id_end").change(function () {
    var url = $("#adsform").attr("data-url");
    var endId = $(this).val(); 
    var mainId = 43
    var subId = $("#id_sub").val();
    var url2 = ("{% url 'ads:load_sub'%}");
    if (endId !== "") {
      console.log("55555");
      $.ajax({
        url: url2,
        data: {
          'main':mainId ,
          'sub': subId ,
          'end': endId      
        },
        success: function (data) {
          $("#id_last").html(data);
        }
      });
    }
    else {
      console.log("4444444");
      $("#id_last").html(Choose2);
    }
  });


