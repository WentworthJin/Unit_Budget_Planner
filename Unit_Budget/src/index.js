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
    animationEnabled: true,
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
    animationEnabled: true,
    data: [//array of dataSeries              
      { 
       type: "bar",
       dataPoints: dataArray
      }
    ],
    axisY:{
      prefix: "$",
    }     
    
  });
  bar_chart.render();
}

const getWorkLoadData = function () {
  fetch('http://127.0.0.1:5000/workload', {
    method:"GET",
    headers:{
      headers: {
        "Content-Type":"application/json"
      }
    }
  })
  .then(resp => resp.json())
  .then((data) =>
    graphing(data)
  )
  .catch(error => 
    console.log(error))
}

// drawing a stack bar chart 
const graphing =  function(data) {
  const workload = []
  const staffCost = []
  for(var i = 0; i < data.length; i++){
    workload.push({"label":data[i][0], "y":data[i][1]})
    staffCost.push({"label":data[i][0], "y":data[i][2]})
  };


  var stack = document.getElementById("stack")
  var stack_chart = new CanvasJS.Chart(stack, {

  theme: "light2",
  animationEnabled: true,
  title:{
    text: "Workload VS Total Cost"              
  },

  data: [  //array of dataSeries     
  {     
    type: "column",
    name: "Workload",
    showInLegend: true,
    dataPoints: workload
  },

  { //dataSeries - second quarter

  type: "column",
  name: "StaffCost", 
  showInLegend: true,               
  dataPoints: staffCost
}
],
/** Set axisY properties here*/
  axisY:{
    prefix: "$",
  }    
});

stack_chart.render()
}

getAllData()
getWorkLoadData()
getEmployeeData()
<<<<<<< HEAD
graphing()
=======





>>>>>>> 2d75713550cd9e932d35271f2c6b63852d544b3e
