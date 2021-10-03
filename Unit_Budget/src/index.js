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

/**
 * Build SearchParams to include supplied queries.
 * 
 * @param year The year when a report is created.
 * @param semester The semester a report targets to.
 * @param unitcode The Unit code a report targets to.
 */
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
 * function fetch the data and return a response of an array of data 
 * pass into the window.onload for plot the bar graph
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

/**
 * Plot a bar graph 
 * @param data type=array, receive data from server 
 * plot the data dynamically based on data from database 
 */
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


/**
 * function fetch the data and return a response of an array of data 
 * pass into the horizontal bar chart for plot the horizontal bar chart
 * 
 * @param year The year when the report is created.
 * @param semester The semester which the report targets to.
 * @param unitcode The Unit code which the report targets to.
 */ 
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


/**
 * Plot the horizontal bar graph 
 * @param data, type=array, receive data from server 
 * plot the data dynamically based on data from database 
 */
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

/**
 * function fetch the data and return a response of an array of data 
 * pass into the graphing for plot the cluster bar chart 
 *
 * @param year The year when the report is created.
 * @param semester The semester which the report targets to.
 * @param unitcode The Unit code which the report targets to.
 */ 
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

/**
 * Plot the cluster bar graph 
 * @param data, type=array, receive data from server 
 * plot the data dynamically based on data from database 
 */ 
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
