
function myFunction() {
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById("srchInput");
  filter = input.value.toUpperCase();
  ul = document.getElementById("srchUL");
  li = ul.getElementsByTagName("li");
  for (i = 0; i < li.length; i++) {
      a = li[i].getElementsByTagName("a")[0];
      txtValue = a.textContent || a.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
          li[i].style.display = "";
      } else {
          li[i].style.display = "none";
      }
  }
}


function SMRYfunction() {
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById("srchSMRYInput");
  filter = input.value.toUpperCase();
  ul = document.getElementById("srchSMRY");
  li = ul.getElementsByTagName("li");
  for (i = 0; i < li.length; i++) {
      a = li[i].getElementsByTagName("a")[0];
      txtValue = a.textContent || a.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
          li[i].style.display = "";
      } else {
          li[i].style.display = "none";
      }
  }
}


function RCDfunction() {
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById("srchRCDInput");
  filter = input.value.toUpperCase();
  ul = document.getElementById("srchRCD");
  li = ul.getElementsByTagName("li");
  for (i = 0; i < li.length; i++) {
      a = li[i].getElementsByTagName("a")[0];
      txtValue = a.textContent || a.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
          li[i].style.display = "";
      } else {
          li[i].style.display = "none";
      }
  }
}



function delete_receipt(id){    
    /*console.log(id)*/
    window.confirm("deleting receipt:", id);
    location.reload()

    var url = '/update_receipt/'
    fetch(url,{
        method: 'POST',
        headers: {
         'Content-Type':'application/json',
         'X-CSRFToken':csrftoken},
         body:JSON.stringify({'rctId':id})             
    })   
}



function show_addReceipt(){
    hide_show_addreceipt_form('R')
    /*console.log("next lesson")*/
  }


/*function to hide or show lesson addReceipt*/
function hide_show_addreceipt_form(id){
    document.getElementById(id).classList.toggle('hidden')
  }










  function getToken(name) {
    let csrftoken = null;          
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();

            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                csrftoken = decodeURIComponent(cookie.substring(name.length + 1));

                break;
            }
        }
    }           
    return csrftoken;
  }
  var csrftoken = getToken('csrftoken')