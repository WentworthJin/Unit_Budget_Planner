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


// drawing a bar chart 
window.onload = function (data) {
  const dataArray = []
  for(var i = 0; i < data.length; i++){
    dataArray.push({"label":data[i][0], "y":data[i][7]})
  } 
  
  var chart = new CanvasJS.Chart("barchart", {

    title:{
      text: "Unit Budget"              
    },
    data: [//array of dataSeries              
      { //dataSeries object

       /*** Change type "column" to "bar", "area", "line" or "pie"***/
       type: "column",
       dataPoints: dataArray
     }
     ],
    axisY:{
      prefix: "$",
    }     
    
  });
  chart.render();
}


// get the data to plot the graph 
const getEmployeeData = () => {
  fetch('http://127.0.0.1:5000/employee_budget', {
    method:"GET",
    headers:{
      headers: {
        "Content-Type":"application/json"
      }
    }
  })
  .then(resp => resp.json())
  .then((data) =>
    horizontalbarchart(data)
  )
  .catch(error => 
    console.log(error))
}

const horizontalbarchart = function (data) {
  const dataArray = []
  for(var i = 0; i < data.length; i++){
    dataArray.push({"y":data[i][4], "label":data[i][0]})
  };

  var horizontal = document.getElementById("horizontal")
  var bar_chart = new CanvasJS.Chart(horizontal, {
    title:{
      text: "Budget for each employees"              
    },
    data: [//array of dataSeries              
      { //dataSeries object

       /*** Change type "column" to "bar", "area", "line" or "pie"***/
       type: "column",
       dataPoints: dataArray
      }
    ],
    axisY:{
      prefix: "$",
    }     
    
  });
  bar_chart.render();
}



// drawing a stack bar chart 

const graphing =  function() {
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
}

getAllData()
getEmployeeData()
graphing()




