
function myFunction() {
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById("srchInput");
  filter = input.value.toUpperCase();
  /*console.log("input: ", filter)*/
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
  /*console.log("input: ", filter)*/
  ul = document.getElementById("srchRCD");
  li = ul.getElementsByTagName("li");
  for (i = 0; i < li.length; i++) {
      a = li[i].getElementsByTagName("a")[0];
      console.log("input: ", a)
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




function PLGfunction() {
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById("srchPLGinput");
  filter = input.value.toUpperCase();
  ul = document.getElementById("srchPLG");
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

















/*YEARLY PLEDGE DOWNLOADS*/
/*function yearlypledge(yr){    
  console.log(yr)
  location.href = '/yearlypledge/yr/'
  window.confirm("deleting receipt:", id);
  location.reload()

  var url = '/yearlypledge/'
  fetch(url,{
      method: 'POST',
      headers: {
       'Content-Type':'application/json',
       'X-CSRFToken':csrftoken},
       body:JSON.stringify({'yr':yr})             
  })  
}*/







function registered(){
    console.log('clicked')
    var url = '/ContactData/'
    location.href = url
  }

  function receipts(){
    console.log('clicked')
    var url = '/ReceiptsData/'
    location.href = url
  }


function pledges(){
    console.log('clicked')
    var url = '/member-search/'
    location.href = url
}

function contact(){
    console.log('clicked')
    var url = '/member-search/'
    location.href = url
}


function Members_Pledges(){
    hide_show_submenu("MP")
    console.log('clicked')
  }

  function Members_Pledge_Payments(){
    hide_show_submenu("MPP")
    console.log("clicked")
  }

  function Members_Pledge_Balance(){
    hide_show_submenu('MPB')
    console.log("clicked")
  }


  /*function to hide or show submenu*/
function hide_show_submenu(id){
    document.getElementById(id).classList.toggle('hidden')
  }












/*function to pass data to view*/
function getdata_in_view(url,dt){
  var url = url
    fetch(url,{
        method: 'POST',
        headers: {
         'Content-Type':'application/json',
         'X-CSRFToken':csrftoken},
         body:JSON.stringify({'dt':dt})             
    })
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