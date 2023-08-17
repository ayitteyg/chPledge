


function showLesson(){
         
    console.log("button clicked"+'george')
    document.getElementById('showMenu').classList.toggle('hidden')
}


document.getElementById('A').addEventListener('click', ()=>{
   
    console.log('caret cliked')
    document.getElementById('1').classList.toggle('show')
    document.getElementById('A1').classList.toggle('rotate')
  })




document.getElementById('A1A').addEventListener('click', ()=>{
  /*showLesson()*/
  console.log('level cliked')
  document.getElementById('L1').classList.toggle('show')
  document.getElementById('1a').classList.toggle('rotate')
  /*document.getElementById('alg').classList.toggle('hidden')*/
  })
  

  
  /*document.getElementById('A1i').addEventListener('click', ()=>{
    showLesson()
    
    console.log('level cliked:')

    var id = return_page(self)
    console.log('id retured:',id)
    document.getElementById('alg').classList.toggle('hidden')
    })*/
  

function return_page(self){
  var id = String(self.id)
  console.log('id retured:',id)
  document.getElementById('alg').classList.toggle('hidden')

  


}

