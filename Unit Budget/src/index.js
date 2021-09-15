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

// drawing a bar chart 
window.onload = function () {
  var chart = new CanvasJS.Chart("barchart", {

    title:{
      text: "Unit Budget"              
    },
    data: [//array of dataSeries              
      { //dataSeries object

       /*** Change type "column" to "bar", "area", "line" or "pie"***/
       type: "column",
       dataPoints: [
       { label: "CITS5508", y: 18 },
       { label: "CITS5503", y: 29 },
       { label: "CITS5206", y: 40 },                                    
       { label: "CITS5506", y: 34 },
       { label: "CITS5501", y: 24 }
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
