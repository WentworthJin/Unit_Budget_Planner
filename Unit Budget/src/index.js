// This method is for role identification
  var el_down = document.getElementById("GFG_DOWN");
  function GFG_click(clicked) {
      el_down.innerHTML = "You are the "+clicked+".";
  }

// document.getElementById('role1').onclick = function(){
//     this.style.backgroundColor = 'Yellow';
// };

function showAndHide() {
  const x = document.getElementById("radio");
  if (x.style.display == "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

// get the data from database 
const getAllData = () => {
  fetch('http://127.0.0.1:5000/get_all_data', {
    method:"GET",
    headers:{
      headers: {
        "Content-Type":"application/json"
      }
    }
  })
  .then(resp => resp.json())
  .then((data) => 
    window.onload(data))
  .catch(error => 
    console.log(error))
}


// make the data dynamic changing
// drawing a bar chart 
window.onload = function (data) {
  var chart = new CanvasJS.Chart("barchart", {

    title:{
      text: "Unit Budget"              
    },
    data: [//array of dataSeries              
      { //dataSeries object

       /*** Change type "column" to "bar", "area", "line" or "pie"***/
       type: "column",
       dataPoints: [
       { label: data[0][0], y: data[0][1] },
       { label: data[1][0], y: data[1][1] },
       { label: data[2][0], y: data[2][1] },                                    
       ]
     }
     ],
    axisY:{
      prefix: "$",
      suffix: "K"
    }     
    
  });
  chart.render();
}

getAllData()

// drawing a stack bar chart 
var stack = document.getElementById("stack")
var stack_chart = new CanvasJS.Chart(stack, {

  theme: "light2",
        
  title:{
    text: "Budget for Semester 1 and 2"              
  },

  data: [  //array of dataSeries     
  { //dataSeries - first quarter
/*** Change type "column" to "bar", "area", "line" or "pie"***/        
    type: "column",
    name: "First Semester",
    showInLegend: true,
    dataPoints: [
    { label: "CITS5508", y: 58 },
    { label: "CITS5503", y: 69 },
    { label: "CITS5206", y: 80 },                                    
    { label: "CITS5506", y: 74 },
    { label: "CITS5501", y: 64 }
    ]
  },

  { //dataSeries - second quarter

  type: "column",
  name: "Second Semester", 
  showInLegend: true,               
  dataPoints: [
  { label: "CITS5508", y: 63 },
  { label: "CITS5503", y: 73 },
  { label: "CITS5206", y: 88 },                                    
  { label: "CITS5506", y: 77 },
  { label: "CITS5501", y: 60 }
  ]
}
],
/** Set axisY properties here*/
  axisY:{
    prefix: "$",
    suffix: "K"
  }    
});

stack_chart.render()
