let textBox = document.getElementById("one");

function whenClicked(){
  let value = textBox.value;
  if(value.length < 10){ console.log("input is small...");}
  var count=0;
  for(var index=0;index < value.length;index++){
    if(value.charAt(index) == 'A' || value.charAt(index) == 'a'){
        count = count+1;
    } 
  }
  
   console.log(count);
  
  console.log("Clicked.... "+value.length);
}

let button = document.getElementById("two");

button.onclick = whenClicked;
