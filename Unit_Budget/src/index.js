// This method is for role identification
var el_down = document.getElementById("GFG_DOWN");
function GFG_click(clicked) {
     el_down.innerHTML = "You are the "+clicked+".";
}

function showAndHide() {
  const x = document.getElementById("radio");
  if (x.style.display == "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

const buildSearchParams = (year, semester, unitcode) => {
  const queryParams = new URLSearchParams();
  if(year) {
    queryParams.append("year", year);
  }
  if(semester) {
    queryParams.append("semester", semester);
  }
  if(unitcode) {
    queryParams.append("unitcode", unitcode);
  }

  return queryParams;
}
/**
 * List all reports.
 * 
 * @param {*} year The year when the report is created.
 * @param {*} semester The semester which the report targets to.
 * @param {*} unitcode The Unit code which the report targets to.
 */ 
const getAllData = async(year, semester, unitcode) => {
  const queryParams = buildSearchParams(year, semester, unitcode);
  const result = await fetch('http://127.0.0.1:5000/get_all_data?' + queryParams, {
    method:"GET",
    headers:{
      headers: {
        "Content-Type":"application/json"
      }
    }
  });

  const data = await result.json();
  window.onload(data);
  return data;
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
const getEmployeeData = (year, semester, unitcode) => {
  const queryParams = buildSearchParams(year, semester, unitcode);
  fetch('http://127.0.0.1:5000/employee_budget?' + queryParams, {
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

const getWorkLoadData = function (year, semester, unitcode) {
  const queryParams = buildSearchParams(year, semester, unitcode);
  fetch('http://127.0.0.1:5000/workload?' + queryParams, {
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





